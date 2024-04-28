.. _instrument.setup_catalog_configuration:

Setup catalog configuration for databroker
------------------------------------------

Contact BCDA (bcda@aps.anl.gov) for assignment of a databroker catalog
configuration.  BCDA maintains a list of all assigned catalogs on a
`private server <https://git.aps.anl.gov/bcda/bluesky-catalogs/-/blob/master/README.md>`__

For example purposes, let's assume you have been given this
bluesky/databroker catalog assignment:

-  name: ``45ida_abcd``
-  MongoDB server: ``mongoserver.xray.aps.anl.gov``
-  MongoDB collection: ``45ida_abcd-bluesky``

See this `guide <https://bcda-aps.github.io/bluesky_training/instrument/_configure_databroker.html>`__ to configure databroker.

Confirm that databroker can find the ``45ida_abcd`` catalog by running
the python executable and passing the python commands as a command-line
option:

.. raw:: html

   <pre>
   $ <b>python -c "import databroker; print(list(databroker.catalog))"</b>
   ['45ida_abcd']
   </pre>
