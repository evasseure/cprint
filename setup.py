#!/usr/bin/env python

from setuptools import setup, find_packages

import cprint

setup(
    name='cprint',
    version=cprint.__version__,
    packages=find_packages,
    author='Erwan Vasseure',
    description='Printing and debugging with color',
    long_description=open('README.md').read(),
    include_package_data=True,
    url='https://github.com/EVasseure/cprint',
)