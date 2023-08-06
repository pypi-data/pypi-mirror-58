# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pystarter']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pystarter',
    'version': '1.2.0',
    'description': 'A program to help you start python and git projects with file creations',
    'long_description': None,
    'author': 'Rafael Cenzano',
    'author_email': 'savagecoder77@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
