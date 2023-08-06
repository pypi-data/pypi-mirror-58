#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 6/29/19
"""
.. currentmodule:: bnrml.normalizers
.. moduleauthor:: Pat Daburu <pat@daburu.net>

Be normal!
"""
from abc import ABC, abstractmethod
from functools import lru_cache
from collections import OrderedDict
from enum import Enum
import hashlib
from pathlib import Path
import string
from typing import (
    Any,
    Dict,
    FrozenSet,
    Iterable,
    List,
    Mapping,
    NamedTuple,
    Union
)
from frozenordereddict import FrozenOrderedDict
from pytypewriter import Exportable, pycls, pyfqn
from . import mappings
from .errors import BnrmlException


_ZERO_PUNCTUATION = str.maketrans(
    '', '',
    string.punctuation
)  #: string transform that eliminates punctuation


class Normal(Exportable):
    """
    This is a data object that represents a "normal" value along with all of
    its abbreviations and aliases.
    """
    __slots__ = ['_normal', '_abbreviations', '_aliases', 'hash_']

    class Components(Enum):
        """
        This is an enumeration of the principal components of a `Normal`.
        """
        NORMAL = 'NORMAL'  #: the normal form
        ABBREVIATION = 'ABBREVIATION'  #: an abbreviation
        ALIAS = 'ALIAS'  #: an alias

    def __init__(
            self,
            normal: str,
            abbreviation: str,
            aliases: Iterable[str]
    ):
        """

        :param normal: the normal form
        :param abbreviation: the abbreviated form
        :param aliases: aliases
        """
        self._normal = normal
        self._abbreviation = abbreviation
        self._aliases = frozenset(aliases)
        self.hash_: int or None = None

    @property
    def normal(self) -> Union[str, int]:
        """
        Get the normal form.
        """
        return self._normal

    @property
    def abbreviation(self) -> str:
        """
        Get the abbreviated form
        """
        return self._abbreviation

    @property
    def aliases(self) -> FrozenSet[str]:
        """
        Get the aliases.
        """
        return self._aliases

    def export(self) -> Mapping[str, Any]:
        """
        Export the instance as a mapping of simple types.

        :return: the mapping
        """
        return {
            'normal': self._normal,
            'abbreviation': self._abbreviation,
            'aliases': list(self._aliases)
        }

    @classmethod
    def load(cls, data: Mapping[str, Any]) -> 'Normal':
        """
        Create an instance from a mapping.

        :param data: the data
        :return: the instance
        """
        # Construct the instance.
        obj = cls(
            **{
                k: data.get(k) for k in [
                    'normal',
                    'abbreviation',
                    'aliases'
                ]
            }
        )
        # If the data contains a ready-made hash, let's apply it now.
        hash_ = data.get('hash')
        if hash_ is not None:
            setattr(obj, 'hash_', hash_)
        # That's that.
        return obj

    @classmethod
    def loadd(cls, normal: str, data: Mapping[str, Any]) -> 'Normal':
        """
        Create an instance from normal value and a mapping of other
        attribute values (as you might find them in a dictionary that utilizes
        the normal value as a key and the other attributes as a value object).

        :param normal: the normal form (key)
        :param data: the object defining other attributes
        :return:
        """
        return cls.load(
            {
                'normal': normal,
                **data
            }
        )

    def _makehash(self) -> int:
        """
        Generate a hash for the datum.

        :return: the hash
        """
        md5 = hashlib.sha3_512(  # pylint: disable=no-member
            str(
                {
                    'normal': self._normal,
                    'abbreviation': self._abbreviation,
                    'aliases': list(self._aliases),
                }
            ).encode('UTF-8')
        )
        return int(md5.hexdigest(), 16)

    def __hash__(self):
        if self.hash_ is None:
            self.hash_ = self._makehash()
        return self.hash_

    def __eq__(self, other):
        return self.hash_ == getattr(other, 'hash_', None)

    def __ne__(self, other):
        return not self.hash_


class IndexKeyViolation(NamedTuple):
    """
    This is a data object that describes a key conflict (duplicate values)
    in a set of normal definitions.

    .. seealso::

        :py:class:`IndexKeyViolationException`
    """
    key: str
    component: Normal.Components


class IndexKeyViolationException(BnrmlException):
    """
    This exception is raised in response to attempts to index multiple normal
    definitions that have conflicting keys (duplicate values).
    """
    def __init__(
            self,
            message: str,
            violations: Iterable[IndexKeyViolation],
            inner: Exception = None
    ):
        """

        :param message: the exception message
        :param violations: the individual violations
        :param inner: the exception that caused this exception
        """
        super().__init__(message=message, inner=inner)
        self._violations = list(violations) if violations else []

    @property
    def violations(self) -> Iterable[IndexKeyViolation]:
        """
        Get the individual violations.
        """
        return iter(self._violations)


