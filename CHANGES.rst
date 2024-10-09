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
    1.0.4
    ******

    release expected by 2024-12-31?

    Maintenance
    ------------

    * Change environment installation to prefer pip for most packages.

1.0.3
******

released 2024-06-13

New Features
------------

* Example of APS taxi/fly scans.

Fixes
-----

* Application new_bluesky_environment would crash when requests package not found.
* Function newSpecFile did not update scan_id in some cases.

Maintenance
------------

* Add environment file for 2024_2 cycle.
* Testing with Python 3.9, 3.10, 3.11.
* Make the home page less complex.
* Require Py3.9 or higher to run new_bluesky_environment application.

1.0.2
******

released 2024-02-26

New Features
------------

* Add options to instrument configuration (iconfig.yml):

  * After every run, verify that files were saved, print a confirmation message. 
  * Debugging and message options.

* Add package(s) to environment:

  * ophyd-registry

* Build ``oregistry`` of all ophyd objects.
* Post a warning if at APS but not on controls subnet.

Maintenance
------------

* Add 'Hello, World!' test to installation checklist.
* Drop the (unused now) *stdlogpj* package for configuring Python's *logging*.
* Environment for bluesky_2024_1.
* Lint the code (for style and syntax errors) using the 'ruff' package.
* Updates (learned from 2-ID) for new installations.
* Various documentation updates.

v1.0.1
******

Released 2023-08-22.

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

v1.0.0
******

Released 2023-06-05.

Notice
------

* Initial tag
