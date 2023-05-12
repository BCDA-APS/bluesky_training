# README.md

This repository, via [Jupyter](https://jupyter.org/) notebooks, demonstrates use
of the Bluesky framework at a typical beam line scenario for a BCDA-sponsored
class.

Unit Tests | License | GH tag
--- | --- | ---
[![Unit Tests](https://github.com/BCDA-APS/bluesky_training/workflows/Unit%20Tests/badge.svg)](https://github.com/BCDA-APS/bluesky_training/actions/workflows/unit_tests.yml) | [![license: ANL](https://img.shields.io/badge/license-ANL-brightgreen)](/LICENSE.txt) | [![tag](https://img.shields.io/github/tag/BCDA-APS/bluesky_training.svg)](https://github.com/BCDA-APS/bluesky_training/tags)

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
  - [Introductory](#introductory)
  - [Basic hardware configuration and measurement](#basic-hardware-configuration-and-measurement)
    - [Hardware Configuration - Advanced](#hardware-configuration---advanced)
  - [Measurement using the `instrument` package](#measurement-using-the-instrument-package)
    - [Measurement - Advanced](#measurement---advanced)
  - [Post-measurement (such as Analysis)](#post-measurement-such-as-analysis)
    - [Data Processing, Reduction, and/or Analysis](#data-processing-reduction-andor-analysis)
  - [Review](#review)
  - [Install as Bluesky `instrument` package](#install-as-bluesky-instrument-package)

name | URL
--- | ---
Documentation | https://BCDA-APS.github.io/bluesky_training
Instrument template | https://github.com/BCDA-APS/bluesky_training/tree/main/bluesky/instrument
APS instruments | https://github.com/BCDA-APS/bluesky_training/wiki/
Bluesky Framework | https://blueskyproject.io/
bluesky | https://blueskyproject.io/bluesky
ophyd | https://blueskyproject.io/ophyd
databroker | https://blueskyproject.io/databroker
databroker-pack | https://blueskyproject.io/databroker-pack
apstools | https://BCDA-APS.github.io/apstools
APS Data Management | https://confluence.aps.anl.gov/display/DMGT/Infrastructure

## Introductory

The [APS Bluesky 101](https://bcda-aps.github.io/bluesky_training/tutor/aps101.html)
introductory course covers these two notebooks as well as scanning with scaler _v._ motor.

- [Bluesky *Hello, World!*](https://bcda-aps.github.io/bluesky_training/instrument/_hello_world.html)
- [Connect with EPICS](https://bcda-aps.github.io/bluesky_training/tutor/connect_epics.html)

## Basic hardware configuration and measurement

These notebooks demonstrate the basics of hardware configuration
([ophyd](https://blueskyproject.io/ophyd)) and custom measurement plans
([bluesky](https://blueskyproject.io/bluesky)), in addition to measurement
activities.

1. [scaler](https://bcda-aps.github.io/bluesky_training/tutor/_basic_a.html)
1. [motor](https://bcda-aps.github.io/bluesky_training/tutor/_basic_b.html)
1. [step scan](https://bcda-aps.github.io/bluesky_training/tutor/_basic_c.html)

### Hardware Configuration - Advanced

- [Run a Linux command as an `ophyd.Device`](https://bcda-aps.github.io/bluesky_training/howto/_doodle.html)
- [Store Images, Darks, and Flats frames separately in HDF5 files](https://bcda-aps.github.io/bluesky_training/howto/_images_darks_flats.html)

## Measurement using the `instrument` package

As the configuration of a system becomes more complex, it may be easier to
describe (and startup) by making the steps into Python package that can be
`import`ed.  These notebooks start with an `instrument` package that is
preconfigured to use the general purpose `gp:` IOC and the area detector `ad:`
IOC.

1. [Count the scaler](https://bcda-aps.github.io/bluesky_training/howto/_count_scaler.html)
1. [Watch a temperature](https://bcda-aps.github.io/bluesky_training/example/_watch_temperature.html)
1. [Lineup a 1-D peak](https://bcda-aps.github.io/bluesky_training/howto/_lineup_1d_peak.html)
1. [Locate peak on 2-D area detector image](https://bcda-aps.github.io/bluesky_training/howto/_locate_image_peak.html)
1. [Plot $(x,y)$ data from a databroker run](https://bcda-aps.github.io/bluesky_training/howto/_plot_x_y_databroker.html)
1. [Custom bluesky plan](https://bcda-aps.github.io/bluesky_training/howto/_custom_plan.html)

### Measurement - Advanced

- [Move 2 motors with dynamic limits](https://bcda-aps.github.io/bluesky_training/howto/_dynamic_limits_2motor.html)
  : EPICS : Demo of dynamic limit signal to avoid collision of two motors
- [XAFS scan, multi-segment](https://bcda-aps.github.io/bluesky_training/example/_xafs_scan.html)
  :  step scan (note: detector data is random numbers)

## Post-measurement (such as Analysis)

Typically, measurement data is sent to Bluesky's
[databroker](https://blueskyproject.io/databroker) package for storage in a
MongoDB database (or a structured set of folders) for access and analysis.
These notebooks use data recorded previously and stored in a structured set of
folders (created by tools from Bluesky's
[databroker-pack](https://blueskyproject.io/databroker-pack/) package.)

### Data Processing, Reduction, and/or Analysis

- [Access data later, after the measurement](https://bcda-aps.github.io/bluesky_training/howto/_after_measurement.html)
  using Data Broker
- [Analyze a 2-D image](https://bcda-aps.github.io/bluesky_training/howto/_locate_image_peak.html)
- [Plot $(x,y)$ data from a databroker run](https://bcda-aps.github.io/bluesky_training/howto/_plot_x_y_databroker.html)
  using Data Broker

## Review

- [Command Review](https://bcda-aps.github.io/bluesky_training/tutor/_command_review.html)
- [Overview of the `instrument` package](https://bcda-aps.github.io/bluesky_training/instrument/describe_instrument.html)

## Install as Bluesky `instrument` package

The [`bluesky`](https://github.com/BCDA-APS/bluesky_training/tree/main/bluesky)
directory of this [repository](https://github.com/BCDA-APS/bluesky_training)
serves as a template for creating a new bluesky `instrument` package.  See these
installation
[instructions](https://bcda-aps.github.io/bluesky_training/instrument/_install_new_instrument.html#setup-a-bluesky-instrument).
The process to install on Mac OS and Windows is similar but support for those
operating systems is not provided here.
