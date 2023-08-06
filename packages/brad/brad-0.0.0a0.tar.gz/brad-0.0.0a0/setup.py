# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['brad']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.18.0,<2.0.0']

setup_kwargs = {
    'name': 'brad',
    'version': '0.0.0a0',
    'description': 'Brad is a Python package for Bootstrap, permutation tests and other resampling functions.',
    'long_description': None,
    'author': 'tcbegley',
    'author_email': 'tomcbegley@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
