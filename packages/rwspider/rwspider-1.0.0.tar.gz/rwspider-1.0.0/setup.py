#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
        name='rwspider',
        version='1.0.0',
        author='Rui Ma',
        author_email='ruima_06@outlook.com',
        url='https://ruiwencloud.xyz',
        description=u'python 爬虫扩展功能\nfake-ua: ',
        packages=['rwspider'],
        install_requires=["requests"],
        entry_points={
            'console_scripts': [
                'rw-ua=rwspider:print_ua'
            ]
        }
)
