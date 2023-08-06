# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['ready']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ready',
    'version': '0.5.1',
    'description': 'Take control of the event loop with simplified task management and queueing',
    'long_description': '# `ready`\n[![pypi](https://badge.fury.io/py/ready.svg)](https://pypi.python.org/pypi/ready/)\n[![Made with Python](https://img.shields.io/pypi/pyversions/ready)](https://www.python.org/)\n[![Type hinted - mypy validated](https://img.shields.io/badge/typehinted-yes-teal)](https://github.com/kalaspuff/ready)\n[![MIT License](https://img.shields.io/github/license/kalaspuff/ready.svg)](https://github.com/kalaspuff/ready/blob/master/LICENSE)\n[![Code coverage](https://codecov.io/gh/kalaspuff/ready/branch/master/graph/badge.svg)](https://codecov.io/gh/kalaspuff/ready/tree/master/ready)\n\n*A set of functions to simplify task management on the event loop using asyncio on Python 3.6, 3.7 and 3.8.*\n\n\n## Installation with `pip`\nLike you would install any other Python package, use `pip`, `poetry`, `pipenv` or your weapon of choice.\n```\n$ pip install ready\n```\n\n\n## Usage and examples\n\n#### Use-case\n```\nimport ready\n\n```\n',
    'author': 'Carl Oscar Aaro',
    'author_email': 'hello@carloscar.com',
    'url': 'https://github.com/kalaspuff/ready',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
