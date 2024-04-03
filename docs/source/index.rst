APS Bluesky Training
====================

This APS Bluesky Training repository demonstrates use of the Bluesky
framework at a typical APS beamline.  Its ``bluesky/`` directory also
serves as a template for new beamline installations.

.. for documentation authors:
   Documentation may be created in restructured text (.rst), markdown (.md)
   of Jupyter notebooks (.ipynb).  Add new documents to the appropriate folder
   (howto, instrument, reference, tutor).  Start the file name with a leading
   `_` (underline) so that it will be included automatically.  The select few
   files which do not start with a "_" are added explicitly to the toctree in
   the `index.rst` file of that folder.

.. raw:: html

   <table style="border: 5px">
      <caption>
         Documentation is categorized in four major sections.
         <br />
         In addition to these highlights, additional content
         is available in each section of the documentation.
      </caption>
      <tr>
         <td style="width:40%; vertical-align:text-top; padding-bottom: 20px">
            <a href="howto/index.html"><b>How-to Guides</b></a>
            <br />
            Practical guides for accomplishing specific tasks.
            <ul>
               <li>
                  <a href="howto/bluesky_cheat_sheet.html">Bluesky Cheat Sheet</a>:
                  First Steps to use Bluesky after installation.
               </li>
               <li>
                  <a href="howto/_plot_x_y_databroker.html">
                     Plot x, y data from a databroker run
                  </a>
               </li>
               <li>
                  <a href="howto/_after_measurement.html">
                    Working with data after the measurement
                  </a>
               </li>
            </ul>
            <a href="example/index.html"><b>Examples</b></a>
            Demonstrations of specific tasks.
            <ul>
               <li>
                  <a href="example/_xafs_scan.html">XAFS scan</a>:
                  Example multi-segment XAFS scan.
               </li>
            </ul>
         </td>
         <td style="width:40%; vertical-align:text-top; padding-bottom: 10px">
            <a href="instrument/index.html"><b>Instrument</b></a>
            <br />
            Details to configure and develop your <em>instrument</em> package.
            <br />
            <ul>
               <li>
                  <a href="instrument/_install_new_instrument.html">Installation Guide</a>:
                  Install the components of the Bluesky framework.
               </li>
               <li>
                  <a href="https://github.com/BCDA-APS/bluesky_training/tree/main/bluesky/instrument">
                  Template
                  </a> for a bluesky <em>instrument</em> package.
               </li>
               <li>
                  <a href="instrument/guide.html">Instrument Package Guide</a>:
                  Building the <em>instrument</em> package.
               </li>
               <li>
                  <a href="instrument/describe_instrument.html">About the instrument package</a>
               </li>
            </ul>
         </td>
      </tr>
      <tr>
         <td style="width:40%; vertical-align:text-top; padding-bottom: 20px">
            <a href="tutor/index.html"><b>Tutorials and Lessons</b></a>
            <br />
            Step-by-step guides to help you get started and learn through doing.
            <ul>
               <li>
                  <a href="tutor/hello_world.html">Hello, World</a>
               </li>
               <li>
                  <a href="tutor/connect_epics.html">Connect Bluesky with EPICS</a>
               </li>
            </ul>
         </td>
         <td style="width:40%; vertical-align:text-top; padding-bottom: 20px">
            <a href="reference/index.html"><b>Reference</b></a>
            <br />
            Reference material to learn more about Bluesky.
            <ul>
               <li>
                  <a href="https://github.com/BCDA-APS/bluesky_training/wiki">
                  bluesky training wiki
                  </a>:
                  Includes list of APS instruments.
               </li>
               <li>
                  <a href="https://wiki-ext.aps.anl.gov/blc/index.php?title=Controls_Software_Documentation#Bluesky">
                  General Bluesky Documentation (for APS)
                  </a>
               </li>
               <li>
                  <a href="reference/_zz_other_resources.html">Other resources</a>
               </li>
            </ul>
         </td>
      </tr>
   </table>

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
