# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['carloscar']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'carloscar',
    'version': '0.0.2',
    'description': 'co – A command line interface for productivity and every-day tasks',
    'long_description': '# `carloscar`\n[![pypi](https://badge.fury.io/py/carloscar.svg)](https://pypi.python.org/pypi/carloscar/)\n[![Made with Python](https://img.shields.io/pypi/pyversions/carloscar)](https://www.python.org/)\n[![Type hinted - mypy validated](https://img.shields.io/badge/typehinted-yes-teal)](https://github.com/kalaspuff/carloscar)\n[![MIT License](https://img.shields.io/github/license/kalaspuff/carloscar.svg)](https://github.com/kalaspuff/carloscar/blob/master/LICENSE)\n[![Code coverage](https://codecov.io/gh/kalaspuff/carloscar/branch/master/graph/badge.svg)](https://codecov.io/gh/kalaspuff/carloscar/tree/master/carloscar)\n\n*co – A command line interface for productivity and every-day tasks.*\n\n\n## Installation with `pip`\nLike you would install any other Python package, use `pip`, `poetry`, `pipenv` or your weapon of choice.\n```\n$ pip install carloscar\n```\n\n\n## Usage and examples\n\n#### Use-case\n```\n$ co --help\n```\n',
    'author': 'Carl Oscar Aaro',
    'author_email': 'hello@carloscar.com',
    'url': 'https://github.com/kalaspuff/carloscar-cli',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
