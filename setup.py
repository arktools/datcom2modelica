#!/usr/bin/env python

# Copyright 2012 Lenna X. Peterson (github.com/lennax)
# All rights reserved
# License: GPL v3
# This program comes with ABSOLUTELY NO WARRANTY. This is free software 
# and you are welcome to distribute it under certain conditions. 
# For details, see license.txt

from setuptools import setup, find_packages

requires = []

try:
    import argparse
except ImportError:
    requires.append('argparse')

setup(
    #name='datcom2modelica',
    version='0.0.1',
    license='GPL v3',
    description='DATCOM to modelica converter',
    author='James Goppert',
    author_email='james.goppert@gmail.com',
    url='http://github.com/arktools/datcom2modelica',
    packages=find_packages(),
    scripts=['scripts/convert.py'],
    requires=requires,
    test_suite='test',
)
