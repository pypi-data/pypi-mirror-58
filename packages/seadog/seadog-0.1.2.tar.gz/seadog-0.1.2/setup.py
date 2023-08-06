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
    'version': '0.1.2',
    'description': 'Statistical data visualization from the command line',
    'long_description': '# seadog\n\nSeadog helps you generate statistical data visualizations directly from the command line. \n\nIt aims to allow quick analyses of data, and while it is essentially a wrapper for [matplotlib](https://github.com/matplotlib/matplotlib) and [seaborn](https://github.com/mwaskom/seaborn), it does not intend to cover all options and capabilities. \n\nThe word seadog may be slang for either a veteran sailor or seals. \n\nSupports Python 3.7+.\n\n## Installation\n\nUsing `pip` to install `seadog`:\n\n```bash\npip install --user seadog\n```\n\n## Quick start\n\nThis section will be updated once `seadog` provides some functionality. Features will be added as I need them.\n\n## Todo\n\n- Data description\n- Data sample (n)\n- Data correlation\n- Data NaN detection (graph in terminal)\n- Data NaN removal\n- Bar chart (and horizontal option)\n- Histogram\n- Dist plot with KDE\n- Logarithmic scales for x and y\n- Axes labels\n- Scatter plots\n- Pie charts?\n\n',
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
