Changelog
=========

[0.0.4] - 2021-05-30
--------------------

Added
^^^^^

- Added ``py.typed`` to package, so that MyPy can use the type annotations from
  ``more-ds``.
- Included ``CHANGELOG.rst`` in ``sdist`` and specified ``project_urls`` in
  ``setup.cfg`` so that the changelog is visible from pypi.org.


[0.0.3] - 2021-01-22
--------------------

Fixed
^^^^^

- Allow for repeatedly adding new query parameters (contributed by Jan Murre
  @jjmurre)

[0.0.2] - 2021-01-11
--------------------

Changed
^^^^^^^

- Fixed README.rst rendering on PyPi.


[0.0.1] - 2021-02-11
--------------------

Added
^^^^^

- Initial version.
- Copied ``URL`` class + tests from https://github.com/workfloworchestrator/nwa-stdlib

Changed
^^^^^^^

- Modified example in ``URL``'s docstring to be in doctest format.
