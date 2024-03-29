Install New Instrument
======================

Describes the steps to install a new bluesky instrument.

.. note:: These *instructions have been written for workstations running the Linux operating system*. They may be used for other operating systems but expect some modifications are necessary. One such modification is that the ``libhkl`` library, needed for diffractometer support, is only available for Linux x86_64 host architectures.

.. warning:: In Linux, use the ``bash`` command shell. For more info see `what is bash? <https://bcda-aps.github.io/bluesky_training/reference/_FAQ.html#faq-bash>`__

Installation checklist
--------------------------

The *installation checklist* summarizes the steps with links
to the documentation for each step.

#. run ``new_bluesky_instrument.py ~/bluesky`` (see sections below)
#. `create conda environment <https://bcda-aps.github.io/bluesky_training/reference/_create_conda_env.html>`__
#. `configure IPython profile startup <https://bcda-aps.github.io/bluesky_training/reference/_ipython.html>`__
#. `configure bash with environment variable and alias <https://bcda-aps.github.io/bluesky_training/reference/_create_conda_env.html#create-an-alias-to-activate-the-bluesky-environment>`__
#. Verify the installation by running the `Hello, World! tutorial. <https://bcda-aps.github.io/bluesky_training/tutor/hello_world.html>`__
#. create soft link:  ``ln -s ${HOME}/bluesky/blueskyStarter.sh ~/bin/``
#. Assign a MongoDB catalog for databroker: `instructions for BCDA <https://git.aps.anl.gov/bcda/bluesky-catalogs/-/blob/master/README.md>`__
#. `databroker catalog configuration <https://bcda-aps.github.io/bluesky_training/instrument/_configure_databroker.html#setup-your-databroker-catalog-configuration>`__
#. `initial configuration of instrument <https://bcda-aps.github.io/bluesky_training/instrument/_configure_bluesky_instrument.html#initial-configuration>`__
#. :ref:`start a remote repository <start_vc>`

Setup a bluesky instrument
--------------------------

Use the ``new_bluesky_instrument.py``
`program <https://github.com/BCDA-APS/bluesky_training/blob/main/new_bluesky_instrument.py>`__
to install a new bluesky instrument configuration from the online `APS
Bluesky Training <https://github.com/BCDA-APS/bluesky_training>`__
repository template. The program creates a new ``bluesky`` directory in
the home directory. Use ``new_bluesky_instrument.py -h`` for usage
information.

The ``new_bluesky_instrument.py`` program requires Python 3.6+ and the
`requests <https://docs.python-requests.org/en/latest/index.html>`__
package.

.. raw:: html

   <details>
   <summary>How can I tell the python version I am using?</summary>

   Type the following command:

   <pre>
   $ <b>python --version</b>
   </pre>

   This will print the version of Python currently installed on your
   system. You may wish to review
   <a href="https://www.python.org/downloads/">instructions to  upgrade Python</a>.
   </details>

.. raw:: html

   <details>
   <summary>How can I tell if the requests package is installed?</summary>

   Test that the <code>requests</code> package is available by trying to import
   it. In a terminal, type the following command and press <em>Enter</em>:
   <pre>
   $ <b>python3 -c "import requests"</b>
   </pre>

   If the command runs without any errors, then you have the
   <code>requests</code> package installed. If you don't have it installed,
   you'll see an error message like:
   <pre>"ModuleNotFoundError: No module named 'requests'"</pre>
   </details>
   <br />

Run the installer program (instructions are different if you are using a
workstation at APS with access to the ``/APSshare`` file server):

.. tabs::

   .. tab:: At APS

      On an APS machine with access to APSshare,
      run this command from a terminal session:

      .. raw:: html

         <pre>
         $ <b>python3 /APSshare/bin/new_bluesky_instrument.py ~/bluesky</b>
         </pre>

   .. tab:: Not at APS

      Workstations on other networks (with no access to APSshare) need to
      download this program.  Open the file in your browser with this
      :download:`link <../../../new_bluesky_instrument.py>`
      and use your browser's commands to **Save As ...** in the directory of
      your choice (use the file name: `new_bluesky_instrument.py`). Then,
      navigate to the directory where the program was downloaded and run the
      following command:

      .. raw:: html

         <pre>
         $ <b>python3 new_bluesky_instrument.py ~/bluesky</b>
         </pre>

When run successfully, the program output should look like this:

.. raw:: html

   <pre>
   INFO:__main__:Requested installation to: 'bluesky'
   INFO:__main__:Downloading 'https://github.com/BCDA-APS/bluesky_training/archive/refs/heads/main.zip'
   INFO:__main__:Extracting content from '/tmp/bluesky_training-main.zip'
   INFO:__main__:Installing to '/home/user/bluesky'
   INFO:__main__:Initialized Git repository in '/home/user/bluesky'
   </pre>
   
The installer program takes care of initializing a local git repository in the ``bluesky`` folder.
Further instructions are provided :ref:`below <start_vc>` to create a remote reposititory. 


Activate the bluesky conda environment
--------------------------------------

.. raw:: html

   <details>
   <summary>How to create a conda environment for bluesky?</summary>

   See <a href="https://bcda-aps.github.io/bluesky_training/reference/_create_conda_env.html">here</a>.

   </details>

To use bluesky, you first need to activate the bluesky conda environment:

.. raw:: html

   <pre>
   $ <b>conda activate bluesky_2023_3</b>
   </pre>

The prompt changes to display ``(bluesky_2023_3)`` .

