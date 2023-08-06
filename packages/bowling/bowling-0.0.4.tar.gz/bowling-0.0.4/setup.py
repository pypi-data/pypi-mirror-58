# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bowling']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'bowling',
    'version': '0.0.4',
    'description': '',
    'long_description': None,
    'author': 'Satoshi Yagi',
    'author_email': 'satoshi.yagi@yahoo.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
