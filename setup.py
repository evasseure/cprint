#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

import cprint

setup(
    name='cprint',
    version=cprint.__version__,
    author='Erwan Vasseure',
    description='Printing and debugging with color',
    long_description=open('README.md').read(),
    url='https://github.com/EVasseure/cprint',
    include_package_data=True,
    packages=['cprint'],
)