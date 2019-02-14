#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages

setup(
    name="sortphotos",
    version="1.2",
    description="Organizes photos and videos into folders using date/time information ",
    author="OpenCo Inc",
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",
    entry_points={"console_scripts": ["sortphotos = src.sortphotos:main"]},
)
