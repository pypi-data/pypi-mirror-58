#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 9/8/19
"""
.. currentmodule:: bnrml.soundalike.distance
.. moduleauthor:: Pat Daburu <pat@daburu.net>

Just how similar are two strings?
"""
from abc import ABC
from enum import Enum
import string
from typing import Callable, Type
import textdistance
from pytypewriter import pycls, pyfqn, InvalidTypeException
from ..errors import BnrmlException


_ZERO_PUNCTUATION = str.maketrans(
    '', '',
    string.punctuation
)  #: string transform that eliminates punctuation


class UnknownTextDistanceException(BnrmlException):
    """
    Raised when a caller attempts to retrieve an unknown
    :py:class:`TextDistance <TextDistance>`

    .. seealso::

        :py:func:`text_distance`
    """


class TextDistances(Enum):
    """
    This is an enumeration of the known, built-in text measuring rods.
    """
    HAMMING = 'HAMMING'
    LEVENSHTEIN = 'LEVENSHTEIN'


class TextDistance(ABC):
    """
    This is a utility object that measures the "distance" (or difference)
    between two words.
    """

    #: indicates a text distance beyond the threshold
    OUT_OF_RANGE: float = float('inf')

    def __init__(
            self,
            distance_fn: Callable[[str, str], int],
            ndistance_fn: Callable[[str, str], float],
            threshold: int
    ):
        """

        :param distance_fn: a function that measures the quantitative text
            distance between two words
        :param ndistance_fn: a function that measures the distance between two
            words and returns a value between 0 and 1 where 0 means the words
            are the same and 1 means they are completely different
        :param threshold: the maximum quantitative distance between two words
            before they are considered completely distinct
        """
        self._distance_fn: Callable[[str, str], int] = distance_fn
        self._ndistance_fn: Callable[[str, str], float] = ndistance_fn
        self._threshold: int = threshold

    @property
    def threshold(self) -> int:
        """
        Get the maximum quantitative distance between two words before they are
        considered completely distinct.
        """
        return self._threshold

    @threshold.setter
    def threshold(self, value: int):
        """
        Set the maximum quantitative distance between two words before they are
        considered completely distinct.

        :param value: the threshold value
        """
        if value < 1:
            raise ValueError("'value' must be > 1.")
        if value >= self.OUT_OF_RANGE:
            raise ValueError(
                "'value' must not exceed the maximum (out of range) value."
            )
        self._threshold = value

    @classmethod
    def key(cls) -> str:
        """
        This is a key handle for this type of ruler.
        """
        return pyfqn(cls)

    def distance(
            self,
            texta: str,
            textb: str,
            normalized: bool = False
    ) -> float:
        """
        Encode a string to its fuzzy matching hash.

        :param texta: a string
        :param textb: another string
        :param normalized: `True` to return a normalized value between 0 and
            1 where 0 means the same and 1 means completely different
        :return: the distance

        .. note::

            If the distance exceeds the :py:func:`threshold` value, a very large
            value equal to :py:attr:`OUT_OF_RANGE` is returned to the caller.
        """
        # Clean up the input strings.
        _a = texta.strip().lower().translate(_ZERO_PUNCTUATION)
        _b = textb.strip().lower().translate(_ZERO_PUNCTUATION)
        # Use the function supplied to get the distance.
        if normalized:
            return self._ndistance_fn(texta, textb)
        # Get the distance.
        d = float(self._distance_fn(texta, textb))
        # If the distance is within the threshold, return it.  Otherwise return
        # the "out-of-range" value.
        return d if d <= self._threshold else self.OUT_OF_RANGE


class Hamming(TextDistance):
    """
    This is a rule that returns the
    `Hamming distance <https://en.wikipedia.org/wiki/Hamming_distance>`_
    between two strings.
    """
    def __init__(self, threshold: int = 4):
        """

        :param threshold: the maximum quantitative distance between two words
            before they are considered completely distinct
        """
        super().__init__(
            distance_fn=textdistance.hamming.distance,
            ndistance_fn=textdistance.hamming.distance,
            threshold=threshold
        )

    @classmethod
    def key(cls) -> str:
        """
        This is a key handle for this type of ruler.
        """
        return TextDistances.HAMMING.name


class Levenshtein(TextDistance):
    """
    This is a rule that returns the
    `Levenshtein distance <hhttps://en.wikipedia.org/wiki/Levenshtein_distance>`_
    between two strings.
    """
    def __init__(self, threshold: int = 4):
        """

        :param threshold: the maximum quantitative distance between two words
            before they are considered completely distinct
        """
        super().__init__(
            distance_fn=textdistance.levenshtein.distance,
            ndistance_fn=textdistance.levenshtein.distance,
            threshold=threshold
        )

    @classmethod
    def key(cls) -> str:
        """
        This is a key handle for this type of ruler.
        """
        return TextDistances.LEVENSHTEIN.name


_TEXT_DISTANCE_TYPES = {
    **{
        k: v for k, v in {
            TextDistances.HAMMING: Hamming,
            TextDistances.LEVENSHTEIN: Levenshtein
        }.items()
    },
    **{
        t.key(): t for t in [
            Hamming,
            Levenshtein
        ]
    }
}  #: a mapping of encoder type keys to encoder types


def text_distance(key: TextDistances or str) -> Type:
    """
    Get a :py:class:`Rod` type that corresponds to a given enumeration
    value or name.

    :param key: the name
    :return: the corresponding type
    :raises KeyError: if no mapping exists for the key
    """
    try:
        return _TEXT_DISTANCE_TYPES[
            key.upper() if isinstance(key, str)
            else key
        ]
    except KeyError:
        try:
            _cls = pycls(key)
            return _cls()
        except InvalidTypeException:
            raise UnknownTextDistanceException(
                f"No class is associated with text distance key "
                f"'{key}'."
            )
