# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['youarehere']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.10.43,<2.0.0', 'requests>=2.22.0,<3.0.0']

setup_kwargs = {
    'name': 'youarehere',
    'version': '0.1.0',
    'description': 'Route53 DNS utility',
    'long_description': None,
    'author': 'Jordan Matelsky',
    'author_email': 'j6k4m8@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
