#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
seamm_ff_util
Forcefield utilities for SEAMM
"""
import sys
from setuptools import setup, find_packages
import versioneer

short_description = __doc__.split("\n")

# from https://github.com/pytest-dev/pytest-runner#conditional-requirement
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pillow',
    'seamm_util',
    'packaging',
]
# 'rdkit' must be installed by hand using conda

# test_requirements = [
#     'pytest',
#     # TODO: put package test requirements here
# ]

setup(
    # Self-descriptive entries which should always be present
    name='seamm_ff_util',
    author="Paul Saxe",
    author_email='psaxe@molssi.org',
    description=("The SEAMM Forcefield utilities read and write forcefields, "
                 "assigns them to molecules, and creates energy expressions."),
    long_description=readme + '\n\n' + history,
    version=versioneer.get_version(),
    # version='0.2.1',
    cmdclass=versioneer.get_cmdclass(),
    license='BSD-3-Clause',

    # Which Python importable modules should be included when your package is installed
    # Handled automatically by setuptools. Use 'exclude' to prevent some specific
    # subpackage(s) from being added, if needed
    packages=find_packages(include=['seamm_ff_util']),

    # Optional include package data to ship with your package
    # Customize MANIFEST.in if the general case does not suit your needs
    # Comment out this line to prevent the files from being packaged with your software
    include_package_data=True,

    # Allows `setup.py test` to work correctly with pytest
    setup_requires=[] + pytest_runner,

    url='https://github.com/molssi-seam/seamm_ff_util',

    # Required packages, pulls from pip if needed; do not use for Conda
    # deployment
    install_requires=requirements,

    test_suite='tests',
    # tests_require=test_requirements,

    # Valid platforms your code works on, adjust to your flavor
    platforms=['Linux',
               'Mac OS-X',
               'Unix',
               'Windows'],

    # Manual control if final package is compressible or not, set False to
    # prevent the .egg from being made
    zip_safe=False,

    keywords='seamm_ff_util',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
