# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['packages']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'packages',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Chris Hunt',
    'author_email': 'chrahunt@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
