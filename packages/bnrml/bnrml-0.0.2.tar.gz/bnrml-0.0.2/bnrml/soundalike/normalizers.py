#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 9/9/19
"""
.. currentmodule:: bnrml.soundalike.normalizers
.. moduleauthor:: Pat Daburu <pat@daburu.net>

This module contains extensions for normalizers the perform fuzzy matching.
"""
from typing import Dict, Iterable, List, NamedTuple, Union
from . import distance, encoding
from .distance import TextDistance
from .encoding import FuzzyEncoder
from ..normalizers import Normal, NormalsIndex


class SourceNormal(NamedTuple):
    """Associates a ``Normal`` definition with a source string."""
    source: str  #: a source string
    normal: Normal  #: a normal associated with the source string


class DistanceNormal(NamedTuple):
    """Describes the distance between a ``Normal`` and its source string."""
    #: the calculated distance from a string to one of the keys in a normal
    #: definition
    distance: float
    source_normal: SourceNormal


class SoundalikeNormalsIndex(NormalsIndex):
    """
    This is a `Normal` indexer that attempts fuzzy matching in cases where no
    direct match is found.
    """
    def __init__(
            self,
            normals: Iterable[Normal] = None,
            encoder: Union[FuzzyEncoder, str] = 'soundex',
            text_distance: Union[distance.TextDistance, str] = 'levenshtein'
    ):
        # Let the superclass do its thing.
        super().__init__(normals=normals)
        # Figure out what we'll use to encode strings.
        self._encoder = (
            encoder if isinstance(encoder, FuzzyEncoder)
            else encoding.encoder(encoder)()
        )  #: the principal encoder
        self._text_distance = (
            text_distance if isinstance(text_distance, TextDistance)
            else distance.text_distance(text_distance)()
        )  #: the text distance utility
        #: an index of soundalike-encoded strings (keys) mapped to the
        #: the source strings and normal definitons from which the strings
        #: came
        self._by_code: Dict[str, List[SourceNormal]] = {}

    def update(self, normals: Iterable[Normal] = None) -> 'NormalsIndex':
        """
        Generate the indexes.

        :return: this instance
        """
        # Let the superclass perform its work.
        super().update(normals)
        # Create an empty index.
        by_code: Dict[str, List[SourceNormal]] = {}

        # Let's go through all the normals.
        for normal in self.normals:
            # Collect all the unique values.
            sources = set([normal.normal] + [a for a in normal.aliases])
            # Now let's go through all the sources (which include the normal
            # form and all the aliases).
            for source in sources:
                # If there is, somehow, an empty value...
                if not source:
                    continue  # ...just move along.
                # Lowercase the source string and encode it.
                code = self._encoder.encode(self.std_key(source))
                # If no usable code was generated...
                if not code:
                    continue  # ...skip it.
                # Create a `SourceNormal` data object to keep track of the
                # fact that this source is associated with this normal
                # definition.
                source_normal = SourceNormal(
                    source=source,
                    normal=normal
                )
                # We may have seen this code before, so let's try to just
                # append this value...
                try:
                    by_code[code].append(source_normal)
                except KeyError:
                    # ...but if we haven't, we need to start a new list...
                    source_normals = [source_normal]
                    # ...and file it under this code as the key.
                    by_code[code] = source_normals

        # When we're finished, we can replace the existing index.
        self._by_code = by_code
        # The caller expects us to return this instance.
        return self

    def search(self, s: str) -> Normal or None:
        """
        Search for a normal definition.

        :param s: the denormalized string
        :return: the normal definition or `None`
        """
        # Let the superclass take a shot.
        normal = super().search(s)
        # If the superclass found something...
        if normal:
            # ...that's our answer.
            return normal

        # Standardize the input.
        s_std = self.std_key(s)

        # Encode the string to its fuzzy matching hash.
        code = self._encoder.encode(s_std)

        # Get all the normal definitions that are indexed under this
        # fuzzy matching hash code.
        soundalikes: Iterable[SourceNormal] = self._by_code.get(code)

        # If we don't recognize the code at all...
        if not soundalikes:
            # ...we don't have a match.
            return None

        # Sort the soundalikes according to their distance from the original
        # string.
        soundalikes_sorted: List[DistanceNormal] = sorted(
            [
                DistanceNormal(
                    distance=self._text_distance.distance(s_std, sn.source),
                    source_normal=sn
                )
                for sn in soundalikes
            ],
            key=lambda dn: dn.distance
        )
        # Return the normal definition that sorted to the top.
        return soundalikes_sorted[0].source_normal.normal
