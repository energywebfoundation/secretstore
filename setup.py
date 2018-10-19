#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup
)

extras_require = {
    "dev": [
        "bumpversion",
        "setuptools>=36.2.0",
        "wheel",
        "Sphinx",
        "sphinx-rtd-theme "
    ]
}

setup(
    name="secretstore",
    version="0.0.1rc1",
    author="Adam Nagy",
    author_email="adam.nagy@energyweb.org",
    description="Python package for Parity's Secret Store API calls and sessions.",
    long_description_markdown_filename="README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/energywebfoundation/secretstore-py",
    project_urls={
        "Documentation": "https://github.com/energywebfoundation/secretstore-py"
    },
    python_requires='>=3.5.3,<4',
    extras_require=extras_require,
    include_package_data=True,
    install_requires=[
        "web3>=4.0.0"
        "requests>=2.16.0,<3.0.0",
    ],
    license="MIT",
    zip_safe=False,
    keywords='secretstore secret store parity api energyweb ewf',
    packages=["secretstore",],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)