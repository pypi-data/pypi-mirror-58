"""
setup.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

from izzy.version import __version__

import numpy as np
from setuptools import setup


# Read in requirements.txt
requirements = np.loadtxt('requirements.txt', dtype='str').tolist()

# Setup
setup(
    name='izzy',
    version=__version__,
    author='C. Lockhart',
    author_email='chris@lockhartlab.org',
    description='A toolkit for executing and analyzing machine learning classification',
    long_description='A toolkit for executing and analyzing machine learning classification',
    long_description_content_type='text/x-rst',
    url="https://www.lockhartlab.org",
    packages=[
        'izzy',
        'izzy.datasets',
        'izzy.eda',
        'izzy.features',
        'izzy.io',
        'izzy.misc',
        'izzy.classification',
        'izzy.regression',
        'izzy.tests',
        'izzy.tests.classification',
        'izzy.viz',
    ],
    install_requires=requirements,
    include_package_data=True,
    zip_safe=True
)
