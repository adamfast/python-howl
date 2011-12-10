#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='howl',
    version='1.0.0',
    description='A simple class to post to the Howl alert app from Python',
    author='Jeff Triplett',
    author_email='',
    url='https://github.com/adamfast/python-howl',
    packages=find_packages(),
    package_data={
    },
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
