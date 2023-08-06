#!/usr/bin/env python
"""netfile installation script."""

import setuptools
#from distutils.core import setup

def main():
    """netfile installation wrapper"""
    kwargs = {
        'name': 'netfile',
        'version': '0.1.3',
        'author': 'nago',
        'author_email': 'nago@malie.io',
        'description': "netfile is a minimalistic .NET executable binary parser",
        'url': "https://gitlab.com/malie-library/netfile",
        'packages': setuptools.find_packages(),
        'classifiers': [
            "Development Status :: 2 - Pre-Alpha",
            "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
            "Natural Language :: English",
            "Operating System :: OS Independent", # Uh, I hope, haha
            "Programming Language :: Python :: 3",
            "Topic :: Software Development :: Disassemblers",
        ],
        'install_requires': [
            'pefile',
        ],
    }

    with open("README.md", "r") as fh:
        kwargs['long_description'] = fh.read()
    kwargs['long_description_content_type'] = 'text/markdown'

    setuptools.setup(**kwargs)

if __name__ == '__main__':
    main()
