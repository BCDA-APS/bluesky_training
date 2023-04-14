# README.md

This repository, via [Jupyter](https://jupyter.org/) notebooks, demonstrates use
of the Bluesky framework at a typical beam line scenario for a BCDA-sponsored
class.

<!-- consider this new structure

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

Also take note of

   * https://diataxis.fr/
   * https://stackoverflow.com/questions/42843288/is-there-any-way-to-make-markdown-tables-sortable
-->


- [README.md](#readmemd)
  - [Notebooks](#notebooks)
    - [Introductory](#introductory)
    - [Basic hardware configuration and measurement](#basic-hardware-configuration-and-measurement)
      - [Advanced](#advanced)
    - [Measurement using the `instrument` package](#measurement-using-the-instrument-package)
      - [Advanced](#advanced-1)
    - [Post-measurement (such as Analysis)](#post-measurement-such-as-analysis)
      - [Data Processing, Reduction, and/or Analysis](#data-processing-reduction-andor-analysis)
      - [Export, Copy Data](#export-copy-data)
    - [Review](#review)
  - [Installation](#installation)
    - [Install for Training](#install-for-training)
    - [Install as Bluesky `instrument` package](#install-as-bluesky-instrument-package)
  - [References](#references)


## Notebooks

Jupyter notebooks are used to document Bluesky-related activites and provide
documentation.  They are gathered into sections by topic.  Within a section,
there is no particular order, except as numbered.

### Introductory

The [APS Bluesky 101](APS_Bluesky_101.md) introductory course covers these two notebooks as well as scanning with scaler _v._ motor.

* [Bluesky *Hello, World!*](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/bluesky/hello_world.ipynb)
* [Connect with EPICS](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/connect_epics.ipynb)

### Basic hardware configuration and measurement

These notebooks demonstrate the basics of hardware configuration
([ophyd](https://blueskyproject.io/ophyd)) and custom measurement plans
([bluesky](https://blueskyproject.io/bluesky)), in addition to measurement
activities.

1. [scaler](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/basic_scaler.ipynb)
1. [motor](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/basic_motor.ipynb)
1. [step scan](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/basic_step_scan.ipynb)

#### Advanced

- [Run a Linux command as an `ophyd.Device`](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/demo_doodle.ipynb)
- [Store Images, Darks, and Flats frames separately in HDF5 files](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/images_darks_flats.ipynb)

### Measurement using the `instrument` package

As the configuration of a system becomes more complex, it may be easier to
describe (and startup) by making the steps into Python package that can be
`import`ed.  These notebooks start with an `instrument` package that is
preconfigured to use the general purpose `gp:` IOC and the area detector `ad:`
IOC.

1. [Count the scaler](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/count_scaler.ipynb)
1. [Watch a temperature](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/watch_temperature.ipynb)
1. [Lineup a 1-D peak](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/lineup_1d_peak.ipynb)
1. [Locate peak on 2-D area detector image](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/locate_image_peak.ipynb)

* [Custom bluesky plan](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/custom_plan.ipynb)

#### Advanced

* [Move 2 motors with dynamic limits](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/demo_dynamic_limits_2motor.ipynb) - EPICS : Demo of dynamic limit signal to avoid collision of two motors
* [XAFS scan, multi-segment](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/xafs_scan.ipynb) - step scan (note: detector data is random numbers)

### Post-measurement (such as Analysis)

Typically, measurement data is sent to Bluesky's
[databroker](https://blueskyproject.io/databroker) package for storage in a
MongoDB database (or a structured set of folders) for access and analysis.
These notebooks use data recorded previously and stored in a structured set of
folders (created by tools from Bluesky's
[databroker-pack](https://blueskyproject.io/databroker-pack/) package.)

#### Data Processing, Reduction, and/or Analysis

* [Access data later, after the measurement](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/after_measurement.ipynb) using Data Broker
* [Analyze a 2-D image](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/bluesky/databroker_analysis.ipynb) using Data Broker
* [Analyze a 2-D image on Windows workstation](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/resources/example-data/demonstrate.ipynb)
* [Plot (x,y) data from a run](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/plot_x_y_databroker.ipynb) using Data Broker

#### Export, Copy Data

* [Export data, overview](export-bluesky-data.md)
* [Export data to CSV](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/export-to-csv.ipynb)
* [Transfer data to another workstation](/resources/example-data/README.md)

### Review

* [Command Review](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/command_review.ipynb)
* [Overview of the `instrument` package](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/describe_instrument.ipynb)


## Installation

### Install for Training

Instructions are available for [installation on Linux workstations](install.md).
The steps are similar on Mac OS and Windows but details are not provided here.

### Install as Bluesky `instrument` package

Parts of this repository (under the `bluesky`) also serve as a template for
creating a new bluesky `instrument` package.  See these
[instructions](/resources/install_new_instrument.md) for the _Steps to install a
new instrument_.

## References

name | URL
--- | ---
Bluesky Framework | https://blueskyproject.io/
bluesky | https://blueskyproject.io/bluesky
ophyd | https://blueskyproject.io/ophyd
databroker | https://blueskyproject.io/databroker
databroker-pack | https://blueskyproject.io/databroker-pack
apstools | https://BCDA-APS.github.io/apstools
APS instruments | https://github.com/BCDA-APS/use_bluesky/wiki/
APS Data Management | https://confluence.aps.anl.gov/display/DMGT/Infrastructure
License | [![license: ANL](https://img.shields.io/badge/license-ANL-brightgreen)](LICENSE.txt)
