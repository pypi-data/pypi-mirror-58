#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: setup
# Created: 21.07.2012
# License: MIT License

import os
from setuptools import setup

VERSION = "1.0.1"
AUTHOR_NAME = 'Manfred Moitzi'
AUTHOR_EMAIL = 'me@mozman.at'


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return "File '%s' not found.\n" % fname


setup(name='dxfgrabber',
      version=VERSION,
      description='A Python library to grab information from DXF drawings - all DXF versions supported.',
      author=AUTHOR_NAME,
      url='https://github.com/mozman/dxfgrabber.git',
      download_url='https://github.com/mozman/dxfgrabber/releases',
      author_email=AUTHOR_EMAIL,
      packages=['dxfgrabber'],
      provides=['dxfgrabber'],
      keywords=['DXF'],
      long_description=read('README.rst') + read('NEWS.rst'),
      platforms="OS Independent",
      license="MIT License",
      classifiers=[
          "Development Status :: 7 - Inactive",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries :: Python Modules", ]
)
