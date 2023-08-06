# !/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_namespace_packages
import unittest

# Install Requires Version
_NUMPY_VERSION                  = '1.15.4'
_SPHINX_VERSION_MIN             = '2.2.2'
_SPHINX_RTD_THEME_VERSION_MIN   = '0.4.3'

# Load long description from the README.rst file
with open("README.rst", "r") as readme:
    long_description = readme.read()


# Define the tests to be all files in tests/ that start with 'test_'
def test_suite():
    test_loader = unittest.TestLoader()
    return test_loader.discover('tests', pattern='test_*.py')


setup(
    name='pasam',
    packages=find_namespace_packages(),
    version='0.1.5',
    description='Path sampling package',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author='Stefanie Marti, Christoph Jaeggli',
    license='MIT License',
    author_email='stefanie.marti@insel.ch, christoph.jaeggli@insel.ch',
    url='https://github.com/jaegglic/pasam',
    keywords=['sampling', 'radiotherapy', 'delivery path'],
    python_requires='>=3.6',
    install_requires=[
        f'numpy=={_NUMPY_VERSION}',
        f'sphinx>={_SPHINX_VERSION_MIN}',
        f'sphinx_rtd_theme>={_SPHINX_RTD_THEME_VERSION_MIN}',
    ],
    test_suite='setup.test_suite',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
)
