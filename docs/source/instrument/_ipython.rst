IPython Profile
===============

An IPython profile [#profile]_ is used to enable the console interface for a bluesky
session.


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

where :download:`__start_bluesky_instrument__.py <../../../bluesky/console/__start_bluesky_instrument__.py>`
is summarized (there are additional features) by:

.. code-block:: py
   :linenos:

   import pathlib, sys
   sys.path.append(str(pathlib.Path.home() / "bluesky"))
   from instrument.collection import *
