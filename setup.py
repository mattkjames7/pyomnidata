import setuptools
from setuptools.command.install import install
import os
from getversion import getversion

with open("README.md", "r") as fh:
    long_description = fh.read()

version = getversion()

setuptools.setup(
    name="pyomnidata",
    version=version,
    author="Matthew Knight James",
    author_email="mattkjames7@gmail.com",
    description="Python tool for downloading, converting and reading OMNI solar wind data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattkjames7/pyomnidata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
    ],
    install_requires=[
		'numpy',
		'matplotlib',
		'RecarrayTools',
		'PyFileIO',
		'DateTimeTools>=1.0.1',
        'requests'
	],
)



