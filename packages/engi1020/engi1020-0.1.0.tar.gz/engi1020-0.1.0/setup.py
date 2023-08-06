# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="engi1020",
    version="0.1.0",
    description="Software library for Engineering 1020: Introduction to Programming at Memorial University.",
    license="MIT",
    author="Jonathan Anderson",
    packages=find_packages(),
    install_requires=['matplotlib'],
    long_description=open("README.rst").read(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ]
)
