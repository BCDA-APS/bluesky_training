.. index:: instrument package

.. _instrument:

==========
Instrument
==========

As the configuration of a system becomes more complex, it may be easier to
describe (and startup) by making the startup steps into a Python package for
`import`.

The ``instrument`` package defines the features of your equipment for use with
data acquisition using the Bluesky [#]_ framework.  It is
structured as a Python package [#]_ so that it will be easy to use with
the Python ``import`` command, like much other Python software.

There are many ways to define your equipment so consider this guide as a
reference for ideas rather than a set of requirements.

.. toctree::
   :maxdepth: 2
   :glob:

   describe_instrument
   guide
   _*

----

.. [#] https://blueskyproject.io/
.. [#] https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html
