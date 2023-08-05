# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['lhub_extractors']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<7.1',
 'dataclasses-json',
 'docstring-parser>=0.1,<0.2',
 'wheel>=0.32.3,<0.33.0']

setup_kwargs = {
    'name': 'lhub-extractors',
    'version': '0.3.8',
    'description': 'LogicHub Feature Extractors',
    'long_description': None,
    'author': 'Bernie Liu',
    'author_email': 'bernie@logichub.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
