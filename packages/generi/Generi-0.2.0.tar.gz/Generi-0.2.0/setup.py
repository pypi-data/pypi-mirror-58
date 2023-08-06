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
    'version': '0.2.0',
    'description': 'Manage huge sets of Docker images using matrix builds',
    'long_description': '![Generi logo](/docs/images/icon.png?raw=true "Generi logo")\n\n📚 [Documentation](https://generi.nicklehmann.sh/)\n\n🐳 About\n========\n\nGeneri is a tool to automatically create Dockerfiles and build images for a large combination of different factors. It is the right tool if you need to build many similar images with slightly different parameters. \n\nFor example, say you are developing an app. You might want to build one docker image for python 2.7, 3.6, 3.8. And for each python version, you need one with a database included or not. And all that for each tag. If you have experienced a scenario like this, try out Generi.\n\n🎇 Features\n===========\n\n- Configuration in yaml\n- Specify different parameter to form a build matrix\n- Generate Dockerfile for each combination\n- Build all variations of your image with one command\n- Push to the repository of your choice\n- Everything customisable using [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)\n\n✈️ Quickstart\n=============\n\n`Generi` can be configured using a simple yaml file that defines your matrix build. \n\n*schema.yaml*\n\n```yaml\nparameters:\n  python_version:\n    - 2.7\n    - 3.5\n    - 3.6\n    - 3.7\n  operating_system:\n    - buster\n    - alpine\n\ntemplate: templates\noutput: "output/{{ python_version }}/{{ operating_system }}"\nimage: "nicklehmann/myapplication:py{{ python_version }}-{{ operating_system }}"\n\nregistry:\n  username: nicklehmann\n```\n\n*templates/Dockerfile*\n\n```dockerfile\nFROM python:{{ python_version }}-{{ operating_system }}\n\nCOPY main.py main.py\n\nCMD ["python", "main.py"]\n```\n\nFirst, render your dockerfiles by running\n\n```bash\n$ generi write schema.yaml\n```\n\nAfter that, build and optionally push your image.\n\n```bash\n$ generi build schema.yaml\n$ generi push schema.yaml\n```\n\nFor more examples, please see the [usage](https://generi.nicklehmann.sh/usage/usage.html) section of the documentation.\n',
    'author': 'Nick Lehmann',
    'author_email': 'nick@lehmann.sh',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nick-lehmann/Generi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
