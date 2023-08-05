
from setuptools import setup
from setuptools import find_packages

import re

filepath = 'batchcrop/__init__.py'
__version__ = re.findall(r'__version__ = \'(.*)\'', open(filepath).read())[0]

setup(
    name = 'batchcrop',
    version = __version__,
    license = 'MIT',
    author = 'Tom de Geus',
    author_email = 'tom@geus.me',
    description = 'Crop a batch of images.',
    long_description = 'Crop a batch of images.',
    keywords = 'convert',
    url = 'https://github.com/tdegeus/batchcrop',
    packages = find_packages(),
    install_requires = ['docopt>=0.6.2'],
    entry_points = {
        'console_scripts': ['batchcrop = batchcrop.cli.batchcrop:main']})
