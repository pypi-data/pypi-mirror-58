#!/usr/bin/env python
# coding=utf-8

from setuptools import setup,find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="lunuan", # Replace with your own username
    version="0.1.3",
    author='huaxing',
    author_email='huaxing@lunuan.com.cn',
    maintainer='huaxing',
    maintainer_email='huaxing@lunuan.com.cn',
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" ",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
