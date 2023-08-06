fuzzysorteddict
===============

.. image:: https://travis-ci.com/ncsuarc/FuzzySortedDict.svg?branch=master
    :target: https://travis-ci.com/ncsuarc/FuzzySortedDict

fuzzysorteddict is a sorted dictionary with nearest-key lookups.

>>> from fuzzysorteddict import FuzzySortedDict
>>> d = FuzzySortedDict()
>>> d[1] = 1
>>> d[2] = 2
>>> d[1.75]
2

FuzzySortedDict can be particularly useful for sparsely populated ranges,
such as when working with time.

>>> from fuzzysorteddict import FuzzySortedDict
>>> import datetime
>>> d = FuzzySortedDict()
>>> d[datetime.datetime(2000, 1, 1, 12, 0, 0)] = 1
>>> d[datetime.datetime(2000, 1, 1, 12, 0, 4)] = 2
>>> d[datetime.datetime(2000, 1, 1, 12, 0, 1)]
1

Installation
------------

FuzzySortedDict is easily installed with ``pip``.

.. code::

    pip install fuzzysorteddict
