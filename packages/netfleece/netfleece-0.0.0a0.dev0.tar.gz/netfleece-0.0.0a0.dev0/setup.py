#!/usr/bin/env python3
"""netfleece placeholder"""

import setuptools

def main():
    kwargs = {
        'name': 'netfleece',
        'version': '0.0.0a0.dev0',
        'author': 'nago',
        'author_email': 'nago@malie.io',
        'description': "Python 3.7+ Microsoft .NET Remoting Binary Format (MS-NRBF) to JSON parser",
        'url': "https://gitlab.com/malie-library/netfleece",
        'packages': setuptools.find_packages(),
        'classifiers': [
            "Development Status :: 1 - Planning",
            "License :: OSI Approved :: MIT License",
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
