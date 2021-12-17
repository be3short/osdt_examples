import os

from setuptools import setup
import sys
# dev: python .\setup.py develop
# regular python .\setup.py install
# uninstall: python setup.py develop --uninstall

setup(
    name="test_lib",
    version='1.0',
    long_description=__doc__,
    packages=['test_lib'],
    include_package_data=True,
    zip_safe=False,
)
