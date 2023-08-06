# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['elasticedge',
 'elasticedge.api',
 'elasticedge.auth',
 'elasticedge.console',
 'elasticedge.console.commands']

package_data = \
{'': ['*']}

install_requires = \
['cleo>=0.7.6,<0.8.0', 'pyyaml>=5.2,<6.0', 'requests>=2.22.0,<3.0.0']

entry_points = \
{'console_scripts': ['elasticedge = elasticedge.console:main']}

setup_kwargs = {
    'name': 'elasticedge',
    'version': '0.4.0',
    'description': '',
    'long_description': None,
    'author': 'Marco Acierno',
    'author_email': 'marcoaciernoemail@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
