# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['vbml',
 'vbml.patcher',
 'vbml.patcher.loader',
 'vbml.patcher.pattern',
 'vbml.patcher.standart']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'vbml',
    'version': '0.5.9',
    'description': 'Way to check',
    'long_description': None,
    'author': 'timoniq',
    'author_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