class NormalsIndex:
    """
    This is an indexer for :py:class:`Normal` definitions.
    """
    def __init__(self, normals: Iterable[Normal] = None):
        """

        :param normals: the initial normals contained in the index
        """
        #: the full set of normals
        self._normals = set(normals) if normals else set()
        #: normals indexed by the normal form
        self._by_normal: Dict[str, Normal] = {}
        #: normals indexed by abbreviations
        self._by_abbrev: Dict[str, Normal] = {}
        #: normals indexed by alias
        self._by_alias: Dict[str, Normal] = {}
        # If normal definitions were supplied...
        if self._normals:
            # ...update now.
            self.update()

    @property
    def normals(self) -> Iterable[Normal]:
        """
        Get the normals present in the index.
        """
        return iter(self._normals)

    @classmethod
    def std_key(cls, key: str) -> str:
        """
        Standardize an index key value.

        :param key: the key
        :return: the standard form
        """
        # Remove punctuation.
        _key = key.lower().translate(_ZERO_PUNCTUATION).strip()
        # Compress whitespace.
        return ' '.join(_key.split())

    def update(self, normals: Iterable[Normal] = None) -> 'NormalsIndex':
        """
        Generate the indexes.

        :return: this instance
        """
        # Create new data structures and indexes.
        _normals = (
            (
                self._normals | set(normals) if normals else set()
            )
            if normals else
            self._normals
        )
        by_normal = {}
        by_abbrev = {}
        by_alias = {}
        all_keys: Dict[str, Normal] = {}

        # We'll want to keep track of index violations.
        violations: List[IndexKeyViolation] = []
        for normal in _normals:
            # Index the normal forms, abbreviations, and aliases.
            for index, component, keys in [
                    (
                        by_normal,
                        Normal.Components.NORMAL,
                        [normal.normal]
                    ),
                    (
                        by_abbrev,
                        Normal.Components.ABBREVIATION,
                        [normal.abbreviation]
                    ),
                    (
                        by_alias,
                        Normal.Components.ALIAS,
                        normal.aliases
                    )
            ]:
                for key in keys:
                    # If the key is empty...
                    if not key:
                        # ...move along.
                        continue
                    # Standardize the key.
                    _key = self.std_key(key)
                    # If we've already seen this key but it's associated
                    # with another `Normal`...
                    if all_keys.get(_key) != normal:
                        violations.append(
                            IndexKeyViolation(
                                key=_key,
                                component=component
                            )
                        )
                        continue
                    else:
                        # Make note that we've seen this key.
                        all_keys[key] = normal
                        # Simply add this one to the index.
                        index[_key] = normal
        # If any violations were detected...
        if violations:
            # ...raise an exception.
            raise IndexKeyViolationException(
                message=f'Index violations exist in the series: {violations}',
                violations=violations
            )

        # It looks like we're good, so replace the existing data structures and
        # indexes.
        self._normals = _normals
        self._by_normal = by_normal
        self._by_abbrev = by_abbrev
        self._by_alias = by_alias

        # Return this instance to the caller.
        return self

    def search(self, s: str) -> Normal or None:
        """
        Search for a normal definition.

        :param s: the the denormalized string
        :return: the normal definition or `None`
        """
        _std = self.std_key(s)
        for idx in [self._by_normal, self._by_abbrev, self._by_alias]:
            try:
                return idx[_std]
            except KeyError:
                pass
        return None


class Normalization(Exportable):
    """
    A `Normalization` contains the results of an attempt to normalize a value.
    """
    __slots__ = [
        '_denormalized',
        '_normalized',
        '_normals',
        '_extras'
    ]

    def __init__(
            self,
            denormalized: str,
            normalized: str,
            normals: Iterable[Normal] = None,
            extras: OrderedDict = None
    ):
        """

        :param denormalized: the denormalized value
        :param normalized: the normal form
        :param normals: the :py:class:`Normal` definitions that match the
            denormalized value (if any)
        :param extras: extra values
        """
        self._denormalized = denormalized
        self._normalized = normalized
        self._normals = list(normals) if normals else []
        self._extras = (
            FrozenOrderedDict(extras) if extras else FrozenOrderedDict()
        )

    @property
    def denormalized(self) -> str:
        """
        Get the denormalized value.
        """
        return self._denormalized

    @property
    def normalized(self) -> str:
        """
        Get the normal form.
        """
        return self._normalized

    @property
    def normals(self) -> Iterable[Normal]:
        """
        Get the :py:class:`Normal` definitions that matched the denormalized
            value (if there were any)
        """
        return iter(self._normals)

    @property
    def extras(self) -> FrozenOrderedDict:
        """
        Get the extra values.
        """
        return self._extras

    def export(self) -> Mapping[str, Any]:
        """
        Export the instance as a mapping of simple types.

        :return: the mapping
        """
        return {
            k: v for k, v in
            {
                **{slot[1:]: getattr(self, slot) for slot in self.__slots__},
                'normals': [n.export() for n in self._normals],
                'extras': dict(self.extras)
            }.items()
        }

    @classmethod
    def load(cls, data: Mapping[str, Any]) -> Any:
        """
        Create an instance from a mapping.

        :param data: the data
        :return: the instance
        """
        return cls(**data)


