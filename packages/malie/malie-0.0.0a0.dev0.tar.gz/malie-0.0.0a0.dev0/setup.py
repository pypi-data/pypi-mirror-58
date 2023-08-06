#!/usr/bin/env python3
"""malie placeholder"""

import setuptools

def main():
    kwargs = {
        'name': 'malie',
        'version': '0.0.0a0.dev0',
        'author': 'nago',
        'author_email': 'nago@malie.io',
        'description': "malie is a Pokemon TCG Database toolset",
        'url': "https://gitlab.com/malie-library/malie",
        'packages': setuptools.find_packages(),
        'classifiers': [
            "Development Status :: 1 - Planning",
            "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
            "Natural Language :: English",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 3",
        ]
    }
    kwargs['long_description'] = "Bless this mess"

    setuptools.setup(**kwargs)

if __name__ == '__main__':
    main()
