.. _reference.configure_ipython_profile:

Configure IPython Profile for Bluesky
=====================================

An IPython profile [#profile]_ is used to enable the console interface for a bluesky
session.

.. index:: startup; snippet

.. _startup_snippet:

Python snippet to start instrument for data collection
------------------------------------------------------

.. This snippet is so useful, it has been promoted to the
   top of this file so it can be found more easily.

This snippet of Python code will start Bluesky for data collection.  Use it in
the IPython startup script and also in Jupyter notebooks.  First, it puts the
parent directory of the ``instrument`` package on the exectuable path, then it
starts the instrument.

.. code-block:: py
   :linenos:

   import pathlib, sys
   sys.path.append(str(pathlib.Path.home() / "bluesky"))
   from instrument.collection import *

.. tip:: Use this snippet in Jupyter notebooks to start the ``instrument``.

A slightly more robust version of this snippet is supplied by this ``bluesky_training`` repository:
:download:`__start_bluesky_instrument__.py <../../../bluesky/console/__start_bluesky_instrument__.py>`

Create IPython Profile for Bluesky
----------------------------------

If there is an existing ``~/.ipython`` directory (perhaps created for
other use from this account), then choose a unique directory for
bluesky. Typical alternative is ``~/.ipython-bluesky``.

.. code-block:: bash
   :linenos:

   export BLUESKY_DIR=~/.ipython-bluesky
   mkdir -p "${BLUESKY_DIR}"
   ipython profile create bluesky --ipython-dir="${BLUESKY_DIR}"

.. [#profile] https://ipython.readthedocs.io/en/stable/config/intro.html#profiles

Add a single Python file to the startup directory
-------------------------------------------------

.. code-block:: text
   :linenos:

     .ipython-bluesky/
       profile_bluesky/
         startup/
           __start_bluesky_instrument__.py --> ~/bluesky/console/__start_bluesky_instrument__.py

.. tip:: when IPython starts ...

   **Every** Python file in the startup directory is run when IPython starts.
   The files are run in lexical (alphabetical) order.
