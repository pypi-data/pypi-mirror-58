#!/usr/bin/env python
from setuptools import setup, find_packages
setup(
        name="as3",
        version="1.0",
        packages=find_packages(),
        install_requires=['requests>=2.0'],
        author="Pete White",
        author_email="pwhite@f5.com",
        description="This is a Python module to easily use the F5 AS3 deployment method",
        license="PSF",
        url="https://pypi.python.org/pypi?:action=display&name=as3&version=1.0",
)
