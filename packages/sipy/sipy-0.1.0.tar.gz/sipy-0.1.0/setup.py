# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sipy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'sipy',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Samuel Broster',
    'author_email': 'sbroster@undo.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
