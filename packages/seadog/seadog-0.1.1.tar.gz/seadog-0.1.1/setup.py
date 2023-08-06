# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['seadog']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'matplotlib>=3.1.2,<4.0.0',
 'numpy>=1.18.0,<2.0.0',
 'pandas>=0.25.3,<0.26.0',
 'seaborn>=0.9.0,<0.10.0',
 'tabulate>=0.8.6,<0.9.0',
 'termplotlib>=0.2.3,<0.3.0']

entry_points = \
{'console_scripts': ['seadog = seadog.cli:cli']}

setup_kwargs = {
    'name': 'seadog',
    'version': '0.1.1',
    'description': 'Statistical data visualization from the command line',
    'long_description': '# Seadog\n\nslang term for a veteran sailor\n\nslang term for seals\n\nrely extensively on seaborn package\n\ntesting\n\nbuild\n\ninstall\n\nquick start\n',
    'author': 'leonhfr',
    'author_email': 'hello@leonh.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/leonhfr/seadog',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
