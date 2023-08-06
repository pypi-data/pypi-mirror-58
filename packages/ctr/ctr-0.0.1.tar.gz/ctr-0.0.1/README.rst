========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-ctr/badge/?style=flat
    :target: https://readthedocs.org/projects/python-ctr
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/samesense/python-ctr.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/samesense/python-ctr

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/samesense/python-ctr?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/samesense/python-ctr

.. |requires| image:: https://requires.io/github/samesense/python-ctr/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/samesense/python-ctr/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/samesense/python-ctr/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/samesense/python-ctr

.. |version| image:: https://img.shields.io/pypi/v/ctr.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/ctr

.. |wheel| image:: https://img.shields.io/pypi/wheel/ctr.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/ctr

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/ctr.svg
    :alt: Supported versions
    :target: https://pypi.org/project/ctr

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/ctr.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/ctr

.. |commits-since| image:: https://img.shields.io/github/commits-since/samesense/python-ctr/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/samesense/python-ctr/compare/v0.0.1...master



.. end-badges

Concatenate files w/ headers.

* Free software: MIT license

Installation
============

::

    pip install ctr

You can also install the in-development version with::

    pip install https://github.com/samesense/python-ctr/archive/master.zip


Documentation
=============


https://python-ctr.readthedocs.io/


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
