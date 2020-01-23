# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.0.1',
    description='NCL Generator API has a main purpose facilitate NCL implementation using a Python language.',
    long_description=readme,
    author='Michael Alves Bittencourt de Mello',
    author_email='mchl.bittencourt@gmail.com',
    url='https://github.com/MichaelBittencourt/NCL-Generator-API',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

