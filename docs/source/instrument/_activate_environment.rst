.. _instrument.activate_bluesky_conda_environment:

Activate the bluesky conda environment
--------------------------------------

.. note:: Consider merging with :ref:`reference.create_bluesky_enviroment`

.. TODO: instead of dropdown, make a paragraph that references the extra help page
   If you need to install a bluesky conda environment, see these instruction...
   See these instructions (link) if you need to create a bluesky conda environment.
   MAKE SURE THE TITLE names match.  Use :ref: anchors.

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

