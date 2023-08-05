"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='polyutils',
    version='0.71',
    packages=['polyutils'],
    url='https://github.com/gstfrr/polyutils',
    download_url='https://github.com/gstfrr/polyutils/archive/v0.71.tar.gz',
    license='',
    author='Augusto Ferreira',
    author_email='gstfrr@gmail.com',
    description='',
    install_requires=['numpy']
)
