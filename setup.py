#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, 'webbot', '__version__.py')) as f:
    exec(f.read(), about)

with open('README.md') as f:
    readme = f.read()

requires = [
    'selenium',
    'pyyaml'
]

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    url=about['__url__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    packages=['webbot'],
    python_requires='>=3.7',
    install_requires=requires,
    license=about['__license__'],
    entry_points={
        'console_scripts': [
            'webbot = webbot:main'
        ]
    },
    classifiers=[
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development',
    ],
)
