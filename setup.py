#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import cprint

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cprint',
    version=cprint.__version__,
    author='Erwan Vasseure',
    author_email='e.vasseure@gmail.com',
    license='MIT',
    description='Printing and debugging with color',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/EVasseure/cprint',
    include_package_data=True,
    packages=['cprint'],
)
