# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sql2json']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.3.12,<2.0.0', 'click>=7.0,<8.0', 'fire>=0.2.1,<0.3.0']

setup_kwargs = {
    'name': 'sql2json',
    'version': '0.1.3',
    'description': 'SQL query to JSON',
    'long_description': None,
    'author': 'Francisco Perez',
    'author_email': 'fsistemas@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fsistemas/sql2json',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
