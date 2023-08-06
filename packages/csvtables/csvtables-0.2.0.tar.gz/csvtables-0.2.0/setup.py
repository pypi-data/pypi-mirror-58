# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['csvtables']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['csvtables = csvtables.csvtables:cli']}

setup_kwargs = {
    'name': 'csvtables',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Demetris Stavrou',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
