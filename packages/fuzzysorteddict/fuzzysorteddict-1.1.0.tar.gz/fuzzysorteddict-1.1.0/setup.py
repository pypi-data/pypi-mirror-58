# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['fuzzysorteddict']
install_requires = \
['sortedcontainers>=2.1.0,<3.0.0']

setup_kwargs = {
    'name': 'fuzzysorteddict',
    'version': '1.1.0',
    'description': 'A sorted dictionary with nearest-key lookup',
    'long_description': 'fuzzysorteddict\n===============\n\n.. image:: https://travis-ci.com/ncsuarc/FuzzySortedDict.svg?branch=master\n    :target: https://travis-ci.com/ncsuarc/FuzzySortedDict\n\nfuzzysorteddict is a sorted dictionary with nearest-key lookups.\n\n>>> from fuzzysorteddict import FuzzySortedDict\n>>> d = FuzzySortedDict()\n>>> d[1] = 1\n>>> d[2] = 2\n>>> d[1.75]\n2\n\nFuzzySortedDict can be particularly useful for sparsely populated ranges,\nsuch as when working with time.\n\n>>> from fuzzysorteddict import FuzzySortedDict\n>>> import datetime\n>>> d = FuzzySortedDict()\n>>> d[datetime.datetime(2000, 1, 1, 12, 0, 0)] = 1\n>>> d[datetime.datetime(2000, 1, 1, 12, 0, 4)] = 2\n>>> d[datetime.datetime(2000, 1, 1, 12, 0, 1)]\n1\n\nInstallation\n------------\n\nFuzzySortedDict is easily installed with ``pip``.\n\n.. code::\n\n    pip install fuzzysorteddict\n',
    'author': 'NC State Aerial Robotics Club',
    'author_email': 'aerialrobotics@ncsu.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ncsuarc/FuzzySortedDict',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.5',
}


setup(**setup_kwargs)
