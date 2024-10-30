.. _reference.create_bluesky_enviroment:

Create bluesky environment
==========================

Describes the steps to create a virtual environment for a bluesky
:doc:`/instrument/index`.

A bluesky instrument uses many Python packages not included in the Python
Standard Library. Rather than add these directly into the system Python
installation, it is recommended to create a Python virtual environment which has
the suite of packages (and specific versions) required.

.. raw:: html

    <details>
    <summary>More about conda virtual environments</summary>

    A virtual environment gives you control over the suite of installed
    packages and insulates you from any system software updates. It is likely
    that you will have more than one conda environment available.  Each of these
    has a complete installation of Python with a suite of packages.  The suite
    may differ between the environments, as well as the package versions. Even
    the Python version itself may be different.

    <ul>
    <li>Each conda environment has a name, which corresponds to the file
      directory in which the environment's packages, libraries, and other
      resources are stored. </li>
    <li>When you install or update package(s) in one environment, this will not
      affect any of the other environments. This makes it easy to control
      which software is installed.</li>
    </ul>

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

    <details>
    <summary>Why conda?</summary>

    Here, we describe the creation of a Python virtual environment managed by
    <code>conda</code>. While opinions may vary, we see some advantages to using
    <code>conda</code> over <a
    hrf="https://docs.python.org/3/library/venv.html">venv</a>. Consequently, we
    use <code>conda</code> to install most packages, falling back to
    <code>pip</code> to install any remaining packages. We use  <a
    hrf="https://yaml.org/">YAML</a> files to describe these conda environments.
    See this <a
    hrf="https://medium.com/@balance1150/how-to-build-a-conda-environment-through-a-yaml-file-db185acf5d22">article</a>
    for more instruction about conda environment YAML files.
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
      user. For Linux, the recommended installation is described in details below:

      .. raw:: html

         <details>
         <summary>Recommended Miniconda installation for Linux</summary>

         To prevent users from modifying the conda base environment by accident,
         it is recommanded to install it as read-only. This can be achieved by
         installing miniconda with <i>elevated privileges</i> (this type of account
         refers to a user account that has administrative rights, also known as
         the <b>root</b> account or the <b>superuser</b> account).<br>
         The installation steps are described in the following bash script:

         <pre><code class="language-bash">
         # pick the installer script
         INSTALLER=Miniconda3-latest-Linux-x86_64.sh
         # INSTALLER=Miniconda3-py310_23.3.1-0-Linux-x86_64.sh

         # pick the installation location for your system
         # INSTALL_DIR=/opt/miniconda3
         INSTALL_DIR=/APSshare/miniconda/x86_64

         # download the installer script
         wget "https://repo.anaconda.com/miniconda/${INSTALLER}"

         # install Miniconda
         bash ${INSTALLER} -b -p "${INSTALL_DIR}"

         # install libmamba, mamba, & micromamba
         source "${INSTALL_DIR}/bin/activate"
         conda update -y -n base conda
         conda install -y -n base conda-libmamba-solver
         # conda install -y -n base -c conda-forge mamba --solver=libmamba
         conda install -y -n base -c conda-forge micromamba --solver=libmamba

         # set some defaults (can override in local settings)
         CONFIG_FILE="${INSTALL_DIR}/condarc"
         echo "channels:" > "${CONFIG_FILE}"
         echo "  - defaults" >> "${CONFIG_FILE}"
         echo "  - conda-forge" >> "${CONFIG_FILE}"
         echo "  - apsu" >> "${CONFIG_FILE}"
         echo "  - aps-anl-tag" >> "${CONFIG_FILE}"
         echo "channel_priority: flexible" >> "${CONFIG_FILE}"
         echo "solver: libmamba" >> "${CONFIG_FILE}"

         # update ~/.bashrc to activate base environment on login
         conda init
         </code></pre>

         </details>
         <br />


      If you still encounter the same error message after installing conda or
      miniconda, you may need to add the conda installation directory to your
      system's ``PATH`` environment variable manually. You can find instructions
      on how to do this in the `conda documentation
      <https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>`__.



When ``conda`` is activated, the prompt changes to display ``(base)``. Now you
can use ``conda env list`` to see the environments you have and the directories
in which they are installed.


.. raw:: html

   <pre>
   $ <b>conda env list</b>
   # conda environments:
   #
   bluesky_2022_2           /home/username/.conda/envs/bluesky_2022_2
   bluesky_2022_3           /home/username/.conda/envs/bluesky_2022_3
   bluesky_2023_1           /home/username/.conda/envs/bluesky_2023_1
   base                  *  /opt/miniconda3
   </pre>



The environment with the ``*`` is the active one. The command
prompt is also prefixed with the environment name, as mentioned above.



