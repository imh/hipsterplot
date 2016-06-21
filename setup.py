#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MIT Licensed. See hipsterplot.py for more information.

from setuptools import setup
from setuptools.command import sdist

sdist.READMES = ("README.md",) # Includes it in the source distribution

metadata = {
  "name": "hipsterplot",
  "version": "0.1",
  "author": "Ian Horn and Danilo J. S. Bellini",
  "author_email": "horn.imh@gmail.com ; danilo.bellini.gmail.com",
  "url": "http://github.com/imh/hipsterplot",
  "description": "because matplotlib is too mainstream",
  "license": "MIT",
  "py_modules": ["hipsterplot"],
}

metadata["long_description"] = """
Plots a function as a string by calling the Python ``print`` function.

See the `GitHub project page <{url}>`_ for more information.
""".format(url=metadata["url"])

metadata["classifiers"] = [
  "Development Status :: 2 - Pre-Alpha",
  "Environment :: Console",
  "Intended Audience :: Education",
  "Intended Audience :: Science/Research",
  "Intended Audience :: Other Audience",
  "License :: OSI Approved :: MIT License",
  "Operating System :: POSIX :: Linux",
  "Operating System :: OS Independent",
  "Programming Language :: Python",
  "Programming Language :: Python :: 2",
  "Programming Language :: Python :: 2.6",
  "Programming Language :: Python :: 2.7",
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3.2",
  "Programming Language :: Python :: 3.3",
  "Programming Language :: Python :: 3.4",
  "Programming Language :: Python :: 3.5",
  "Topic :: Scientific/Engineering",
  "Topic :: Scientific/Engineering :: Visualization",
]

setup(**metadata)
