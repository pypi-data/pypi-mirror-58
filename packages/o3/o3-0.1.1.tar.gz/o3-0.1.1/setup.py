#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    setup_requires=['pbr'],
    pbr=True,
)
