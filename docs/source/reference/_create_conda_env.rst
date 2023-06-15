Create bluesky environment
==========================

Describes the steps to create a virtual environment for a bluesky instrument
(see `setup a bluesky instrument
<https://bcda-aps.github.io/bluesky_training/instrument/_install_new_instrument.html#setup-a-bluesky-instrument>`__).

A bluesky instrument uses many Python packages not included in the Python
Standard Library. Rather than add these directly into the system Python
installation, it is recommended to create a Python virtual environment which has
the suite of packages (and specific versions) required.

.. raw:: html

    <details><summary>More about conda virtual environments</summary>
    A virtual environment gives your control over the suite of installed
    packages and insulates you from any system software updates. It is likely
    that you will have more than one conda environment available.  Each of these
    has a complete installation of Python with a suite of packages.  The suite
    may differ between the environments, as well as the package versions. Even
    the Python version itself may be different.

      - Each conda environment has a name, which corresponds to the file
        directory in which the environments packages, libraries, and other
        resources are stored. 
      - When you install or update package(s) in one environment, this will not
        affect any of the other environments. This makes it easy to control
        which software is installed.

    The <code>base</code> environment refers to the default environment created
    when you install conda, which is a package manager and environment
    management system for Python. The <code>base</code> environment is created
    automatically during the installation process, and it serves as the starting
    point for managing and creating additional environments. When you install
    packages or libraries using conda without specifying a specific environment,
    the packages are installed into the <code>base</code> environment by
    default. The <code>base</code> environment is often used for general-purpose
    Python development or as a fallback option when you haven't explicitly
    created any other environments. However, it is recommended to create
    separate environments for different projects or applications to avoid
    conflicts between package versions. This allows you to isolate the
    dependencies of each project and maintain consistent environments.
    </details>


Activate conda
--------------

**IMPORTANT**: In Linux, use the ``bash`` command shell. For more info
see `what is
bash? <https://bcda-aps.github.io/bluesky_training/reference/_FAQ.html#faq-bash>`__

.. tabs::

   .. tab:: At APS

      On an APS machine with access to APSshare,
      run this command from a terminal session:

      .. raw:: html

         <pre>
         $ <b>source /APSshare/miniconda/x86_64/bin/activate</b>
         </pre>

      If you are getting an error, contact the Bluesky support team.

   .. tab:: Not at APS

      On a workstations with no access to APSshare, type the following command:

      .. raw:: html

         <pre>
         $ <b>which conda</b>
         </pre>

      If the output prints the path to conda, you can activate it by using:

      .. raw:: html

         <pre>
         $ <b>source /PATH/TO/CONDA/bin/activate</b>
         </pre>
         
      However, if the command ``which conda`` does not return anything, or if
      you are getting an error message (``bash: conda: command not found`` or
      ``bash: activate: No such file or directory``), conda is not installed on
      your computer or it is not added to the system's ``PATH`` environment
      variable.

      You can install conda by following the installation instructions for your
      operating system. You can find the instructions for Windows, macOS, and
      Linux on the official conda documentation `website
      <https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>`__.
      Note: Alternatively, you can install `miniconda
      <https://docs.conda.io/en/latest/miniconda.html>`__, an ideal base
      environment since it installs a minimal suite of Python packages, useful
      only the most basic tasks, such as creating local environments for
      user. 

      If you still encounter the same error message after installing conda or
      miniconda, you may need to add the conda installation directory to your
      system's ``PATH`` environment variable manually. You can find instructions
      on how to do this in the `conda documentation
      <https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>`__.



When ``conda`` is activated, the prompt changes to displays ``(base)``. Now you
can use ``conda env list`` to see the environments you have and the directories
in which they are installed.


.. raw:: html

   <pre>
   $ <b>conda env list</b>
   # conda environments:
   #
   bluesky_2022_3           /home/prjemian/.conda/envs/bluesky_2022_3
   bluesky_2023_1        *  /home/prjemian/.conda/envs/bluesky_2023_1
   base                     /opt/miniconda3
   </pre>

   The environment with the `*` is the active one.  The full command prompt (not
   shown here) will also be prefixed with the environment name, such as
   `(bluesky_2023_1) `.



Install the bluesky environment
-------------------------------

Here's an example for the ``bluesky_2023_2`` environment:

.. raw:: html

    <pre>
    $ <b>cd ~/bluesky</b>
    $ <b>conda env create \
        --force \
        -n bluesky_2023_2 \
        -f ./environments/environment_2023_2.yml \
        --solver=libmamba</b>
    </pre>

The above commands install the ``bluesky_2023_2`` environment inside the
``bluesky`` directory  that was created when installing a new bluesky instrument
(see `setup a bluesky instrument
<https://bcda-aps.github.io/bluesky_training/instrument/_install_new_instrument.html#setup-a-bluesky-instrument>`__).

Note that the installation takes several minutes. 

.. raw:: html

    <details>
    In the commands above, a long command has been split over several lines to make
    it clearer to read and also to take less screen width. We could enter the
    <code>conda env</code> command all one one line.  These commands work the same
    as the one above.

    <pre>
    $ <b>cd ~/bluesky</b>
    $ <b>conda env create --force -n bluesky_2023_2 -f ./environments/environment_2023_2.yml --solver=libmamba</b>
    </pre>

    </details>


Create an alias to activate the bluesky environment
---------------------------------------------------

Creating a bash alias is like creating a custom shortcut. You can do this by
editing the ``~/.bashrc`` and  ``~/.bashrc_aliases`` files, which are
configuration files for your bash shell. Here's a simple step-by-step guide:

.. raw:: html

   <ol>
   <li>Open a terminal.</li>
   <li>Open the <code>~/.bashrc</code> and <code>~/.bashrc_aliases</code> files with your prefered text editor, 
   <i>e.g.</i>:
   <pre>
   $ <b> gedit ~/.bashrc ~/.bashrc_aliases </b>
   </pre>
   If any of those files do not exist, this command will create blank ones. 
   </li>
   <li> In <code>~/.bashrc</code>, scroll down to the end of the file or find 
   a suitable place to add the following lines:
   <pre><b> 
   export BLUESKY_CONDA_ENV=bluesky_2023_2
   source ~/.bashrc_aliases
   </b> </pre>
   <b>Note:</b> those lines may already be included in your <code>~/.bashrc</code>,
   <i>e.g.</i>, if you have created an alias to start a bluesky session.
   </li>
   <li>In <code>~/.bashrc_aliases</code>, scroll down to the end of the file or find 
   a suitable place to add your alias. 
   On a new line, type:
   <pre><b> 
   alias become_bluesky='conda activate ${BLUESKY_CONDA_ENV}'
   </b> </pre>
   </li>  
   <li>Save your changes.</li>
   <li>Type <code>bash</code> and press enter, or open a new terminal windows to
   make the new alias available.</li>

   </ol>
   You can now use the alias <code>become_bluesky</code> to activate the bluesky
   environment. 
