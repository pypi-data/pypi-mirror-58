# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['cognite',
 'cognite.seismic',
 'cognite.seismic._api',
 'cognite.seismic.data_classes',
 'cognite.seismic.protos']

package_data = \
{'': ['*']}

install_requires = \
['grpcio-tools>=1.24,<2.0', 'numpy>=1.17,<2.0']

setup_kwargs = {
    'name': 'cognite-seismic-sdk',
    'version': '0.1.5',
    'description': '',
    'long_description': None,
    'author': 'cognite',
    'author_email': 'support@cognite.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
