========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/jollyjumper/badge/?style=flat
    :target: https://readthedocs.org/projects/jollyjumper
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/linhd-postdata/jollyjumper.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/linhd-postdata/jollyjumper

.. |requires| image:: https://requires.io/github/linhd-postdata/jollyjumper/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/linhd-postdata/jollyjumper/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/linhd-postdata/jollyjumper/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/linhd-postdata/jollyjumper

.. |codecov| image:: https://codecov.io/github/linhd-postdata/jollyjumper/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/linhd-postdata/jollyjumper

.. |version| image:: https://img.shields.io/pypi/v/jollyjumper.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/jollyjumper

.. |commits-since| image:: https://img.shields.io/github/commits-since/linhd-postdata/jollyjumper/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/linhd-postdata/jollyjumper/compare/v0.0.1...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/jollyjumper.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/jollyjumper

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/jollyjumper.svg
    :alt: Supported versions
    :target: https://pypi.org/project/jollyjumper

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/jollyjumper.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/jollyjumper


.. end-badges

Scansion tool for Spanish texts

* Free software: Apache Software License 2.0

Installation
============

::

    pip install jollyjumper

Documentation
=============


https://jollyjumper.readthedocs.io/


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
