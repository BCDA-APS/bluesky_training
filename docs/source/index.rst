APS Bluesky Training
====================

-  Wiki (`<https://github.com/BCDA-APS/bluesky_training/wiki>`_):
   Includes list of APS instruments
-  `Installation Guide <instrument/_install.md>`__: 
   Install the components of the Bluesky framework.
-  `First Steps Guide <howto/__first_steps_guide.md>`__ :
   First Steps to use Bluesky after installation.
-  `Instrument Package Guide <instrument/guide.md>`__: 
   Building the ``instrument`` package.
-  :ref:`tutorials`: 
   Jupyter notebooks with lessons, tutorials, examples, other

**Other resources**

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
   * PyPI: https://pypi.org/project/pyepics/
   * source: https://github.com/pyepics/pyepics

TODO:  Consider adding highlighting certain docs.

.. code::

   Introductory
      Bluesky Hello, World!
      Connect with EPICS
      APS 101
   Basic hardware configuration and measurement
      scaler
      motor
      step scan
   Measurement using the instrument package
      area detector
      count a scaler
      watch a temperature
      lineup 1-D peak
      locate 2-D peak on area detector image
      custom bluesky plans
      bluesky for SPEC users
   After the measurement: processing, reduction, analysis, export or copy data
   Training
   Instrument template
   Conda
   Version control
   References

* https://stackoverflow.com/questions/42843288/is-there-any-way-to-make-markdown-tables-sortable
* https://diataxis.fr/

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   howto/index
   tutor/index
   instrument/index
   reference/index

.. useless, so far:
   Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`