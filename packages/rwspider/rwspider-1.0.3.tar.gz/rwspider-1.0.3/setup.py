#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
        name='rwspider',
        version='1.0.3',
        author='Rui Ma',
        author_email='ruima_06@outlook.com',
        url='https://ruiwencloud.xyz',
        description=u'python 爬虫扩展功能\nfake-ua: ',
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=['rwspider'],
        install_requires=["requests"],
        entry_points={
            'console_scripts': [
                'rw-ua=rwspider:print_ua'
            ]
        }
)
