More Data Structures
====================

More Data Structures
or ``more-ds`` for short,
provides simple and convenient Python data structures.


Data Structures
===============

id
--

``SemVer``
    Class for easy creation of semantic version numbers.

network
-------

``URL``
    Class for easy (unvalidated) URL construction.

time
----

``Timer``
    Context manager for timing a block of code.

Getting Started
===============

.. code-block:: console

    % pip install more-ds

.. code-block:: python

    >>> from more_ds.network import URL
    >>> base_url = URL("http://example.org/")
    >>> api_url = base_url / "api"
    >>> url = api_url / "ip" / "address" // dict(version=4)
    >>> print(url)
    http://example.org/api/ip/address?version=4

Or

.. code-block:: python

    from time import sleep

    from more_ds.time import Timer
    with Timer() as t:
        # sleep for half a second
        sleep(.5)

    print(t.elapsed)  # -> 0:00:00.501864


Or

.. code-block:: python

    >>> from more_ds.id import SemVer
    >>> old = SemVer("v3.1.4")
    >>> new = SemVer("3.2")
    >>> old
    SemVer("3.1.4")
    >>> new
    SemVer("3.2.0")
    >>> old == new
    False
    >>> old < new
    True
    >>> old > new
    False
    >>> repr(old)
    'SemVer("3.1.4")'
    >>> repr(new)
    'SemVer("3.2.0")'
    >>> isinstance(old, str)
    True


Origin
======

The projected started
with the need to extract the simplest of classes
from an existing open source library, `nwa-stdlib`_.
That library primarily contained code
that was rather specific to the organization that created the library.
However, the ``URL`` class was a tiny convenience data structure,
with broader applicability,
that took the chore out of programmatically creating URLs.
By extracting that class into a separate project,
one that is specifically focussed on convenient data structures,
it hopefully attracts a broader set of users
that would otherwise don't feel comfortable including `nwa-stdlib`_ as a whole.

The project's name was inspired by the wonderful `More Itertools`_ library.

.. _nwa-stdlib: https://github.com/workfloworchestrator/nwa-stdlib
.. _More Itertools: https://more-itertools.readthedocs.io/en/stable/index.html
