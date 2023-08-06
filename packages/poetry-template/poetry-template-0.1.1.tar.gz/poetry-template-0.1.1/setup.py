# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_template',
 'poetry_template.package_one',
 'poetry_template.package_two']

package_data = \
{'': ['*']}

install_requires = \
['black>=19.10b0,<20.0',
 'pytest-cov>=2.8.1,<3.0.0',
 'requests>=2.22.0,<3.0.0',
 'sphinx>=2.3.1,<3.0.0']

setup_kwargs = {
    'name': 'poetry-template',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Mislav Jaksic',
    'author_email': 'jaksicmislav@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
