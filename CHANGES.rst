..
   Subsections could include these headings (in this order).
   Only include a subsection if there is content.

   Notice
   Breaking Changes
   New Features
   Enhancements
   Fixes
   Maintenance
   Deprecations
   Known Problems
   New Contributors

Changes
#######

History of user-visible changes between the versions.

Project `milestones <https://github.com/BCDA-APS/bluesky_training/milestones>`_
describe future plans.

..
   1.0.2
   ******

   release expected by 2023-12-31

   New Features
   ------------

   * Add package(s) to environment:

      * haven-spc


1.0.1
******

release expected by 2023-08-31

Breaking Changes
------------------------

* Move older environment files into archive subdirectory.

New Features
------------

* Add packages to environment:
   * bluesky-httpserver
   * bluesky-kafka
   * bluesky-live
   * httpie

* Documentation

  * Git advice for the reference section.
  * How to get the conda command?
  * Use "zlib" as default HDF5 compression.
  * Use Sphinx :download: role.
  * Use Sphinx tab sections for instructions with alternatives.

* Add ``iconfig`` dictionary to routine metadata.

* ``iconfig.yml``

  * Add ICONFIG_VERSION string.
  * EPICS PV for scan_id.
  * Use RUN_ENGINE_SCAN_ID_PV if defined in iconfig.yml file.

* ``new_bluesky_instrument.py``

  * Adds/updates tag version in ``iconfig.yml`` file.
  * Downloads most recent release of repo.
  * Easier to download.

Fixes
------------

* Fix bad formatting of Jupyter notebook cells.
* libmamba installed before it is used now

Maintenance
------------

* Environment for bluesky_2023_3.

1.0.0
******

Released 2023-06-05.

Notice
------

* Initial tag
