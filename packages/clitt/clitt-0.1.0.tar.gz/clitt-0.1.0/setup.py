# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clitt']

package_data = \
{'': ['*'], 'clitt': ['config/*']}

install_requires = \
['colorama>=0.4.1,<0.5.0', 'tweepy>=3.8,<4.0']

setup_kwargs = {
    'name': 'clitt',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Joao Vitor Maia',
    'author_email': 'joaocampo2@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
