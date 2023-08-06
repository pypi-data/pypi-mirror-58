# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['seadog']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0']

setup_kwargs = {
    'name': 'seadog',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'leonhfr',
    'author_email': 'hello@leonh.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
