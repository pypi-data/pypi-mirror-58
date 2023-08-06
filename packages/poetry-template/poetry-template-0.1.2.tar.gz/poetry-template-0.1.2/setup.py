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

entry_points = \
{'console_scripts': ['poetry-template = poetry_template.runner:run']}

setup_kwargs = {
    'name': 'poetry-template',
    'version': '0.1.2',
    'description': 'A sample Python project.',
    'long_description': '## Python Project Template\n```\n# Note: Install Python 3\n\n# Note: install Poetry for Linux\n$: curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python\n\n# Note: install Poetry for Windows\n$: (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python\n\n$: python get-poetry.py --uninstall\n```\n\n```\n$: poetry install  # install all dependencies\n```\n\n### docs\n\n```\n$: poetry shell\n$: cd docs\n# Note: review source/conf.py and source/index.rst\n$: make html\n# Note: see docs in docs/build/apidocs/index.html\n```\n\n### poetry_template\n\n```\n$: poetry run python ./poetry_template/runner.py\n```\n\n### tests\n\n```\n$: poetry run pytest\n```\n\n```\n$: poetry run pytest --cov=poetry_template --cov-report=html tests\n#: Note: see coverage report in htmlcov/index.html\n```\n\n### poetry.lock\n\nDependencies, Python version and the virtual environment are managed by `Poetry`.\n\n```\n$: poetry search Package-Name\n$: poetry add Package-Name[==Package-Version]\n```\n\n### pyproject.toml\n\nDefine project entry point and metadata.  \n\n### setup.cfg\n\nConfigure Python libraries.  \n\n### Linters\n\n```\n$: poetry run black .\n```\n\n### Build and publish\n\n```\n$: poetry config pypi-token.pypi PyPI-API-Access-Token\n\n$: poetry publish --build\n```\n',
    'author': 'Mislav Jaksic',
    'author_email': 'jaksicmislav@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MislavJaksic/Python-Project-Template',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
