# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['woops']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'woops',
    'version': '0.1.0',
    'description': 'Handle and manage Python errors with ease',
    'long_description': '# Woops!\n\nHandle and manage Python errors with ease.\n',
    'author': 'Sébastien Eustace',
    'author_email': 'sebastien@eustace.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sdispater/woops',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
