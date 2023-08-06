#!/usr/bin/env python3
# -*- coding: utf8 -*-

import setuptools
import openfizzbuzz

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='openfizzbuzz',
    version=openfizzbuzz.__version__,
    author='Haytek',
    author_email='haytek34@gmail.com',
    description='Open minded fizzbuzz',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Haytek/openfizzbuzz',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6'

)
