# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rush_cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'colorama>=0.4.3,<0.5.0', 'pyyaml>=5.2,<6.0']

entry_points = \
{'console_scripts': ['rush = rush_cli.cli:entrypoint']}

setup_kwargs = {
    'name': 'rush-cli',
    'version': '0.2.1',
    'description': 'Minimalistic bash task runner',
    'long_description': None,
    'author': 'rednafi',
    'author_email': 'redowan.nafi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
