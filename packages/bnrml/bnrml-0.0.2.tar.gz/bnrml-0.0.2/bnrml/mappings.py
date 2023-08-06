#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by pat on 7/13/19
"""
.. currentmodule:: bnrml.mappings
.. moduleauthor:: Pat Daburu <pat@daburu.net>

This module contains utility functions that may be helpful when working with
mappings (y'know... like dictionaries).
"""
import json
from pathlib import Path
from typing import Mapping
import toml

#: supported file extensions for mapping files
SUPPORTED_MAPPING_FILE_EXTS = ('.toml', '.zip')


def loads(s: str) -> Mapping:
    """
    Convert a `JSON` or `TOML` string into a `Mapping`

    :param s: the string
    :return: the data structure represented by the string
    :raises ValueError: if the string isn't a proper example of a recognized
        format
    """
    # Try to load the data as JSON.
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        # It doesn't look like it's JSON encoded.
        pass
    # Try to load the data as TOML.
    try:
        return toml.loads(s)
    except toml.TomlDecodeError:
        # It doesn't seem to be TOML either.
        raise ValueError(
            'The format is not supported.  Supported formats are JSON '
            'and TOML.'
        )


def loadf(path: Path or str) -> Mapping:
    """
    Convert a `JSON` or `TOML` file to a mapping

    :return: the data structure represented by the string
    :raises ValueError: if the string isn't a proper example of a recognized
        format
    """
    _path = (
        path if isinstance(path, Path)
        else Path(path)
    ).expanduser().resolve()
    return loads(_path.read_text())
