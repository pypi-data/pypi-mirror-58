"""
This file is part of o3.py

Ozone or trioxide, is an allotrope of Oxygen. It's found in the higher
atmosphere, and can also be smelled after rain.
Ozone configuration library is meant to be used when building cloud native
applications (or 12 Factor applications).

Copyright (c) 2009-2019, Oz Tiram
License: LGPL (see LICENSE for details)
"""
import os

class Config:
    """
    This class is a nice wrapper around os.getenv

    An object that gets configuration values from environment
    variables.
    All variables are expected to be capital letters and attributes
    are all snake_case.
    """
    def __getattr__(self, attr):
        try:
            return os.environ[attr.upper()]
        except KeyError:
            raise AttributeError(attr)

