#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: bnrml
.. moduleauthor:: Pat Daburu <pat@daburu.net>

Be normal! (It's a string normalization framework.)
"""
from .normalizers import (
    load_normals,
    loadf_normals,
    SimpleNormalizer,
    Normal,
    Normalization,
    Normalizer
)
from .version import __version__, __release__
