# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['smartpost']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.22,<3.0']

setup_kwargs = {
    'name': 'smartpost',
    'version': '0.1.0',
    'description': 'Python library to interact with Itella Smartpost API',
    'long_description': None,
    'author': 'Rao Zvorovski',
    'author_email': 'rao.zvorovski@codeduf.eu',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
