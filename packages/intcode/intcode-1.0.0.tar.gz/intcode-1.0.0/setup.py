# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['intcode',
 'intcode.handlers',
 'intcode.handlers.io',
 'intcode.interfaces',
 'intcode.interpreter',
 'intcode.ops']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'intcode',
    'version': '1.0.0',
    'description': 'Intcode interpreter for Advent of Code 2019',
    'long_description': None,
    'author': 'Javier Luna molina',
    'author_email': 'javierlunamolina@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
