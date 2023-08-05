# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asyncnostic']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'asyncnostic',
    'version': '0.1.1',
    'description': 'simple way of using pytest with async unit tests',
    'long_description': None,
    'author': 'Derek Yu',
    'author_email': 'derek-nis@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
