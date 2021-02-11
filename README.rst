More Data Structures
====================

More Data Structures
or ``more-ds`` for short,
provides simple and convenient Python data structures.

Origin
======

The projected started
with the need to extract the simplest of classes
from an exitsting open source library, `nwa-stdlib`_.
That library primarily contained code
that was rather specific to the organization that created the library.
However, the ``URL`` class was a tiny convenience data structure,
with broader applicability,
that took the chore out of programmatically creating URLs.
By extracting that class into a separate project,
one that is specifically focussed on convenient data structures,
it hopefully attracts a broader set of users
that would otherwise don't feel comfortable including `nwa-stdlib`_ as a whole.

The project's name was inpired by the wonderful `More Itertools`_ library.

Data Structures
===============

There is currently one data structure available (more to follow):

- ``URL``

URL
---

The ``URL`` class is a ``str`` (overrides it).
Hence, can be used anywhere a regular string is used.
It overrides two magical methods
that correspond to the ``/`` and ``//`` operators.

The ``/`` operator is used to concatenate separate path components of a URL.
The ``//`` operator is used to append a query string by supplying it with a dictionary.

An example should make this clear:

.. code-block:: python

    >>> from more_ds.network.url import URL
    >>> base_url = URL("http://example.org/")
    >>> api_url = base_url / "api"
    >>> url = api_url / "ip" / "address" // dict(version=4)
    >>> print(url)
    http://example.org/api/ip/address?version=4

When adding path components,
the ``/`` operator will insert or remove redundant slashes where necessary.
The ``//`` automatically take cares of properly URL encoding the keys and values.

.. _nwa-stdlib: https://github.com/workfloworchestrator/nwa-stdlib
.. _More Itertools: https://more-itertools.readthedocs.io/en/stable/index.html
