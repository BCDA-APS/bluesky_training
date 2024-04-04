APS Bluesky Training
====================

.. for documentation authors:
   Documentation may be created in restructured text (.rst), markdown (.md)
   of Jupyter notebooks (.ipynb).  Add new documents to the appropriate folder
   (howto, instrument, reference, tutor).  Start the file name with a leading
   `_` (underline) so that it will be included automatically.  The select few
   files which do not start with a "_" are added explicitly to the toctree in
   the `index.rst` file of that folder.

This APS Bluesky Training repository demonstrates use of the Bluesky framework
at a typical APS beamline.  Documentation is categorized in major sections.

.. icons: https://fonts.google.com/icons

.. grid:: 2

    .. grid-item-card:: :material-regular:`alt_route;3em`
      :link: howto/index
      :link-type: doc

      :ref:`howto`

      Practical guides for accomplishing specific tasks.

      .. rubric:: :ref:`examples`

      Demonstrations of specific tasks.

    .. grid-item-card::  :material-regular:`precision_manufacturing;3em`

      :ref:`instrument`

      Details to configure and develop your *instrument* package.

      .. rubric:: `Template <https://github.com/BCDA-APS/bluesky_training/tree/main/bluesky>`_

      The ``bluesky/`` `directory
      <https://github.com/BCDA-APS/bluesky_training/tree/main/bluesky>`_ is the
      template for new beamline :ref:`installations <checklist>`.

    .. grid-item-card:: :material-regular:`school;3em`
      :link: tutor/index
      :link-type: doc

      :ref:`tutorials`

      Step-by-step guides to help you get started and learn through doing.

    .. grid-item-card:: :material-regular:`collections_bookmark;3em`
      :link: reference/index
      :link-type: doc

      :ref:`reference`

      More ways to learn more about Bluesky.

.. toctree::
   :maxdepth: 1
   :hidden:

   howto/index
   instrument/index
   example/index
   tutor/index
   reference/index
   changes

About
-----

:home: https://bcda-aps.github.io/bluesky_training/
:source: https://github.com/bcda-aps/bluesky_training
:published: |today|
:revisions: :ref:`History of code changes <changes>`
:index: :ref:`genindex`

.. * :ref:`modindex`
.. * :ref:`search`
