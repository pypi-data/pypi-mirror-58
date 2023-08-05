# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['pytest-sql-bigquery', 'pytest-sql-bigquery.integrations']

package_data = \
{'': ['*']}

install_requires = \
['google-cloud-bigquery', 'pytest', 'sqlparse==0.2.4', 'tabulate']

setup_kwargs = {
    'name': 'pytest-sql-bigquery',
    'version': '0.0.1',
    'description': 'Pytest plugin for testing sql on BigQuery engine',
    'long_description': None,
    'author': 'TKNGUE',
    'author_email': 'takegue@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
