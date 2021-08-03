# README.md

This repository, via [Jupyter](https://jupyter.org/) notebooks, demonstrates use
of the Bluesky framework at a typical beam line scenario for a BCDA-sponsored
class.

## Notebooks

Jupyter notebooks are used to document Bluesky-related activites and provide
documentation.  They are gathered into sections by topic.  Within a section,
there is no particular order, except as numbered.

### Introductory

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

* [Run a Linux command as an `ophyd.Device`](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/demo_doodle.ipynb)

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

#### Data Movement

* [Copy data to another workstation](/resources/example-data/README.md)

### Review

* [Command Review](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/command_review.ipynb)
* [Overview of the `instrument` package](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/describe_instrument.ipynb)


## Installation

Instructions are available for [installation on Linux workstations](install.md).
The steps are similar on Mac OS and Windows but details are not provided here.

## References

name | URL
--- | ---
Bluesky Framework | https://blueskyproject.io/
bluesky | https://blueskyproject.io/bluesky
ophyd | https://blueskyproject.io/ophyd
databroker | https://blueskyproject.io/databroker
databroker-pack | https://blueskyproject.io/databroker-pack
apstools | https://apstools.readthedocs.io/
APS instruments | https://github.com/BCDA-APS/use_bluesky/wiki/
APS Data Management | https://confluence.aps.anl.gov/display/DMGT/Infrastructure
