"""
setup.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

from simlib.version import __version__

import numpy as np
from setuptools import setup


# Read in requirements.txt
# TODO get rid of requirements.txt in favor of install.sh for travis-ci
requirements = np.loadtxt('requirements.txt', dtype='str').tolist()

# Setup
setup(
    name='simlib',
    version=__version__,
    author='C. Lockhart',
    author_email='chris@lockhartlab.org',
    description='A toolkit for molecular dynamics simulations',
    long_description='A toolkit for molecular dynamics simulations',
    long_description_content_type='text/x-rst',
    url="https://www.lockhartlab.org",
    packages=[
        'simlib',
        'simlib.analysis',
        'simlib.geometry',
        'simlib.io',
        'simlib.misc',
    ],
    install_requires=requirements,
    include_package_data=True,
    zip_safe=True
)
