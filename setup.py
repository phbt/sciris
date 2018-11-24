#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from setuptools import setup, find_packages

# Optionally define extras
if 'minimal' in sys.argv:
    sys.argv.remove('minimal')
    extras = []
else:
    extras = [
        'dill',              # File I/O
        'gitpython',         # Version information
        'openpyxl>=2.5',     # Spreadsheet functions
        'pandas',            # Spreadsheet input
        'psutil',            # Load monitoring
        'xlrd',              # Spreadsheet input
        'xlsxwriter',        # Spreadsheet output
        'requests',          # HTTP methods
        ]

# Get version information
versionfile = 'sciris/sc_version.py'
with open(versionfile, 'r') as f:
    versiondict = {}
    exec(f.read(), versiondict)
    version = versiondict['__version__']

CLASSIFIERS = [
    'Environment :: Console',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GPLv3',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Development Status :: 4 - Beta',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.7',
]

setup(
    name='sciris',
    version=version,
    author='ScirisOrg',
    author_email='info@sciris.org',
    description='Scientific tools for Python',
    url='http://github.com/sciris/sciris',
    keywords=['scientific', 'webapp', 'framework'],
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'matplotlib>=1.4.2', # Plotting
        'numpy>=1.10.1',     # Numerical functions
    ] + extras,              # Optional dependencies
)
