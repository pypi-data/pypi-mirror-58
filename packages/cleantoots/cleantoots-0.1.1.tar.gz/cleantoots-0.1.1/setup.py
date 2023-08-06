# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cleantoots']

package_data = \
{'': ['*']}

install_requires = \
['Mastodon.py>=1.5.0,<2.0.0', 'click>=7.0,<8.0', 'pendulum>=2.0.5,<3.0.0']

setup_kwargs = {
    'name': 'cleantoots',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Gabriel Augendre',
    'author_email': 'gabriel@augendre.info',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
