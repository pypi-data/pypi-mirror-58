#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 9/8/19
"""
.. currentmodule:: bnrml.soundalike.encoding
.. moduleauthor:: Pat Daburu <pat@daburu.net>

Generate soundalike encodings for strings.
"""
from abc import ABC
from enum import Enum
from functools import partial
import re
import string
from typing import Callable, cast, Type
import phonetics
from pytypewriter import pyfqn


_ZERO_PUNCTUATION = str.maketrans(
    '', '',
    string.punctuation
)  #: string transform that eliminates punctuation

_WORD_DIV = re.compile(r'\s+')  #: identifies boundaries between words


class Encoders(Enum):
    """
    This is an enumeration of the known, built-in soundalike encoders.
    """
    SOUNDEX = 'SOUNDEX'
    NYSIIS = 'NYSIIS'
    METAPHONE = 'METAPHONE'
    DMETAPHONE = 'DMETAPHONE'


class FuzzyEncoder(ABC):
    """
    Use a "fuzzy" encoder to generate soundalike codes for strings.
    """
    def __init__(self, fn: Callable[[str], str]):
        """

        :param fn: the function that performs the soundalike
        """
        self._fn: Callable[[str], str] = fn

    @classmethod
    def key(cls) -> str:
        """
        This is a key handle for this type of encoder.
        """
        return pyfqn(cls)

    def encode(self, s: str) -> str or None:
        """
        Encode a string to its fuzzy matching hash.

        :param s: the string
        :return: the encoding (or `None` if no encoding is possible)
        """
        # No input means no output.
        if not s:
            return None
        # Clean up the input string.
        _s = s.strip().lower().translate(_ZERO_PUNCTUATION)
        # Check again... if we were given an empty string, or just punctuation
        # we aren't going to generate a code.
        if not _s:
            return None
        # There may be multiple individual strings, so we may need to encode
        # multiple times.
        codes = [
            self._fn(i) for i in _WORD_DIV.split(_s)
        ]
        # Put it all back together.
        code = ' '.join(codes)
        # Return what we got.
        return code.upper() if code else None


class SoundexEncoder(FuzzyEncoder):
    """
    This is a fuzzy encoder that uses the
    `soundex <https://en.wikipedia.org/wiki/Soundex>`_ algorithm.
    """
    def __init__(self, size: int = 4):
        super().__init__(
            fn=cast(
                Callable[[str], str],
                partial(phonetics.soundex, size=size)
            )
        )

    @classmethod
    def key(cls) -> str:
        """
        This is a key handle for this type of encoder.
        """
        return Encoders.SOUNDEX.name


class NysiisEncoder(FuzzyEncoder):
    """
    This is a fuzzy encoder that uses the
    `NYSIIS <https://www.health.ny.gov/prevention/immunization/information_system/>`_
    algorithm.
    """
    def __init__(self):
        super().__init__(
            fn=cast(
                Callable[[str], str],
                phonetics.nysiis
            )
        )

    @classmethod
    def key(cls) -> str:
        """
        This is a key handle for this type of encoder.
        """
        return Encoders.NYSIIS.name


class MetaphoneEncoder(FuzzyEncoder):
    """
    This is a fuzzy encoder that uses the
    `metaphone <https://en.wikipedia.org/wiki/Metaphone>`_ algorithm.
    """
    def __init__(self):
        super().__init__(
            fn=cast(
                Callable[[str], str],
                phonetics.metaphone
            )
        )

    @classmethod
    def key(cls) -> str:
        """
        This is a key handle for this type of encoder.
        """
        return Encoders.METAPHONE.name


class DMetaphoneEncoder(FuzzyEncoder):
    """
    This is a fuzzy encoder that uses the
    `double metaphone <https://en.wikipedia.org/wiki/Metaphone>`_ algorithm.
    """
    def __init__(self):
        super().__init__(
            fn=self._dmetaphone
        )

    @classmethod
    def key(cls) -> str:
        """
        This is a key handle for this type of encoder.
        """
        return Encoders.DMETAPHONE.name

    @classmethod
    def _dmetaphone(cls, s: str):
        code = phonetics.dmetaphone(s)
        return code[0] if code else None


_ENCODER_TYPES = {
    **{
        k: v for k, v in {
            Encoders.SOUNDEX: SoundexEncoder,
            Encoders.NYSIIS: NysiisEncoder,
            Encoders.METAPHONE: MetaphoneEncoder,
            Encoders.DMETAPHONE: DMetaphoneEncoder
        }.items()
    },
    **{
        t.key(): t for t in [
            SoundexEncoder,
            NysiisEncoder,
            MetaphoneEncoder,
            DMetaphoneEncoder
        ]
    }
}  #: a mapping of encoder type keys to encoder types


def encoder(key: Encoders or str) -> Type:
    """
    Get a :py:class:`FuzzyEncoder` type that corresponds to a given enumeration
    value or name.

    :param key: the name
    :return: the corresponding type
    :raises KeyError: if no mapping exists for the key
    """
    return _ENCODER_TYPES[
        key.upper() if isinstance(key, str)
        else key
    ]
