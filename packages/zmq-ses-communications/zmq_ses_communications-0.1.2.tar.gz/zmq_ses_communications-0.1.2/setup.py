# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zmq_ses_communications',
 'zmq_ses_communications.client',
 'zmq_ses_communications.client.msgs',
 'zmq_ses_communications.server']

package_data = \
{'': ['*'], 'zmq_ses_communications': ['tests/*']}

install_requires = \
['protobuf>=3.11.1,<4.0.0',
 'psutil>=5.6.7,<6.0.0',
 'pytest>=5.3.2,<6.0.0',
 'pyzmq>=18.1.1,<19.0.0']

setup_kwargs = {
    'name': 'zmq-ses-communications',
    'version': '0.1.2',
    'description': 'communication backend for creating a distributed system for integrating devices in a smart factory',
    'long_description': None,
    'author': 'Vinu Home',
    'author_email': 'vinuvnair@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
