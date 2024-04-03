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
at a typical APS beamline.  The repository ``bluesky/`` directory also serves as
a template for new beamline installations.

Documentation is categorized in four major sections. In addition to these
highlights, additional content is available in each section of the
documentation.

.. grid:: 2

    .. grid-item-card:: :ref:`howto`

      Practical guides for accomplishing specific tasks.

      -  `Bluesky Cheat Sheet <howto/bluesky_cheat_sheet.md>`_:
         First Steps to use Bluesky after installation.
      -  `Plot x, y data from a databroker run <howto/_plot_x_y_databroker.ipynb>`_
      -  `Working with data after the measurement <howto/_after_measurement.ipynb>`_

      .. rubric:: :ref:`examples`

      Demonstrations of specific tasks.

      - `XAFS scan <https://bcda-aps.github.io/bluesky_training/example/_xafs_scan.html>`_ :
        Example multi-segment XAFS scan.

    .. grid-item-card:: :ref:`instrument`

      Details to configure and develop your ``instrument`` package.

      -  `Installation Guide <instrument/_install_new_instrument.ipynb>`_:
         Install the components of the Bluesky framework.
      -  `Template <https://github.com/BCDA-APS/bluesky_training/tree/main/bluesky/instrument>`_
         for a bluesky ``instrument``
      -  `Instrument Package Guide <instrument/guide.md>`__:
         Building the ``instrument`` package.
      - `About the instrument package <instrument/describe_instrument.ipynb>`_

    .. grid-item-card:: :ref:`tutorials`

      Step-by-step guides to help you get started and learn through doing.

      - `Hello, World <tutor/hello_world.ipynb>`_
      - `Connect Bluesky with EPICS <tutor/connect_epics.ipynb>`_

    .. grid-item-card:: :ref:`reference`

      More ways to learn more about Bluesky.

      -  `bluesky training wiki <https://github.com/BCDA-APS/bluesky_training/wiki>`_:
         Includes list of APS instruments
      -  `General Bluesky Documentation (for APS) <https://wiki-ext.aps.anl.gov/blc/index.php?title=Controls_Software_Documentation#Bluesky>`_
      - `Other resources <reference/_zz_other_resources.rst>`_

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

:home: https://prjemian.github.io/pyQParamWidget/
:source: https://github.com/prjemian/pyQParamWidget
:published: |today|
:revisions: :ref:`History of code changes <changes>`
:index: :ref:`genindex`

.. * :ref:`modindex`
.. * :ref:`search`
