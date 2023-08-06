.. expi_skel documentation master file, created by
   sphinx-quickstart on Tue Dec 31 18:05:18 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to expi_skel's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   src/expi_skel
   src/walkthrough

expi_skel is a template for packaging extender scripts as python packages 
that can be distributed in expi.

For a package to be accepted in expi it must:

- be a valid python source distribution
- use a unique name
- contain a valid ``README.rst`` file in the distribution root
- contain a valid ``expi.json`` file in the package root
- contain a valid ``docs`` directory in the distribution root, including:
  - ``index.rst``: the entry point into the documentation
  - ``conf.py``: sphinx documentation config, must use `_build`
  - ``Makefile``: the project documentation Makefile

In addition, it may:

- contain Extender modules that will be installed with the package
  - using the ``vi/`` directory in the package root
- contain additional ``.rst`` or ``.pdf`` files in the ``docs`` directory

The ``expi_skel`` template contains examples of all of the required files with
valid sample content.

To get started making your own package, follow the steps in the walkthrough.




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
