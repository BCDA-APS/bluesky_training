.. _instrument.start_version_control:

Start software version control
------------------------------

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
