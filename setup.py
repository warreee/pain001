# Copyright (C) 2023 Sebastian Rousseau.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The setup.py file for Python Pain001."""

from setuptools import setup

LONG_DESCRIPTION = """
The Pain001 library is a Python package that generates a Customer-to-
Bank Credit Transfer payload in the pain.001.001.03 format from a CSV
file.

The package is named after the standard file format for SEPA and non-
SEPA Credit Transfer, which is the Pain (payment initiation) format
001.001.03. The Pain001 library provides a convenient way for developers
to create payment files in this format.
""".strip()

SHORT_DESCRIPTION = """
Pain001 is a Python library for generating Customer-to-Bank Credit Transfer payloads in the ISO 20022 Standard's Pain.001.001.03 format from CSV files.""".strip()

DEPENDENCIES = [
    'csv',
    'xml',
    'os',
    'sys',
]

TEST_DEPENDENCIES = [
    'hypothesis',
    'mock',
    'python-Levenshtein',
]

VERSION = '0.0.1'
URL = 'https://github.com/sebastienrousseau/Pain001'

setup(
    name='pain001',
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,

    author='Sebastian Rousseau',
    author_email='sebastian.rousseau@gmail.com',
    license='Apache Software License',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',


        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
    ],

    keywords='command line interface cli python pain001 interactive bash tool',

    packages=['pain001', 'Payment', 'Initiation', 'SEPA',
              'Banking', 'Transfer', 'ISO20022', 'Credit', 'Bank'],

    install_requires=DEPENDENCIES,
    tests_require=TEST_DEPENDENCIES,
)
