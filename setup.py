#!/usr/bin/env python

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    with open(file_path, encoding='utf-8') as readme:
        return readme.read()


setup(
    name='sipster',
    version='0.0.1',
    author='Simon Gomizelj',
    author_email='simon@vodik.xyz',
    packages=find_packages(),
    license='Apache 2',
    url='https://github.com/vodik/sipster',
    description='Pure python tools for SIP testing',
    long_description=read('README.rst'),
    install_requires=[
        'aiosip',
    ],
    entry_points={
        'console_scripts': [
            'sipster=sipster.__main__:main'
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License'
    ],
)
