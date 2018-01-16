from distutils.core import setup
from setuptools import find_packages

setup(
    name = 'mangaScraper',
    version = '0.1dev',
    author ='featTheB',
    packages = find_packages(),
    long_description=open('README.md').read(),
)