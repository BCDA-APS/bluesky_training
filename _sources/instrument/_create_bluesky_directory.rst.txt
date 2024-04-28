
.. _instrument.create_bluesky_directory:

Create bluesky directory
------------------------

Use the ``new_bluesky_instrument.py``
`program <https://github.com/BCDA-APS/bluesky_training/blob/main/new_bluesky_instrument.py>`__
to install a new bluesky instrument configuration from the online `APS
Bluesky Training <https://github.com/BCDA-APS/bluesky_training>`__
repository :index:`template`. The program creates a new ``bluesky`` directory in
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

      .. tip::  Needs outside network access at APS.

         Remember, since this will try to download content from the
         public internet, it only works from workstations with
         access to networks outside of APS.  From local private networks,
         it will stall in the first steps.

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

The installer program takes care of initializing a local git repository in the
``bluesky`` folder. Further instructions are provided :ref:`below
<instrument.start_version_control>` to create a remote reposititory.
