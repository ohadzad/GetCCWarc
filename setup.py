"""Setup file for the GetCCWarc package."""

# This file is part of GetCCWarc.
# https://github.com/ohadzad/GetCCWarc

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2019, Ohad Zadok <ohadzad@gmail.com>

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import versioneer


TEST_REQUIRES = ['pytest', 'coverage', 'pytest-cov']

README_RST = ''
with open('README.rst') as f:
    README_RST = f.read()


setup(
    name='GetCCWarc',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description=('Easily get files from CC on S3 using file location, offset and length'),
    long_description=README_RST,
    license='MIT',
    author='Ohad Zadok',
    author_email='me@ohadzadok.com',
    url='https://github.com/ohadzad/GetCCWarc',
    packages=['GetCCWarc'],
    entry_points='''
    ''',
    install_requires=[],
    extras_require={
        'test': TEST_REQUIRES,
        ':python_version == "3.7"': ['futures'],
    },
    platforms=['linux', 'osx', 'windows'],
    keywords=['commoncrawl'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: Other/Nonlisted Topic',
        'Intended Audience :: Developers',
    ],
)
