Extension Helpers
=================

The **extension-helpers** package includes convenience helpers to assist with
building Python packages with compiled C/Cython extensions. It is developed by
the Astropy project but is intended to be general and usable by any Python
package.

This is not a traditional package in the sense that it is not intended to be
installed directly by users or developers. Instead, it is meant to be accessed
when the ``setup.py`` command is run and should be defined as a build-time
dependency in ``pyproject.toml`` files.

.. toctree::
   :maxdepth: 1

   using.rst
   openmp.rst
   api.rst
