Installation
============

Describes the steps to install a new bluesky instrument.

**Note**: These *instructions have been written for workstations running
the Linux operating system*. They may be used for other operating
systems but expect some modifications are necessary. One such
modification is that the ``libhkl`` library, needed for diffractometer
support, is only available for Linux x86_64 host architectures.

**IMPORTANT**: In Linux, use the ``bash`` command shell. For more info
see `what is
bash? <https://bcda-aps.github.io/bluesky_training/reference/_FAQ.html#faq-bash>`__.

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
   $ <b>python -c "import requests"</b>
   </pre>

   You might need to <em>specify</em> <code>python3</code>:
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

   .. tab:: at APS

      On an APS machine with access to APSshare,
      run this command from a terminal session:

      .. raw:: html

         <pre>
         $ <b>python /APSshare/bin/new_bluesky_instrument.py ~/bluesky</b>
         </pre>

   .. tab:: not at APS

      Workstations on other networks (with no access to APSshare) need to
      download this program from the URL above. Navigate to the directory where
      the program was downloaded and run the following command:

      .. raw:: html

         <pre>
         $ <b>python new_bluesky_instrument.py ~/bluesky</b>
         </pre>

When run successfully, the program output should look like this:

.. raw:: html

   <pre>
   INFO:__main__:Requested installation to: 'bluesky'
   INFO:__main__:Downloading 'https://github.com/BCDA-APS/bluesky_training/archive/refs/heads/main.zip'
   INFO:__main__:Extracting content from '/tmp/bluesky_training-main.zip'
   INFO:__main__:Installing to '/home/user/bluesky'
   </pre>

The installer checks the ``/tmp`` directory for the ZIP file from the GitHub
repository.  A fresh ZIP file is downloaded if the file is not found or is older
than a day.

Activate the bluesky conda environment
--------------------------------------

.. raw:: html

   <details>
   <summary>How to create a conda environment for bluesky?</summary>

   See <a href="https://bcda-aps.github.io/bluesky_training/instrument/_create_conda_env.html">here</a>.

   </details>

.. raw:: html

   <details>
   <summary>How do I know if I have a conda environment for bluesky?</summary>

   <!-- html comment
   Since we're inside a raw html block, NONE of the rst syntax will work properly.

   Switch back to rst here by unindenting these blocks.
   -->

First, check that you have the ``conda`` command.  Type this command::

   which conda

If this prints a (directory and) file, you have the ``conda`` command. If
nothing is printed, you do not have the ``conda`` command.  Load it with these
next instructions.

.. rst comment
   The command "conda activate" works only when the "conda" command is available.
   When it is not available, then the "conda" command can be added by sourcing it
   using the activate script.  "ource activate".  A common twist is when the
   "activate" script is not in the default path.  Then use "source /path/to/activate",
   such as the miniconda instructions for APS.

.. tabs::

   .. tab:: at APS

      On a machine with access to APSshare, type the command::

         source /APSshare/miniconda/x86_64/bin/activate

   .. tab:: not at APS

      On a machine with no access to APSshare, type the command::

         source activate
      
      .. tip:: You might need to supply the complete path to the ``activate`` script,
         such as shown in the *at APS* tab.

.. FIXME: These instructions are out of order from above and/or repetitive.

The prompt changes to displays ``(base)``. Now you can use
``conda env list`` to see the environments you have and the directories
in which they are installed.

If you are getting an error message (``bash: conda: command not found``
or ``bash: activate: No such file or directory``), conda is not
installed on your computer or it is not added to the system's PATH
environment variable.

You can try to install conda by following the installation instructions
for your operating system. You can find the instructions for Windows,
macOS, and Linux on the official conda documentation
`website <https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>`__.

Once conda is installed, you can activate it by opening a new terminal
or command prompt and typing ``conda activate``. If you still encounter
the same error message, you may need to add the conda installation
directory to your system's PATH environment variable manually. You can
find instructions on how to do this in the Conda documentation.

.. raw:: html

   </details>
   <br />

To use bluesky, you need to activate the bluesky conda environment.
Here's an example:

.. raw:: html

   <pre>
   $ <b>conda activate bluesky_2023_2</b>
   </pre>

The prompt changes to display ``(bluesky_2023_2)`` .

This activation will remain in effect for the duration of the session
(*i.e.* as long as the terminal stays open), unless you activate a
different environment or deactivate it using the ``conda deactivate``
command.

Test the new bluesky instrument
-------------------------------

At this point, you have assembled enough of the parts to test the
initial installation with bluesky. Follow the steps in this
`guide <./_test_new_instrument.md>`__ to test the installation.
Additional instructions are available to `test <./_testing.md>`__ the
installation with EPICS.

In the remaining steps, we'll configure the instrument for your catalog
and specific hardware configuration.

Setup your databroker catalog configuration
-------------------------------------------

Contact BCDA (bcda@aps.anl.gov) for assignment of a databroker catalog
configuration.

Let's assume (for example purposes), you have been given this
bluesky/databroker catalog assignment:

-  name: ``45ida_abcd``
-  MongoDB server: ``mongoserver.xray.aps.anl.gov``
-  MongoDB collection: ``45ida_abcd-bluesky``

See this `guide <./_configure_databroker.md>`__ to configure databroker.

Confirm that databroker can find the ``45ida_abcd`` catalog (by running
the python executable and passing the python commands as a command-line
option):

.. raw:: html

   <pre>
   $ <b>python -c "import databroker; print(list(databroker.catalog))"</b>
   ['45ida_abcd']
   </pre>

IPython profile
---------------

If there is an existing ``~/.ipython`` directory (perhaps created for
other use from this account), then choose a unique directory for
bluesky. Typical alternative is ``~/.ipython-bluesky``. These bash
script commands create the `IPython
profile <https://ipython.readthedocs.io/en/stable/config/intro.html>`__
for bluesky, then create a starter script for the ``instrument`` package
within that profile's ``startup`` directory.

First, use ipython to create the profile

.. code:: bash

   ipython profile create bluesky --ipython-dir="~/.ipython"

Next, create the starter script for the profile.  (Copy *all* these lines and
paste them exactly into your terminal.)

.. code:: bash

   cat > ~/.ipython/profile_bluesky/startup/00-start-bluesky.py  << EOF
   import pathlib, sys
   sys.path.append(str(pathlib.Path().home() / "bluesky"))
   from instrument.collection import *
   EOF

Start version control
---------------------

While this step is optional, it is **highly recommended** that you place
your bluesky instrument directory under some form of software version
control. At minimum, this can provide some form of backup protection. It
also helps others to collaborate with similar bluesky instruments by
sharing your instrument's implementations.

Instructions for using `git <https://git-scm.com/>`__ as software
version control with `GitHub <https://github.com/>`__ or the `APS GitLab
server <https://git.aps.anl.gov/>`__ are provided in `this separate
document <../reference/_git-help.rst>`__.

Configure bluesky instrument
----------------------------

See this `advice <./_configure_bluesky_instrument.md>`__ for
configuration of the ``instrument`` package (content in the
``instrument/`` directory).
