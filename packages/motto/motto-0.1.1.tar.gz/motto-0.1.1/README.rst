motto
=====

.. image:: https://img.shields.io/pypi/v/motto
   :alt: PyPI
   :target: https://pypi.org/project/motto

.. image:: https://img.shields.io/pypi/pyversions/motto
   :alt: PyPI - Python Version
   :target: https://pypi.org/project/motto

.. image:: https://github.com/attakei/motto/workflows/Continuous%20Integration/badge.svg?branch=master
   :alt: GitHub Actions - Continuous Integration
   :target: https://github.com/attakei/motto/actions

docutils-based sentence linter.

Overview
--------

Motto is sentence linter platform for reStructuredText.

It parses document by ``docutils`` and check any paragraph by linter modules.

Demo
----

.. image:: https://attakei.net/assets/motto/motto-demo.gif

Installation
------------

You can install by ``pip`` command.

.. code-block:: bash

   pip install motto

Usage
-----

Run ``motto`` command.

.. code-block:: bash

   # Check single file
   motto README.rst
   # Checke internals of directory recursively
   motto docs/

More information
----------------

See `Janapanese readme document <./README_ja.rst>`_

License
-------

MIT License. See `it <./LICENSE>`_
