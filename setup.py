#!/usr/bin/env python3
# Copyright 2019 Mycroft AI Inc.
# Modified 2021 Seeed Studio STU, Dmitry Maslov

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os import path
from setuptools import setup, find_packages
from precise_runner import __version__

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='precise-runner-simple',
    version=__version__,
    packages=[
        'precise_runner',
        'precise_runner.scripts'
    ],
    include_package_data=True,

    author='Matthew Scholefield',
    author_email='matthew.scholefield@mycroft.ai',
    description='Simplified Wrapper to use Mycroft Precise Wake Word Listener',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='wakeword keyword wake word listener sound',
    url='http://github.com/MycroftAI/mycroft-precise',

    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',                
    ],
    entry_points={
        'console_scripts': [
            'mycroft-precise=precise_runner.scripts.mycroft_precise:main',
        ]
    },
    install_requires=requirements
)
