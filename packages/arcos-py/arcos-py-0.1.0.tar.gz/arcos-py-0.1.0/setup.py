#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import pathlib

REQUIRED = [
    'requests',
    'numpy',
    'pandas',
    'geopandas',
    'shapely',
    'fiona',
]


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(
  author="Marc Rauckhorst",
  author_email='mwrauck@sas.upenn.edu',
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
  description="Python equivalent of the Washington Post's ARCOS R-package for accessing their ARCOS API",
  license="MIT license",
  include_package_data=True,
  packages=find_packages(exclude=("tests",)),
  install_requires = REQUIRED,
  name='arcos-py',
  version='0.1.0',
  zip_safe=False,
)
