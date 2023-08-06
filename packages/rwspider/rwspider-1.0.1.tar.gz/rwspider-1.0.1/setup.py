#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
        name='rwspider',
        version='1.0.1',
        author='Rui Ma',
        author_email='ruima_06@outlook.com',
        url='https://ruiwencloud.xyz',
        description=u'python 爬虫扩展功能\nfake-ua: ',
        long_description="README.md",
        long_description_content_type="text/markdown",
        packages=['rwspider'],
        install_requires=["requests"],
        entry_points={
            'console_scripts': [
                'rw-ua=rwspider:print_ua'
            ]
        }
)
