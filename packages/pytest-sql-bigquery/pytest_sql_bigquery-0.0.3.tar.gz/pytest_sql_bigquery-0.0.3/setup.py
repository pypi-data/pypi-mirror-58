# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['pytest_sql_bigquery', 'pytest_sql_bigquery.integrations']

package_data = \
{'': ['*']}

install_requires = \
['google-cloud-bigquery', 'pytest', 'sqlparse==0.2.4', 'tabulate']

setup_kwargs = {
    'name': 'pytest-sql-bigquery',
    'version': '0.0.3',
    'description': 'Yet another SQL-testing framework for BigQuery provided by pytest plugin ',
    'long_description': '\n# Pytest plugin for Bigquery SQL\n\npytest-sql-bigquery is pytest-plugin which provides a sql-unitest-framework for BigQuery.\nThis plugin adopts an end-to-end approch that runnning SQL test on SQL engines.\n\n## Yet anthoer approch to tst SQL code\n\nSee following SQL codes:\n\n```sql\nwith dataset as (\n    select 1\n    union all select 2\n)\n, __check_sample as (\n    select \'test\' as label, count(1) as actual, 2 as expected from dataset \n)\n\nselect * from dataset\n```\n\nThis code is minimal example including test case.\n`__check_sample` is a test case which makes sure the `dataset` view has just 2 record.\n\n\nOur idea is very simple: "Verify SQL code by SQL-self."\n\nThis plugin generate SQL test codes from SQL and executed them on SQL-engine such as BigQuery.\n\nThe advantages of this approch are \n\n- SQL codes owns specification itself\n- Provide portability of logic and its test codes. \n- Free to hard-mocking database system\n\n\n# Get Started\n\n## Requirements\n\n- Python >= 3.7\n- sqlparse\n- google-cloud-bigquery (For BigQuery integration)\n\n- BigQuery (Google Cloud Project)\n\n## Install\n\n```\npip install pytest-bigquery-sql\n```\n\nThen, set up `confidist.py` for pytest settings.\n\n```python\nimport pytest\n\nfrom pytest_sql_bigquery.integrations.pytest import SQLReaderForChecking\n\nclass ChainPytestFile(pytest.File):\n\n    def __init__(self, path, parent, chains, **kwargs):\n        super().__init__(path, parent, **kwargs)\n        self.chains = chains\n\n    def collect(self):\n        for interpreter in self.chains:\n            yield from interpreter.collect()\n\ndef pytest_collect_file(parent, path):\n    if path.ext == ".sql":\n        return ChainPytestFile(\n            path, parent,\n            [\n                SQLReaderForChecking(path, parent),\n            ])\n```\n\nRun test for `examples/sql` directory\n\n```\npytest run -vv examples/sql \n```\n',
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
