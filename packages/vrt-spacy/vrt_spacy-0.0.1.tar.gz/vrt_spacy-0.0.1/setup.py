#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Michael Ruppert <michael.ruppert@fau.de>
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='vrt_spacy',
    version='0.0.1',
    packages=['vrt_spacy'],
    url='https://github.com/miweru/vrt_spacy',
    license='GPL-3.0',
    author='Michael Ruppert',
    author_email='michael.ruppert@fau.de',
    description='creating vrt corpora',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        "smart_open>=1.9.0",
        "spacy>=2.2.3",
        "vrt-generator>=0.0.6"
    ],
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
    ],
)
