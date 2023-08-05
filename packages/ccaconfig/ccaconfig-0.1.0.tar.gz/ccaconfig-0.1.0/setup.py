# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ccaconfig']

package_data = \
{'': ['*']}

install_requires = \
['ccalogging>=0.3.3,<0.4.0', 'pytest>=5.3.2,<6.0.0', 'pyyaml>=5.2,<6.0']

setup_kwargs = {
    'name': 'ccaconfig',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'ccdale',
    'author_email': 'chris.allison@hivehome.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
