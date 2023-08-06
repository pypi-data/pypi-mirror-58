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
    'version': '0.1.1',
    'description': 'Dota 2 hero grid generator using OpenDotaAPI stats',
    'long_description': "# ODHeroGrid\n![logo](logo.png)\n\nSmall script that generates a custom Dota 2 Hero Grid layout of heroes sorted \nby winrate in public or professional games, using stats from OpenDota.\n\n# Installation\n```\npip install odherogrid\n```\n\n# Usage\n```\nodhg  [-b, --brackets] BRACKET (default: 7)\n        Which skill bracket to get winrates from.\n            <1, herald, h>                          Herald\n            <2, guardian, g>                        Guardian\n            <3, crusader, c>                        Crusader\n            <4, archon, a>                          Archon\n            <5, legend, l>                          Legend\n            <6, ancient, n>                         Ancient\n            <7, divine, d, immortal, i>             Divine\n            <8, pro, p, official, tournaments>      Pro\n            <0, all, A>                             All\n\n      [-g, --grouping] GROUPING (default: 1)\n        How heroes should be grouped in the grid\n            <1, mainstat, m, stat, stats>           Mainstat\n            <2, attack, a, melee, range>            Attack\n            <3, role, r>                            Role\n            <0, none, n, all, everything>           None\n\n      [-p, --path] PATH\n        Specify absolute path of Dota 2 userdata/cfg directory.\n        (It's usually better to run --setup to configure this path.)\n\n      [-s, --sort] (flag)\n        Sort heroes by winrate in ascending order. (Default: descending).\n\n      [-S, --setup] (flag)\n        Runs first-time setup in order to create a persistent config.\n\n      [-h, --help] (flag)\n        Displays command usage information.\n\n```\n\n# Examples\n\n\n#### Use options stored in config. (Runs first-time setup if no config exists)\n```bash\nodhg\n```\nThe config file will be stored as `~/.odhg/config.yml`\n\nIt is recommended to create a config rather than using command-line options.\n\n\n#\n## Bracket\n\n\n#### Create grid for Herald hero winrates:\n```bash\nodhg --brackets 1\n```\n\n#### Bracket names can also be used:\n```bash\nodhg --brackets herald\n```\n\n#### Shorter:\n```bash\nodhg -b 1\nodhg -b h\n```\n\n#\n#### Create grids for Herald, Divine & Pro winrates:\n```bash\nodhg -b 1 -b 7 -b 8\n```\n#### Alternatively:\n```bash\nodhg -b h -b d -b p\n```\n#\n#### Create grids for all brackets:\n```bash\nodhg -b 0\n```\n\n\n#\n## Grouping\n\n\n#### Create grids for Divine hero winrates, grouped by Hero roles (Carry/Support/Flex):\n```bash\nodhg -g 3 -b 7\n```\n\n#### Name of grouping method can also be used:\n```bash\nodhg -g role -b 7\n```\n\n\n#\n## Path\n\n\n#### Specify a specific Steam user CFG directory:\n```bash\nodhg --path C:\\Program Files (x86)\\Steam\\userdata\\420666\\570\\remote\\cfg\n```\n\n\n# Screenshots\n\n![Divine Winrates](screenshot.png)\n_Divine winrate hero grid generated 2019-12-23_\n",
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
