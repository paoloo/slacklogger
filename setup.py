#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='slacklogger',
    description='logger/notifier module for slack',
    url='https://github.com/paoloo/slacklogger',
    author='Paolo Oliveira',
    author_email='paolo@fisica.ufc.br',
    license='BSD License',
    packages=find_packages(),
    version='0.1.5',
    install_requires=['pyOpenSSL>=16.0.0', 'websocket-client>=0.37.0'],
    entry_points={
        'console_scripts': [
            'slacklogger = slacklogger.__main__:main'
        ]
    },
)
