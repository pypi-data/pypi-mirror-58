# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flake8_click']

package_data = \
{'': ['*']}

install_requires = \
['attrs', 'click>=7.0,<8.0', 'flake8>=3.7,<4.0', 'libcst>=0.2.4,<0.3.0']

entry_points = \
{'flake8.extension': ['r2c-click-best-practices = '
                      'flake8_click.flake8_click:ClickPracticeCheckers']}

setup_kwargs = {
    'name': 'flake8-click',
    'version': '0.2.5',
    'description': '',
    'long_description': None,
    'author': 'R2C',
    'author_email': 'hello@returntocorp.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://r2c.dev',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
