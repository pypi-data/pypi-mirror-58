# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyliter', 'pyliter.color', 'pyliter.resources']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'pyglet>=1.4.8,<2.0.0', 'pyyaml>=5.2,<6.0']

entry_points = \
{'console_scripts': ['pyliter = pyliter.__main__:pyliter_cli']}

setup_kwargs = {
    'name': 'pyliter',
    'version': '1.1.1',
    'description': '',
    'long_description': None,
    'author': 'jnyjny',
    'author_email': 'erik.oshaughnessy@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
