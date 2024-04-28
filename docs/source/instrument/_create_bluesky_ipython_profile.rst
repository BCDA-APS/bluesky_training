.. _instrument.create_bluesky_ipython_profile:

Create a bluesky IPython profile
--------------------------------

.. note::  Compare with :ref:`reference.configure_ipython_profile`

This bash command create a new IPython profile for bluesky:


.. raw:: html

   <pre>
   $ <b>ipython profile create bluesky --ipython-dir="~/.ipython"</b>
   </pre>

Next, create the starter script for this profile. This will ensure that the instrument
package gets loaded when starting a bluesky IPython session.

.. note:: Copy *all* these lines and paste them exactly into your terminal.

.. code:: bash

   cat > ~/.ipython/profile_bluesky/startup/00-start-bluesky.py  << EOF
   import pathlib, sys
   sys.path.append(str(pathlib.Path().home() / "bluesky"))
   from instrument.collection import *
   EOF


To start an IPython session with the new bluesky profile, you can now use the following command:

.. raw:: html

   <pre>
   $ <b>ipython --profile=bluesky</b>
   </pre>


.. raw:: html

   <details>
   <summary>How to create an alias to start a bluesky session?</summary>

   Creating a bash alias is like creating a custom shortcut.
   You can do this by editing the <code>~/.bashrc</code> and  <code>~/.bash_aliases</code>
   files, which are configuration files for your bash shell.
   Here's a simple step-by-step guide:


   <ol>
   <li>Open a terminal.</li>
   <li>Open the <code>~/.bashrc</code> and <code>~/.bash_aliases</code> files with your prefered text editor,
   <i>e.g.</i>:
   <pre>
   $ <b> gedit ~/.bashrc ~/.bash_aliases </b>
   </pre>
   If any of those files do not exist, this command will create blank ones.
   </li>
   <li>In <code>~/.bash_aliases</code>, scroll down to the end of the file or find a suitable place to add your alias.
   On a new line, type:
   <pre>
   export BLUESKY_CONDA_ENV=bluesky_2023_3
   alias start_bluesky='conda activate ${BLUESKY_CONDA_ENV}; ipython --profile=bluesky'
   </pre>
   <b>Note:</b> this lines may already be included in your <code>~/.bash_aliases</code>,
   <i>e.g.</i>, if you have created an alias to activate the bluesky conda environment.
   </li>
   <li> In <code>~/.bashrc</code>, scroll down to the end of the file or find a suitable place to add the following lines:
   <pre>
   source ~/.bash_aliases
   </pre>
   </li>
   <li>Save your changes.</li>
   <li>Type <code>bash</code> and press enter, or open a new terminal windows to make the new alias available.</li>

   </ol>
   You can now use the alias <code>start_bluesky</code> to activate the conda environment and
   and start a new bluesky session in a terminal.

   </details>


For more info about IPython configuration, see `here <https://ipython.readthedocs.io/en/stable/config/intro.html>`__.