.. raw:: html

   <details>
   <summary>How to create an alias to activate the bluesky environment?</summary>

   See <a href="https://bcda-aps.github.io/bluesky_training/reference/_create_conda_env.html#create-an-alias-to-activate-the-bluesky-environment">here</a>. 
   </details>



This activation will remain in effect for the duration of the session
(*i.e.* as long as the terminal stays open), unless you activate a
different environment or deactivate it using the ``conda deactivate``
command.




Test the new bluesky instrument
-------------------------------

At this point, you have assembled enough of the parts to test the
initial installation with bluesky. Follow the steps in the following guides:

- `Hello World <https://bcda-aps.github.io/bluesky_training/tutor/hello_world.html>`_: test the basic installation of bluesky.
- `Test my new instrument package <https://bcda-aps.github.io/bluesky_training/instrument/_test_new_instrument.html>`_: verify the new instrument package loads without error.
- `Test bluesky with EPICS <https://bcda-aps.github.io/bluesky_training/instrument/_test_bluesky_at_aps.html>`_: make sure you are able to connect to EPICS PVs at the APS.


In the remaining steps, we'll configure the instrument for your catalog
and specific hardware configuration.



Create a bluesky IPython profile
--------------------------------

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


Setup your databroker catalog configuration
-------------------------------------------

Contact BCDA (bcda@aps.anl.gov) for assignment of a databroker catalog
configuration.

For example purposes, let's assume you have been given this
bluesky/databroker catalog assignment:

-  name: ``45ida_abcd``
-  MongoDB server: ``mongoserver.xray.aps.anl.gov``
-  MongoDB collection: ``45ida_abcd-bluesky``

See this `guide <https://bcda-aps.github.io/bluesky_training/instrument/_configure_databroker.html>`__ to configure databroker.

Confirm that databroker can find the ``45ida_abcd`` catalog by running
the python executable and passing the python commands as a command-line
option:

.. raw:: html

   <pre>
   $ <b>python -c "import databroker; print(list(databroker.catalog))"</b>
   ['45ida_abcd']
   </pre>

.. _start_vc:

Start version control
---------------------

While this step is optional, it is **highly recommended** that you keep
your bluesky instrument directory under some form of software version
control. At minimum, this can provide some form of backup protection. It
also helps others to collaborate with similar bluesky instruments by
sharing your instrument's implementations.

The installer program initializes a local git repository in the ``bluesky``
folder. We now need to create a blank remote repository, for example
on `GitHub <https://github.com/>`_ or the `APS GitLab server
<https://git.aps.anl.gov/>`_ using your :ref:`beamline organization 
<beamline-github-organizations>`. 
Note that the bluesky team recommends GitHub. (Why is that? See section
:ref:`git-help` for more info).

.. note:: APS beamlines use specific conventions for :ref:`beamline organization <beamline-github-organizations>`.

.. warning:: To simplify the process (avoid merge conflicts), it is important for the
   remote repository to be **empty**. To do so, carefully follow the instructions described 
   in the tabs below.


.. tabs::

   .. tab:: GitHub (recommended)

      Follow the official GitHub instructions `Create a repository <https://docs.github.com/en/get-started/quickstart/create-a-repo#create-a-repository>`_
      with the modifications below:

      .. raw:: html

         <ul>
         <li><b>Do not</b> select "Initialize this repository with a README" (skip step 5)</li>
         <li>Keep the other options as default:</li>
         <ul>
         <li>Visibility: Public</li>
         <li>Repository template: No template</li>
         <li><code>.gitignore</code> template: None</li>
         <li>License: None</li>
         </ul>
         </ul>



   .. tab:: GitLab

      Follow the official GitLab instructions `Create a blank project <https://docs.gitlab.com/ee/user/project/#create-a-blank-project>`_
      with the modifications below:

      .. raw:: html

         <ul>
         <li>Visibility Level: Public</li>
         <li><b>Unselect</b> "Initialize repository with a README"</li>
         <li>Keep "Enable Static Application Security Testing (SAST)" unselected</li>
         </ul>


The next steps are common to both web-based repositories (GitHub and GitLab):

- copy the remote `repository URL <https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#choosing-a-url-for-your-remote-repository>`_, for example,
  ``https://github.com/OWNER/REPOSITORY.git``
- open a terminal

.. raw:: html

   <pre>
   $ <b>cd ~/bluesky </b>
   $ <b>git remote add origin https://github.com/OWNER/REPOSITORY.git  </b>
   # Set a new remote

   $ <b>git remote -v  </b>
   # Verify new remote
   > origin  https://github.com/OWNER/REPOSITORY.git (fetch)
   > origin  https://github.com/OWNER/REPOSITORY.git (push)

   $ <b>git push -u origin main  </b>
   # Push repo to remote
   </pre>


For more information, you can refer to the official GitHub documentation:

- which URL to use (``ssh`` vs ``https``): `About remote repositories <https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories>`_
- ``git remote add`` command: `Adding a remote repository <https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories#adding-a-remote-repository>`_
- ``git push`` command: `Pushing to a remote repository <https://docs.github.com/en/enterprise-server@3.9/get-started/using-git/pushing-commits-to-a-remote-repository>`_

Configure bluesky instrument
----------------------------

See this `advice <https://bcda-aps.github.io/bluesky_training/instrument/_configure_bluesky_instrument.html>`__ for
configuration of the ``instrument`` package (*i.e.* content in the
``instrument/`` directory).
