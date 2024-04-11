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
at a typical APS beamline.

.. icons: https://fonts.google.com/icons

.. grid:: 2

    .. grid-item-card:: :material-regular:`list_alt;3em` :ref:`instrument.install`

      Install a new ``bluesky`` directory and get started.

    .. grid-item-card:: :material-regular:`precision_manufacturing;3em` :ref:`instrument`

      Customize your control system with Bluesky.

    .. grid-item-card:: :material-regular:`straight;3em` :ref:`examples`

      Examples show the steps that demonstrate how something was done.

    .. grid-item-card:: :material-regular:`alt_route;3em` :ref:`howto`

      Practical guides for accomplishing specific tasks.

    .. grid-item-card:: :material-regular:`school;3em` :ref:`tutorials`

      Step-by-step guides to help you get started and learn through doing.

    .. grid-item-card::  :material-regular:`precision_manufacturing;3em` `Template <https://github.com/BCDA-APS/bluesky_training/tree/main/bluesky>`_

      The pristine model of your ``bluesky`` directory.

    .. grid-item-card:: :material-regular:`question_mark;3em` :ref:`FAQ`

      Some commonly-asked questions concerning Bluesky.

    .. grid-item-card:: :material-regular:`collections_bookmark;3em` :ref:`reference`

      Learn more about Bluesky.

.. toctree::
   :maxdepth: 1
   :hidden:

   instrument/index
   example/index
   howto/index
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
