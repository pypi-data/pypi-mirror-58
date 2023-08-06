# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lucidic']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'lucidic',
    'version': '0.1.0',
    'description': 'Lucidic is a Python dictionary utility designed to simplify dictionary operations and comparisons',
    'long_description': '# Lucid Python Dictionary Utility Package Changelog\n',
    'author': 'Rich Nason',
    'author_email': 'rnason@cloudmage.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/TheCloudMage/PyPkgs-Lucidic',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
