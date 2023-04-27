APS Bluesky Training
====================

This repository demonstrates use of the Bluesky framework at a typical APS beam
line.

.. for documentation authors:
   Documentation may be created in restructured text (.rst), markdown (.md)
   of Jupyter notebooks (.ipynb).  Add new documents to the appropriate folder
   (howto, instrument, reference, tutor).  Start the file name with a leading
   `_` (underline) so that it will be included automatically.  The select few
   files which do not start with a "_" are added explicitly to the toctree in
   the `index.rst` file of that folder.

- :ref:`howto`
   -  `First Steps Guide <howto/first_steps_guide.md>`_:
      First Steps to use Bluesky after installation.
   -  `Plot x, y data from a databroker run <https://bcda-aps.github.io/bluesky_training/howto/_plot_x_y_databroker.html>`_
   -  `Working with data after the measurement <https://bcda-aps.github.io/bluesky_training/howto/_after_measurement.html>`_
- :ref:`instrument`
   -  `Installation Guide <https://bcda-aps.github.io/bluesky_training/instrument/_install_new_instrument.html>`_:
      Install the components of the Bluesky framework.
   -  `Template <https://github.com/BCDA-APS/bluesky_training/tree/main/bluesky/instrument>`_
      for a bluesky ``instrument``
   -  `Instrument Package Guide <instrument/guide.md>`__:
      Building the ``instrument`` package.
   - `About the instrument package <file:///home/prjemian/Documents/projects/BCDA-APS/bluesky_training/docs/build/html/instrument/describe_instrument.html>`_
- :ref:`examples`
   - `XAFS scan <https://bcda-aps.github.io/bluesky_training/example/_xafs_scan.html>`_ : Example multi-segment XAFS scan.
- :ref:`Tutorials and Lessons <tutorials>`
   - `Connect Bluesky with EPICS <https://bcda-aps.github.io/bluesky_training/tutor/connect_epics.html>`_
   - `Hello, World <https://bcda-aps.github.io/bluesky_training/instrument/_hello_world.html>`_
- :ref:`reference`
   -  `bluesky training wiki <https://github.com/BCDA-APS/bluesky_training/wiki>`_:
      Includes list of APS instruments
   -  `General Bluesky Documentation (for APS) <https://wiki-ext.aps.anl.gov/blc/index.php?title=Controls_Software_Documentation#Bluesky>`_

.. toctree::
   :maxdepth: 1
   :hidden:

   howto/index
   instrument/index
   example/index
   tutor/index
   reference/index

Other resources
==================

* apstools
   * home: https://bcda-aps.github.io/apstools/latest/
   * source: https://github.com/BCDA-APS/apstools
   * PyPI: https://pypi.org/project/apstools/
   * conda: https://anaconda.org/conda-forge/apstools
* Bluesky framework
   * home: https://blueskyproject.io
   * source: https://github.com/bluesky
   * conda: all packages available on conda-forge channel
* MongoDB
   * home: https://www.mongodb.com/
* PyDM
   * home: https://slaclab.github.io/pydm/
   * source: https://github.com/slaclab/pydm
   * PyPI: https://pypi.org/project/pydm/
   * conda: https://anaconda.org/conda-forge/pydm
* PyEPICS
   * home: https://pyepics.github.io/pyepics/
   * source: https://github.com/pyepics/pyepics
   * PyPI: https://pypi.org/project/pyepics/
   * conda: https://anaconda.org/conda-forge/pyepics

Index
==================

* :ref:`genindex`

.. * :ref:`modindex`
.. * :ref:`search`
