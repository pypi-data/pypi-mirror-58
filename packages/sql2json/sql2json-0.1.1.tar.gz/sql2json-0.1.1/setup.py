# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sql2json']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.3.12,<2.0.0', 'click>=7.0,<8.0']

setup_kwargs = {
    'name': 'sql2json',
    'version': '0.1.1',
    'description': 'SQL query to JSON',
    'long_description': None,
    'author': 'Francisco P\xc3\xa9rez',
    'author_email': 'fsistemas@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
