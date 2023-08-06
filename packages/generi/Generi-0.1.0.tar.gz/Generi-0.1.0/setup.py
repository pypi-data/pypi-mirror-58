# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['generi', 'generi.commands', 'generi.config']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=2.10.3,<3.0.0',
 'aiodocker>=0.17.0,<0.18.0',
 'fire>=0.2.1,<0.3.0',
 'pyyaml>=5.2,<6.0']

entry_points = \
{'console_scripts': ['generi = generi.cli:main']}

setup_kwargs = {
    'name': 'generi',
    'version': '0.1.0',
    'description': 'Manage huge sets of Docker images using matrix builds',
    'long_description': None,
    'author': 'Nick Lehmann',
    'author_email': 'nick@lehmann.sh',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
