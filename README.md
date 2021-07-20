# README.md

This repository, via [Jupyter](https://jupyter.org/) notebooks, demonstrates use
of the Bluesky framework at a typical beam line scenario for a BCDA-sponsored
class.

## Notebooks

Jupyter notebooks are used to document Bluesky-related activites and provide
documentation.

### Introductory

* [Bluesky *Hello, World!*](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/hello_world.ipynb)
* [Command Review](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/command_review.ipynb)
* [Overview of the `instrument` package](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/describe_instrument.ipynb)

### Measurement

Includes hardware configuration and custom measurement plans, in addition to measurement activities.

* [Custom bluesky plan](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/custom_plan.ipynb)
* [Count the scaler](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/count_scaler.ipynb)
* [Lineup a 1-D peak](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/lineup_1d_peak.ipynb)
* [Locate peak on 2-D area detector image](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/locate_image_peak.ipynb)
* [Watch a temperature](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/watch_temperature.ipynb)

### Analysis

* [Access data later, after the measurement](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/after_measurement.ipynb)
* [Analyze 2-D data on Windows workstation](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/resources/example-data/demonstrate.ipynb)
* [Copy data to another workstation](/resources/example-data/README.md)
* [Databroker analysis of 2-D image](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/databroker_analysis.ipynb)


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
apstools | https://apstools.readthedocs.io/
APS instruments | https://github.com/BCDA-APS/use_bluesky/wiki/
