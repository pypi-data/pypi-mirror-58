#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='tikzify',
    version='0.6',
    description=(
        'A set of utilities for programmatically generating TikZ code'),
    author='Neil Girdhar',
    author_email='mistersheik@gmail.com',
    project_urls={
        "Bug Tracker": "https://github.com/NeilGirdhar/tikzify/issues",
        "Source Code": "https://github.com/NeilGirdhar/tikzify",
    },
    download_url="https://pypi.python.org/pypi/tikzify",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords=['testing', 'logging', 'example'],
    python_requires='>=3.7',
    setup_requires=[],
    tests_require=[],
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
)
