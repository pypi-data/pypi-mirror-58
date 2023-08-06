# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cleantoots']

package_data = \
{'': ['*']}

install_requires = \
['Mastodon.py>=1.5.0,<2.0.0', 'click>=7.0,<8.0', 'pendulum>=2.0.5,<3.0.0']

entry_points = \
{'console_scripts': ['cleantoots = cleantoots.main:cli']}

setup_kwargs = {
    'name': 'cleantoots',
    'version': '0.2.3',
    'description': 'Cleanup your toot history.',
    'long_description': '# Cleantoots\n[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2FCrocmagnon%2Fcleantoots%2Fbadge&style=flat)](https://actions-badge.atrox.dev/Crocmagnon/cleantoots/goto)\n\nThe idea of cleantoots is highly inspired by [magnusnissel/cleantweets](https://github.com/magnusnissel/cleantweets).\n\n## Initial config\n\nOnly once\n\n```bash\npython -m pip install cleantoots\ncleantoots setup-config  # See the following section for config options\ncleantoots login\n```\n\n## Config options\n\n```ini\n# Any key in this section will serve as a default for other sections\n[DEFAULT]\n\n# Toots that have at least this number of boosts won\'t be deleted.\nboost_limit = 5\n\n# Toots that have at least this number of favorites won\'t be deleted.\nfavorite_limit = 5\n\n# Toots that are more recent than this number of days won\'t be deleted.\ndays_count = 30\n\n# The timezone to use for dates comparisons.\ntimezone = Europe/Paris\n\n# Each section represents an account.\n[Fosstodon]\n# Your Mastodon server URL.\napi_base_url = https://fosstodon.org\n\n# These files are used to store app information obtained when running `login`.\n# The files must be different between accounts. Two different files are required per account.\napp_secret_file = fosstodon_app.secret\nuser_secret_file = fosstodon_user.secret\n\n# IDs of toots you want to protect (never delete).\n# You can find the toot ID in the URL when viewing a toot.\nprotected_toots = 103362008817616000\n    103361883565013391\n    103363106195441418\n\n# Another account\n[Mastodon.social]\napi_base_url = https://mastodon.social\napp_secret_file = mastodonsocial_app.secret\nuser_secret_file = mastodonsocial_user.secret\n\n# Overriding some defaults\nboost_limit = 10\nfavorite_limit = 30\ndays_count = 7\n```\n\n## Run\n\nSee `cleantoots config` for the current config.\n\n```bash\ncleantoots clean  # Defaults to a dry run. Does NOT delete.\ncleantoots clean --delete  # Delete without prompt.\n```\n\n## Tested environments\nCleantoots test suite runs on Python 3.6, 3.7 and 3.8\non latest versions of macOS, Windows and Ubuntu as GitHub Actions understands it. See\n(the docs)[https://help.github.com/en/actions/automating-your-workflow-with-github-actions/workflow-syntax-for-github-actions#jobsjob_idruns-on]\nfor more information on what "latest" means".\n',
    'author': 'Gabriel Augendre',
    'author_email': 'gabriel@augendre.info',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Crocmagnon/cleantoots/tree/master',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
