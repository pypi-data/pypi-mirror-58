#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 9/8/19
"""
.. currentmodule:: bnrml.soundalike
.. moduleauthor:: Pat Daburu <pat@daburu.net>

This package contains fuzzy string matching goodies.
"""
from .distance import (
    UnknownTextDistanceException,
    TextDistances,
    TextDistance,
    Hamming,
    Levenshtein,
    text_distance
)
from .encoding import (
    encoder,
    FuzzyEncoder,
    SoundexEncoder,
    NysiisEncoder,
    MetaphoneEncoder,
    DMetaphoneEncoder
)
from .normalizers import SoundalikeNormalsIndex
