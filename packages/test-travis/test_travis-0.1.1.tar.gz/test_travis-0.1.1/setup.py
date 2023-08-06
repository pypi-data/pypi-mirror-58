# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['test_travis']

package_data = \
{'': ['*']}

install_requires = \
['autopep8', 'jinja2', 'poetry']

entry_points = \
{'console_scripts': ['poetry-setup = poetry_setup.core:main']}

setup_kwargs = {
    'name': 'test-travis',
    'version': '0.1.1',
    'description': 'A cookiecutter template for Python project',
    'long_description': '# test_travis\n\n[![Build Status](https://www.travis-ci.org/lin-zone/test_travis.svg?branch=master)](https://www.travis-ci.org/lin-zone/test_travis)\n[![codecov](https://codecov.io/gh/lin-zone/test_travis/branch/master/graph/badge.svg)](https://codecov.io/gh/lin-zone/test_travis)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/test_travis?logo=python&logoColor=FBE072)](https://pypi.org/project/test_travis/)\n[![GitHub](https://img.shields.io/github/license/lin-zone/test_travis)](https://github.com/lin-zone/test_travis/blob/master/LICENSE)\n[![GitHub stars](https://img.shields.io/github/stars/lin-zone/test_travis?logo=github)](https://github.com/lin-zone/test_travis)\n[![GitHub forks](https://img.shields.io/github/forks/lin-zone/test_travis?logo=github)](https://github.com/lin-zone/test_travis)\n',
    'author': 'lin-zone',
    'author_email': 'z_one10@163.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lin-zone/test_travis',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
