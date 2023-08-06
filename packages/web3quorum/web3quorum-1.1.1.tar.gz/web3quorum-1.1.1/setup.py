# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['web3quorum']

package_data = \
{'': ['*']}

install_requires = \
['web3>=5.4,<6.0']

setup_kwargs = {
    'name': 'web3quorum',
    'version': '1.1.1',
    'description': 'A library to interact with Quorum API',
    'long_description': None,
    'author': 'Chainstack',
    'author_email': 'dev@chainstack.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
