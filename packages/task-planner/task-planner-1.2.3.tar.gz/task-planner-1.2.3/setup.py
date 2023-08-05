#!/usr/bin/env python3

# Copyright 2019 Yannick Kirschen. All rights reserved.
# Use of this source code is governed by the GNU-GPL
# license that can be found in the LICENSE file.


from setuptools import setup, find_packages

from task import __version__


def long_description():
    with open('README.md') as f:
        return f.read()


setup(
    name='task-planner',
    version=__version__.__version__,
    license='MIT',
    url='https://github.com/yannickkirschen/task',
    author='Yannick Kirschen',
    author_email='github.yannickkirschen@protonmail.com',
    description='A task planner for the terminal.',
    long_description_content_type='text/markdown',
    long_description=long_description(),
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ]
)
