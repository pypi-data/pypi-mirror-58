# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastrl']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fastrl',
    'version': '0.0.0',
    'description': '',
    'long_description': None,
    'author': 'Aditya Gudimella',
    'author_email': 'aditya.gudimella@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
