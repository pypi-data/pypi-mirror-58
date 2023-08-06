# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['mazel']
entry_points = \
{'console_scripts': ['mazel = mazel:main']}

setup_kwargs = {
    'name': 'mazel',
    'version': '0.0.1',
    'description': 'Makefile caller',
    'long_description': None,
    'author': 'John Paulett',
    'author_email': 'john@paulett.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
