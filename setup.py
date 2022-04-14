#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='capt-listen',
    version='1.0.0',
    description='Listen to the wavefiles',
    author='',
    author_email='bencherif.research@gmail.com',
    # REPLACE WITH YOUR OWN GITHUB PROJECT LINK
    url='https://github.com/mbencherif/capt-listen',
    install_requires=['streamlit'],
    packages=find_packages(),
)