def load_normals(data: Mapping[str, Any]) -> Iterable[Normal]:
    """
    Parse :py:class:`Normals <Normal>` from a file.

    :param data: the data mapping that describes the `Normals`
    :return: the normals described in the file
    """
    # If there is some data to work with...
    if data:
        # ...go through all the keys in the dictionary.  (We'll consider those
        # keys to be the normal form.)
        for k, v in data.items():
            # Create the `Normal` from the data at hand...
            normal = Normal(
                normal=k,
                abbreviation=v.get('abbreviation'),
                aliases=v.get('aliases')
            )
            # ...and yield it to the caller.
            yield normal


def loadf_normals(path: Path or str) -> Iterable[Normal]:
    """
    Load :py:class:`Normals <Normal>` from a file.

    :param path: the file path
    :return: the normals described in the file
    """
    _path = (
        path if isinstance(path, Path) else Path(path)
    ).expanduser().resolve()
    data = mappings.loadf(path=_path)
    return load_normals(data=data.get('normals'))


class Normalizer(Exportable, ABC):
    """
    Normalizers convert values to their normal forms (if possible).
    """

    def __init__(
            self,
            **kwargs
    ):
        """

        :param normals: the set of normals
        :param kwargs: additional keyword arguments
        """
        self._kwargs: Dict[str, Any] = kwargs  #: the subclass keyword arguments

    @abstractmethod
    def normalize(
            self,
            s: str,
            default: Union[str, Normal, None] = None
    ) -> Normalization or None:
        """
        Normalize a value.

        :param s: the value to normalize
        :param default: the default value to return if no normal value applies
        :return: the normalized value
        """

    def export(self) -> Mapping[str, Any]:
        """
        Export the instance as a mapping of simple types.

        :return: the mapping
        """
        return {
            'normalizer': {
                'type': pyfqn(self),
                'args': {
                    k: v for k, v in self._kwargs
                }
            }
        }

    @classmethod
    def load(cls, data: Mapping[str, Any]) -> Any:
        """
        Create an instance from a mapping.

        :param data: the data
        :return: the instance
        """
        # Get the `normalizer` value from the data.
        normalizer_data = data['normalizer']
        # Let's figure out what type of `Normalizer` we're going to create.
        _type = normalizer_data.get('type')
        # Let's figure out what type we're supposed to load.
        _cls = pycls(_type) if _type else cls
        # If its not this class...
        if _cls is not cls:
            # ...let the other class' load method take it from here.
            return _cls.load(data)
        # Otherwise, parse out the arguments...
        _args = normalizer_data.get('args', ())
        # ...and create an instance.
        return _cls(**_args)

    @classmethod
    def loadf(cls, path: Union[Path, str]) -> 'Normalizer':
        """
        Load a normalizer from a configuration file.

        :param path: the path to the configuration file
        :return: the normalizer
        """
        data = mappings.loadf(path)
        return cls.load(data)


