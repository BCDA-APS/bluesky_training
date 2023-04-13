Recommended Directory Layout
============================

Starter script
--------------

An example starter script (for the Linux bash shell) is supplied:
:download:`blueskyStarter.sh <../../../bluesky/blueskyStarter.sh>`. You might
link this script to a directory on the executable path, such as:

.. code-block:: text

   ~/bin/blueskyStarter.sh  --> ~/bluesky/blueskyStarter.sh

**TIP**: You might rename `~/bin/blueskyStarter.sh` to something appropriate for
your instrument name, such as this hypothetical example: `blueskyFemtoScanner.sh`.

.. raw:: html

   <details>
      <summary>Install the Starter Script</summary>

      <p>
      The commands and settings to configure the local environment to begin a
      Bluesky session can be arranged by a simple shell script that starts the
      session.

      <p>
      To allow this starter script to be called from any directory (such as
      the user's data directory), the starter script can be placed in a
      directory on the user's executable path.

      <p>
      It is useful to create a local directory (such as <code>~/bin</code>) for custom
      starter scripts and executable file links. Use these steps to configure
      your account. Add this line to <code>~/.bash_aliases</code>:

      <pre>export PATH="~/bin:${PATH}"</pre>

      and create the directory:

      <pre>mkdir ~/bin</pre>

   </details>

The *bluesky* directory
-----------------------

Contains the ``instrument`` package and other support:

.. code-block:: text
   :linenos:

   bluesky/
      blueskyStarter.sh
      console/
      __start_bluesky_instrument__.py
      instrument/

.. TODO: gather this html block into a single raw, as above
.. raw:: html

   <details>

.. raw:: html

   <summary>

Install the *bluesky* directory

.. raw:: html

   </summary>

TODO:

.. raw:: html

   </details>

Start Bluesky
-------------

-  Change to desired working directory.
-  Start Bluesky session using the starter script.

.. code-block:: bash

   blueskyStarter.sh
