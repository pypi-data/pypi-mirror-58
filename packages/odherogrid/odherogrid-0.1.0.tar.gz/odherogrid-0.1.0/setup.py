# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['odherogrid']

package_data = \
{'': ['*'], 'odherogrid': ['scripts/*']}

install_requires = \
['click>=7.0,<8.0', 'pyyaml>=5.2,<6.0', 'requests>=2.22.0,<3.0.0']

entry_points = \
{'console_scripts': ['odhg = odherogrid.scripts.cli:run']}

setup_kwargs = {
    'name': 'odherogrid',
    'version': '0.1.0',
    'description': 'Dota 2 hero grid generator using OpenDotaAPI stats',
    'long_description': None,
    'author': 'PederHA',
    'author_email': 'peder.andresen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/PederHA/odherogrid',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
