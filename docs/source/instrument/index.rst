==========
Instrument
==========

The instrument package defines the features of your equipment for use with data
acquisition using the Bluesky framework.  It is structured as a Python package
[#package]_ so that it will be easy to use with the Python ``import`` command,
like much other Python software.

There are many ways to define your equipment so consider this guide as a
reference for ideas rather than a set of requirements.

.. TODO: Many of these documents need review

   instrument_package_guide.md.review_93
   README.md.review_93
      both: mostly copied to:
         _directory_layout.md
         _get_spec_config.md
         _test_it_works.md

.. toctree::
   :maxdepth: 2
   :glob:

   instrument_template
   describe_instrument
   guide
   _*

----

.. [#package] https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html
