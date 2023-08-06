========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/ntools/badge/?style=flat
    :target: https://readthedocs.org/projects/ntools
    :alt: Documentation Status


.. |travis| image:: https://travis-ci.com/python-metatooling/ntools.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/python-metatooling/ntools

.. |codecov| image:: https://codecov.io/github/python-metatooling/ntools/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/python-metatooling/ntools

.. |version| image:: https://img.shields.io/pypi/v/ntools.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/pypi/ntools

.. |commits-since| image:: https://img.shields.io/github/commits-since/python-metatooling/ntools/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/python-metatooling/ntools/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/ntools.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/pypi/ntools

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/ntools.svg
    :alt: Supported versions
    :target: https://pypi.org/pypi/ntools

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/ntools.svg
    :alt: Supported implementations
    :target: https://pypi.org/pypi/ntools


.. end-badges

Some tools. How many? n.

* Free software: MIT License

Installation
============

::

    pip install ntools

Documentation
=============


https://ntools.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
