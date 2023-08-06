#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='rusmarkup',
    version='0.1.0',
    author='Maksim Ryndin',
    author_email='maksim.ryndin@gmail.com',
    url='https://github.com/maksimryndin/rusmarkup',
    description='Простой язык разметки для русского языка',

    license='MIT',
    packages=['rusmarkup'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
