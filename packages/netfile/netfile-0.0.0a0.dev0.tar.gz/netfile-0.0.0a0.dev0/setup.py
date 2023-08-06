#!/usr/bin/env python3
"""netfile placeholder"""

import setuptools

def main():
    kwargs = {
        'name': 'netfile',
        'version': '0.0.0a0.dev0',
        'author': 'nago',
        'author_email': 'nago@malie.io',
        'description': "netfile is a minimalistic .NET executable binary parser",
        'url': "https://gitlab.com/malie-library/netfile",
        'packages': setuptools.find_packages(),
        'classifiers': [
            "Development Status :: 1 - Planning",
            "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Topic :: Software Development :: Disassemblers",
        ],
    }
    kwargs['long_description'] = "Bless this mess"

    setuptools.setup(**kwargs)

if __name__ == '__main__':
    main()
