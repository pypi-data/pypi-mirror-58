# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['izakaya']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'izakaya',
    'version': '0.0.1',
    'description': 'Real time event sourcing and application state management in a distributed computing context',
    'long_description': '# `izakaya`\n[![pypi](https://badge.fury.io/py/izakaya.svg)](https://pypi.python.org/pypi/izakaya/)\n[![Made with Python](https://img.shields.io/pypi/pyversions/izakaya)](https://www.python.org/)\n[![Type hinted - mypy validated](https://img.shields.io/badge/typehinted-yes-teal)](https://github.com/kalaspuff/izakaya)\n[![MIT License](https://img.shields.io/github/license/kalaspuff/izakaya.svg)](https://github.com/kalaspuff/izakaya/blob/master/LICENSE)\n[![Code coverage](https://codecov.io/gh/kalaspuff/izakaya/branch/master/graph/badge.svg)](https://codecov.io/gh/kalaspuff/izakaya/tree/master/izakaya)\n\n*Real time event sourcing and application state management in a distributed computing context.*\n\n\n## Installation with `pip`\nLike you would install any other Python package, use `pip`, `poetry`, `pipenv` or your weapon of choice.\n```\n$ pip install izakaya\n```\n\n\n## Usage and examples\n\n#### Use-case\n```\nimport izakaya\n\n```\n',
    'author': 'Carl Oscar Aaro',
    'author_email': 'hello@carloscar.com',
    'url': 'https://github.com/kalaspuff/izakaya',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
