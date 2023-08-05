# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['rabbit_rpc_py']

package_data = \
{'': ['*']}

install_requires = \
['pika>=1.1,<2.0', 'pretty-logging>=1.0,<2.0']

setup_kwargs = {
    'name': 'rabbit-rpc-py',
    'version': '0.4.0',
    'description': 'amqp rabbit rpc',
    'long_description': None,
    'author': 'Arvin',
    'author_email': 'arvintian8@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
