#!/usr/bin/env python
# encoding: utf-8
"""
setup.py

Installs the base django project onto your python path, update this if needed.
"""


from setuptools import setup, find_packages


setup(
    name='{{ PROJECT_NAME }}',
    version='0.1',
    packages=find_packages(
        exclude=['ez_setup', 'examples', 'tests']),
)
