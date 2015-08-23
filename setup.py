#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cloudfront-edge-codes.
# https://github.com/heynemann/cloudfront-edge-codes

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>

from setuptools import setup, find_packages
from cloudfront_edge_codes import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'sphinx',
]

setup(
    name='cloudfront-edge-codes',
    version=__version__,
    description='Cloudfront Edge Codes is a translator that returns information on the edge node based on its code. ',
    long_description='''
Cloudfront Edge Codes is a translator that returns information on the edge node based on its code. 
''',
    keywords='cloudfront amazon aws edge codes translation parse',
    author='Bernardo Heynemann',
    author_email='heynemann@gmail.com',
    url='https://github.com/heynemann/cloudfront-edge-codes',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'cloudfront-edge-codes=cloudfront_edge_codes.cli:main',
        ],
    },
)
