# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stepy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'stepy',
    'version': '0.2.1',
    'description': '',
    'long_description': None,
    'author': 'Shparki',
    'author_email': 'murrmat@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
