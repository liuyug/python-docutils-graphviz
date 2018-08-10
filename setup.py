#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from setuptools import setup


with open('README.rst') as f:
    long_description = f.read()


setup(
    name='python-docutils-graphviz',
    version='1.0.1',
    author='Yugang LIU',
    author_email='liuyug@gmail.com',
    url='https://github.com/liuyug/python-docutils-graphviz.git',
    license='MIT',
    description='Graphviz extension for docutils',
    long_description=long_description,
    py_modules=['docutils_graphviz'],
    install_requires=['docutils', 'graphviz'],
)
