.. index:: install; new instrument

.. _instrument.install:

Install New Instrument
======================

Describes the steps to install a new bluesky instrument.

.. note:: 2025-03-25.  The entire installation procedure is being redesigned.
    New repository (and documentation) are here: https://github.com/BCDA-APS/BITS
    Installation is described (for now) here: https://bcda-aps.github.io/BITS/install.html

.. note:: These *instructions have been written for workstations running the Linux operating system*. They may be used for other operating systems but expect some modifications are necessary. One such modification is that the ``libhkl`` library, needed for diffractometer support, is only available for Linux x86_64 host architectures.

.. warning:: In Linux, use the ``bash`` command shell. For more info see `what is bash? <https://bcda-aps.github.io/bluesky_training/reference/_FAQ.html#faq-bash>`__

.. _checklist:

Installation checklist
--------------------------

The *installation checklist* summarizes the steps with links
to the documentation for each step.

#. :ref:`instrument.create_bluesky_directory`
#. :ref:`reference.create_bluesky_enviroment`
#. (optional) :ref:`reference.configure_ipython_profile`
#. (optional) :ref:`reference.create_conda-bluesky_alias`
#. (optional) :ref:`instrument.test_initial_installation`
#. (optional) :ref:`instrument.create_starter_soft_link`
#. :ref:`instrument.setup_catalog_configuration`
#. (optional) :ref:`instrument.start_version_control`

Next steps ...
--------------

After the initial installation, it is time to configure the ``instrument``
package (*i.e.* content in the ``instrument/`` directory) for the details of
your hardware and experiments. See the
:ref:`instrument.configure_bluesky_instrument` section next.