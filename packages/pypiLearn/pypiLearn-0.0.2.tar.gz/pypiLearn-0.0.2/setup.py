#!python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages
from pypiLearn import test

with open("README.md", "r") as fh:
    long_description = fh.read()

print(test.Test.__version__)

setup(
    name="pypiLearn",
    version=test.Test.__version__,
    author="song",
    author_email="soany777@163.com",
    description="a test project for learning how to use pypi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/xxx/test",
    packages=find_packages(),
    install_requires=[
        "numpy"
        ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
)

