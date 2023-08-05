#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
from LeafPy import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="leaf.py",
    version=__version__,
    author="Huaqing Ye",
    author_email="yhq1978@yahoo.com",
    description="a mini python web framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT License",
    keywords=['leaf.py', 'leaf.py web framework'],
    url="https://www.leafpy.org",
    packages=find_packages(),
    package_data={
        'LeafPy': [
            'examples/*.*',
            'examples/index/*.*',
            'examples/media/*.*',
            'examples/templates/*.*',
            'examples/views/*.*',
        ],
    },
    install_requires=[
        "sqlalchemy", "cheroot"
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    scripts=['scripts/LeafPy-admin.py'],
    platforms='any',
    python_requires='>=2.7',
)
