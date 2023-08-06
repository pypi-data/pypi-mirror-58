import os

from setuptools import setup, find_packages

VERSION         = '2.0.1'
DESCRIPTION     = 'Wrapper for TrivoreID SDK'
AUTHOR          = 'Anastasia Gromova'
AUTHOR_EMAIL    = 'id-client-sdk@trivore.com'
LICENSE         = 'Apache 2.0'

def check_dependencies():

    install_requires = []

    # try:
    #     import unittest
    # except ImportError:
    #     install_requires.append('unittest')

    try:
        import requests
    except ImportError:
        install_requires.append('requests')

    # try:
    #     import mock
    # except ImportError:
    #     install_requires.append('mock')

    return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()

    setup(name='trivoreid',
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=AUTHOR,
        maintainer_email=AUTHOR_EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        version=VERSION,
        install_requires=install_requires,
        packages=find_packages())