class SimpleNormalizer(Normalizer, ABC):
    """
    This is an implementation of :py:class:`Normalizer` that provides standard
    logic for working with a pre-defined set of :py:class:`Normals <Normal>`
    in a single index.
    """

    def __init__(
            self,
            normals: Union[Iterable[Normal], Path, str] = None,
            prefer: Normal.Components = Normal.Components.NORMAL,
            index_type: Union[type, str] = NormalsIndex,
            **kwargs
    ):
        """

        :param normals: the set of normals or the path to a file that defines
            the normals
        :param prefer: indicates a preference for using the
            :py:attr:`normal <bnrml.normalizers.Normal.Components.NORMAL>`
            form (the default) or the
            :py:attr:`abbreviation <bnrml.normalizers.Normal.Components.ABBREVIATION>`
            as `normalized`
        :param index_type: the :py:class:`NormalsIndex <NormalsIndex>` type
        :param kwargs: additional keyword arguments
        """
        # Pass the keyword arguments to the parent.
        super().__init__(**kwargs)
        # Get the normalization preference.
        self._prefer: Normal.Components = prefer
        # If the preference isn't either `NORMAL` or `ABBREVIATION`, it's not
        # a valid value.
        if self._prefer not in [
                Normal.Components.NORMAL,
                Normal.Components.ABBREVIATION
            ]:
            raise ValueError(
                f"The `prefer` parameter must be {Normal.Components.NORMAL} or "
                f"{Normal.Components.ABBREVIATION}"
            )
        # Extract the normals (if any) from the constructor args.
        self._normals: List[Normal] = (
            list(loadf_normals(path=normals))
            if isinstance(normals, (Path, str))
            else list(normals)
        ) if normals else []
        # Let's figure out what we're using for a `NormalsIndex`.
        _index_type = (
            index_type if isinstance(index_type, type)
            else pycls(index_type)
        )
        # Generate the index from the normals that were provided.
        self._nindex: NormalsIndex = _index_type().update(self._normals)

    @lru_cache()
    def normalize(
            self,
            s: str,
            default: Union[str, Normal, None] = None
    ) -> Normalization or None:
        """
        Normalize a value.

        :param s: the value to normalize
        :param default: the default value to return if no normal value applies
        :return: the normalized value
        """
        # Let the index do it's work.
        normal = self._nindex.search(s)
        # If the index returned a `Normal`...
        if normal:
            # The preferred value to return as the "normalized" value may be the
            # `normal`, but if the normalizer has been configured to prefer the
            # abbreviation, we'll use that.
            _normalized = (
                normal.abbreviation
                if self._prefer == Normal.Components.ABBREVIATION
                else normal.normal
            )
            # Just in case this normalizer prefers the abbreviation, but the
            # selected normal doesn't actually have an abbreviation (resulting
            # in an empty value for `_normalized`)...
            if not _normalized:
                # Let's resort to the safe normal form.
                _normalized = normal.normal
            # Now we can construct a normalization.
            return Normalization(
                denormalized=s,
                normalized=_normalized,
                normals=[normal]
            )
        # We need to resort to the default, which may be `None`...
        if default is None:
            return None
        # If the `default` is a string...
        if isinstance(default, str):
            # ...we can construct a `Normalization` with no `Normal` instances.
            return Normalization(denormalized=s, normalized=s)
        # If the `default` is a `Normal`...
        if isinstance(default, Normal):
            # ...we can construct a `Normalization` using that information.
            return Normalization(
                denormalized=s,
                normalized=default.normal,
                normals=[default]
            )
        # If we get to this point it means that the `default` parameter isn't
        # of a type we can use here.
        raise TypeError(
            f"The type of the 'default' parameter ({type(default).__name__}) "
            f"is invalid."
        )

    def export(self) -> Mapping[str, Any]:
        """
        Export the instance as a mapping of simple types.

        :return: the mapping
        """
        data = dict(super().export())
        data['normalizer']['args']['normals'] = {
            n.normal: {
                k: v for k, v
                in n.export().items()
                # The normal form is the key.  Don't repeat it.
                if k != 'normal'
            }
            for n in self._normals
        }
        return data

    @classmethod
    def _load_parse_args(cls, args: Mapping[str, Any]) -> Mapping[str, Any]:
        """
        Subclasses may override this method to parse arguments constructor
        arguments as they are parsed in the :py:funct:`load` method.

        :param args: the argument dictionary
        :return: the modified argument dictionary
        """
        return args

    @classmethod
    def load(cls, data: Mapping[str, Any]) -> Any:
        """
        Create an instance from a mapping.

        :param data: the data
        :return: the instance
        """
        # Get the 'normalizer' key wherein the configuration resides.
        normalizer_data = data['normalizer']
        # Let's see what type we're working with.
        _type = normalizer_data.get('type')
        # If no type is specified, assume the current type.
        _cls = pycls(_type) if _type else cls
        # Get the arguments.
        _args = normalizer_data.get('args', ())
        # Let's see if there is a 'normals' argument.  If so, it'll be
        # complex...
        _normals = _args.get('normals', {})
        # ...so we need to do some additional work to parse them into
        # `Normal` instances.
        _args['normals'] = [
            Normal.loadd(normal, data)
            for normal, data
            in _normals.items()
        ]
        # Let's see if the args contain the `prefer` argument.
        _prefer = _args.get('prefer')
        if _prefer:
            try:
                _args['prefer'] = Normal.Components[str(_prefer).upper()]
            except KeyError:
                raise ValueError(
                    f'{repr(str(_prefer))} is not a valid argument for the '
                    f"'prefer' parameter."
                )
        # Give subclasses a change to further process the arguments.
        _args = cls._load_parse_args(_args)
        # That's that.
        return _cls(**_args)
