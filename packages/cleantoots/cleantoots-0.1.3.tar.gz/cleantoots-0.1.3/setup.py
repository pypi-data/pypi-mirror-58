# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cleantoots']

package_data = \
{'': ['*']}

install_requires = \
['Mastodon.py>=1.5.0,<2.0.0', 'click>=7.0,<8.0', 'pendulum>=2.0.5,<3.0.0']

entry_points = \
{'console_scripts': ['cleantoots = cleantoots.main']}

setup_kwargs = {
    'name': 'cleantoots',
    'version': '0.1.3',
    'description': 'Cleanup your toot history.',
    'long_description': '# Cleantoots\n\n## Initial config\n\nOnly once\n\n```bash\npipenv install\npipenv run python main.py create-app\npipenv run python main.py get-credentials\n```\n\n## Run\n\nSee `config.py` for options.\n\n```bash\npipenv run python main.py clean-toots  # Defaults to a dry run. Does NOT delete.\npipenv run python main.py clean-toots --delete  # Delete without prompt.\n```\n',
    'author': 'Gabriel Augendre',
    'author_email': 'gabriel@augendre.info',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Crocmagnon/cleantoots/tree/master',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
