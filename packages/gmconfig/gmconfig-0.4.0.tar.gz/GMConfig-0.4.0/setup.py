# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gmconfig', 'gmconfig.loaders', 'gmconfig.utils']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=5.1,<6.0', 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['lint = black gmconfig',
                     'poetry = poetry.console:main',
                     'test = python -m unittest discover tests -p test_*.py',
                     'test-types = mypy gmconfig']}

setup_kwargs = {
    'name': 'gmconfig',
    'version': '0.4.0',
    'description': 'My lazy mans config loading and exporting module',
    'long_description': '# GMConfig\n\n[![PyPI version](https://badge.fury.io/py/gmconfig.svg)](https://badge.fury.io/py/gmconfig)\n\nMy lazy mans config loading and exporting module\n\n## Build\n\n```bash\npoetry build\n```\n',
    'author': 'GeekMasher',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/GeekMasher/GMConfig',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
