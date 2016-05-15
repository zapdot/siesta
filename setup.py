#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version__ = "0.5.2"

setup(
    name='siesta',
    version=__version__,
    description='Zapdot fork of Siesta by Sebastián Castillo Builes',
    author='Michael Carriere',
    author_email='mike@zapdot.com',
    license='GPL',
    keywords='REST RESTful API HTTP web service',
    url="http://scastillo.github.com/siesta/",
    long_description="""
    Siesta is a client library to consume RESTful web services.
    """,
    packages=find_packages(),
    install_requires = ['simplejson'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        ],
    )
