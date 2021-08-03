# APS Bluesky 101

- [APS Bluesky 101](#aps-bluesky-101)
  - [Overview](#overview)
  - [Before the class](#before-the-class)
  - [Covered here](#covered-here)
  - [Not covered here](#not-covered-here)
  - [Syllabus](#syllabus)

## Overview

The *APS Bluesky 101* class is the first in a series, providing a basic
introduction to using the [Bluesky
framework](https://blueskyproject.io).

The Linux Virtual Machine used to provide a complete system similar to
what is used at an APS beam line, includes Bluesky software, EPICS
client tools (both command line and GUI), IOCs for area detector and
general purpose work, web browsers, graphical text editors, MongoDB
database server, and Python infrastructure.

## Before the class

- (required) [**Install the Virtual Machine**](https://github.com/BCDA-APS/epics-bluesky-vm/blob/main/install_vm.md) on your workstation.
- (helpful) Read the [VM Overview](https://github.com/BCDA-APS/epics-bluesky-vm/blob/main/README.md#about-this-vm) and the [EPICS hardware simulations provided](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/describe_instrument.ipynb#Description).
- (helpful) Have a basic understanding of running programs in Linux.
- (helpful) Basic understanding of programming Python.

## Covered here

- The core parts of Bluesky
- Start Jupyter Lab (in web browser) for Bluesky sessions
- Connect with EPICS (in the VM)
- Setup and scan scaler _v._ motor using the Bluesky `RunEngine` and `databroker`

## Not covered here

- How is Bluesky deployed at the APS?
- [How to access data from previous measurements?](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/after_measurement.ipynb)
- [How to plot data from previous scans?](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/plot_x_y_databroker.ipynb)
- [How to send data to users?](https://github.com/BCDA-APS/bluesky_training/blob/main/resources/example-data/README.md)
- How to use EPICS area detectors? ([setup](https://apstools.readthedocs.io/en/latest/examples/_ad__pilatus.html), [measure](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/locate_image_peak.ipynb), [analyze from `databroker`](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/bluesky/databroker_analysis.ipynb))
- How to support complex devices?
- How does `databroker` store the data?
- What is MongoDB?
- [How to execute Linux command from Bluesky?](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/demo_doodle.ipynb)
- How to setup and use a diffractometer with Bluesky?

## Syllabus

- Bluesky 101
  - Command line:
    - has IOC started? `caget gp:datetime`
    - to restart IOCs: `start_iocs.sh`
    - start EPICS GUI: `start_caQtDM_gp`
  - Jupyter Lab
    - start Jupyter:
      1. `blueskyStarter.sh lab`
      2. web browser starts in ~30s
      3. opens in `bluesky` subdirectory
    - [*Hello World*](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/bluesky/hello_world.ipynb) and `ophyd.EpicsSignal`
  - Connect with EPICS
    - [Scan with motor and scaler](https://github.com/BCDA-APS/bluesky_training/blob/main/bluesky/basic-motor-scaler-scan.ipynb)
      - Connect the motor
      - Connection the scaler
      - Control the counting time
      - Prepare to scan
      - Standard scan with standard plan: `bluesky.plans.scan()`
      - Staging : Scan with _different_ counting time.
      - Custom scan _plan_ with configurable count time
