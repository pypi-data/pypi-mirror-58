# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dirs']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dirs',
    'version': '0.1.0',
    'description': 'A small library for obtaining platform dependent directory paths for application and user directories',
    'long_description': None,
    'author': 'Isabella Muerte',
    'author_email': '63051+slurps-mad-rips@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
