Changelog
=========

[0.0.6] - 2021-11-29
--------------------

Added
^^^^^

- ``SemVer`` class for easy semantic version number creation.

[0.0.5] - 2021-06-06
--------------------

Added
^^^^^

- ``Timer`` class for timing a block of code
- Sphinx based documentation: https://more-ds.readthedocs.io/en/latest/

Changed
^^^^^^^

- Imported data structures in their parent package, shortening the required
  import statements. Eg ``from more_ds.network.url import URL`` now becomes
  ``from more_ds.network import URL``

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

Fixed
^^^^^

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
