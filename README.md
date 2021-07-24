# README.md

This repository, via [Jupyter](https://jupyter.org/) notebooks, demonstrates use
of the Bluesky framework at a typical beam line scenario for a BCDA-sponsored
class.

## Notebooks

Jupyter notebooks are used to document Bluesky-related activites and provide
documentation.

### Introductory

* [Bluesky *Hello, World!*](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/hello_world.ipynb)
* [Connect with EPICS](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/connect_epics.ipynb)

### Measurement

Includes hardware configuration ([ophyd](https://blueskyproject.io/ophyd)) and
custom measurement plans ([bluesky](https://blueskyproject.io/bluesky)), in
addition to measurement activities.

* [Custom bluesky plan](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/custom_plan.ipynb)
* [Count the scaler](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/count_scaler.ipynb)
* [Lineup a 1-D peak](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/lineup_1d_peak.ipynb)
* [Locate peak on 2-D area detector image](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/locate_image_peak.ipynb)
* [Watch a temperature](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/watch_temperature.ipynb)
* [moving 2 motors with dynamic limits](demo_dynamic_limits_2motor.ipynb) - EPICS : Demo of dynamic limit signal to avoid collision of two motors
* [run a Linux command as an `ophyd.Device`](https://nbviewer.jupyter.org/github/BCDA-APS/use_bluesky/blob/main/lessons/linux_command_as_Device/demo_doodle.ipynb)

### Post-measurement (such as Analysis)

Typically, measurement data is sent to Bluesky's [databroker](https://blueskyproject.io/databroker) package for storage in a MongoDB
database (or a structured set of folders) for access and analysis.  These
notebooks use data recorded previously and stored in a structured
set of folders (created by tools from Bluesky's
[databroker-pack](https://blueskyproject.io/databroker-pack/) package.)

* [Access data later, after the measurement](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/after_measurement.ipynb) using Data Broker
* [Analyze a 2-D image using](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/databroker_analysis.ipynb) using Data Broker
* [Analyze 2-D data on Windows workstation](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/resources/example-data/demonstrate.ipynb)
* [Copy data to another workstation](/resources/example-data/README.md)
* [Plot (x,y) data from a run](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/plot_x_y_databroker.ipynb) using Data Broker

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