.. raw:: html

    <details>
    <summary>conda channels</summary>

    Channel refers to a repository or a source from which Conda packages can be
    downloaded and installed. To see your default channels:

    <pre>
    $ <b>conda config --show channels</b>
    </pre>

    To add more channels:

    <pre>
    $ <b>conda config --env --append channels conda-forge </b>
    $ <b>conda config --env --append channels apsu</b>
    </pre>

    When you use Conda to install a package, it will search for the package in
    the specified channel or channels. If the package is found, Conda will
    download and install it along with its dependencies. By default, Conda will
    search for packages in the default channels, but you can also specify
    additional channels to search in using the <code>-c</code> or
    <code>--channel</code> option when using the conda install command.

    </details>


    <details>
    <summary>libmamba solver</summary>

    In 2022, a <a
    href="https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community">significant
    performance enhancement</a> was made available to conda by inclusion of the
    <a
    href="https://conda.github.io/conda-libmamba-solver/">conda-libmamba-solver</a>
    package. If you have installed miniconda using the instructions for Linux
    above, this package is already installed and configured as the default solver.

    You can check your default solver with the following command:

    <pre>
    $ <b>conda config --show solver</b>
    </pre>

    If the above command returns <code>classic</code>, follow those steps:

    <ul>
    <li>Install the libmamba solver:</li>
    <pre>
    $ <b>conda install -c conda-forge libmamba</b>
    </pre>
    <li>Set libmamba as the default solver:</li>
    <pre>
    $ <b>conda config --set solver libmamba</b>
    </pre>
    <li>Confirm libmanda is now your default solver:</li>
    <pre>
    $ <b>conda config --show solver</b>
    </pre>
    </ul>

    </details>




Install the bluesky environment
-------------------------------

The following commands install the ``bluesky_2023_3`` environment inside the
``bluesky`` directory  that was created when installing a new bluesky instrument
(see `setup a bluesky instrument
<https://bcda-aps.github.io/bluesky_training/instrument/_install_new_instrument.html#setup-a-bluesky-instrument>`__).

.. hint:: Software requirements evolve.  Use the newest ``environment*.yml``
   file in the ``environments/`` directory.  This command gives a directory
   listing in chronological order:

   .. raw:: html

      <pre>
      $ <b>ls -larth /environments/environment*.yml</b>
      </pre>

Note that the installation takes several minutes.

.. raw:: html

    <pre>
    $ <b>cd ~/bluesky</b>
    $ <b>conda env create \
        -y \
        -n bluesky_2023_3 \
        -f ./environments/environment_2023_3.yml \
        --solver=libmamba</b>
    </pre>

    <details><summary>Details</summary>
    
    <ul> 
    <li>The <code>-y</code> option will replace any existing environment by this
    name without asking for confirmation. Remove this option if you wish.</li>
    <li>The <code>-n bluesky_2023_3</code> sets the name of the conda environment to be
    created.</li>
    <li>The <code>-f ./environments/environment_2023_3.yml</code> option names the
    YAML file to be used. We create different versions of the YAML file, named
    for the APS operating cycle (2021-1, 2023-2, …), as the suite of packages
    for a working installation may change over time. By keeping all these files
    in the environments subdirectory, we can restore any of these environments
    with a simple command.</li>
    <li>The <code>--solver=libmamba</code> option will use the conda-libmamba-solver.
    The <code>--solver</code> option can be removed but its use results in a much
    faster installation of the bluesky environment. The <code>libmamba</code> installation
    is described in the previous section.</li>
    </ul>

    </details>



Once finished, the installer will report the commands to manage the new environment:

.. raw:: html

    <pre>
    #
    # To activate this environment, use
    #
    #     $ conda activate bluesky_2023_3
    #
    # To deactivate an active environment, use
    #
    #     $ conda deactivate
    </pre>


.. _reference.create_conda-bluesky_alias:

Create an alias to activate the bluesky environment
---------------------------------------------------

Creating a bash alias, an optional step, is like creating a custom shortcut. You
can do this by editing the ``~/.bashrc`` and  ``~/.bash_aliases`` files, which
are configuration files for your bash shell. Here's a simple step-by-step guide:

.. raw:: html

   <ol>
   <li>Open a terminal.</li>
   <li>Open the <code>~/.bashrc</code> and <code>~/.bash_aliases</code> files with your prefered text editor,
   <i>e.g.</i>:
   <pre>
   $ <b> gedit ~/.bashrc ~/.bash_aliases </b>
   </pre>
   If any of those files do not exist, this command will create blank ones.
   </li>
   <li> In <code>~/.bashrc</code>, scroll down to the end of the file or find
   a suitable place to add the following lines:
   <pre>
   source ~/.bash_aliases
   </pre>
   <b>Note:</b> this line may already be included in your <code>~/.bashrc</code>.
   </li>
   <li>In <code>~/.bash_aliases</code>, scroll down to the end of the file or find
   a suitable place to add your alias.
   On a new line, type:
   <pre>
   export BLUESKY_CONDA_ENV=bluesky_2023_3
   alias become_bluesky='conda activate ${BLUESKY_CONDA_ENV}'
   </pre>
   </li>
   <li>Save your changes.</li>
   <li>Type <code>bash</code> and press enter, or open a new terminal windows to
   make the new alias available.</li>

   </ol>
   You can now use the alias <code>become_bluesky</code> to activate the bluesky
   environment.




Other reading
-------------

   - `Getting started with conda <https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html>`__
   - `conda environments - User Guide <https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html>`__
   - `conda environments - Independent Guide <https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533>`__
   - `conda cheat sheet <https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf>`__
   - `Managing conda environments <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`__
   - `difference between base environment and no environment at all <https://stackoverflow.com/questions/55134440/in-conda-what-is-the-differece-between-base-environment-and-no-environment-at>`__
   -  ``venv``:  `Python virtual environments <https://realpython.com/python-virtual-environments-a-primer/>`__
   - `micromamba environments <https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html>`__
