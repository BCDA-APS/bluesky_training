# APS Bluesky 101

- [APS Bluesky 101](#aps-bluesky-101)
  - [Overview](#overview)
  - [Syllabus](#syllabus)
  - [Before the class](#before-the-class)
  - [Covered here](#covered-here)
  - [Not covered here](#not-covered-here)
  - [Reference](#reference)

## Overview

The *APS Bluesky 101* class is the first in a series, providing a basic, yet
hands-on, introduction to using the [Bluesky framework](https://blueskyproject.io).

The class should take (roughly) about 3 hours.  The first hour will cover
from the *Welcome* through the *Jupyter Lab* section.  The remaining time
will be spent on the *Connect with EPICS and scan with Bluesky* section.

The Linux Virtual Machine provides a complete, self-contained system with all
software installed, similar to what is used for scientific measurements with
an APS instrument, includes Bluesky software, EPICS client tools (both command
line and GUI), IOCs for area detector and general purpose work, web browsers,
graphical text editors, MongoDB database server, and Python infrastructure.

## Syllabus

note: time spans are estimates

- half-hour
  - Welcome
  - Check VMs are working
    - spot check (should check _before_ class to fix problems) or follow as observer
  - apply software updates & patches:
    
    ```sh
    cd ~/training
    git stash
    git pull
    bash ./patch1.sh
    cd ~/
    ```

- half-hour
  - start Jupyter lab: `blueskyStarter.sh lab`
  - run `hello_world.ipynb` notebook
  - Challenges and Discussion
- half-hour -  `basic-motor-scaler-scan.ipynb` notebook
  - Connect the motor
  - Connect the scaler
  - Prepare to scan
  - break
- half-hour
    - First scan
    - discussion
- half-hour
  - Fix a few _problems_
  - Scan with a *different* counting time : _staging_
  - Custom plan with configurable count time
- half-hour
  - Challenges and Discussion

## Before the class

- (required) [**Install the Virtual Machine**](https://github.com/BCDA-APS/epics-bluesky-vm/blob/main/install_vm.md) on your workstation if you are permitted to install software on your computer.
  - If you cannot install and run the VM, you can attend the course as
    an observer or view the video later.  A link to the video will be provided
    once it becomes available.
- (helpful) Read the [VM Overview](https://github.com/BCDA-APS/epics-bluesky-vm/blob/main/README.md#about-this-vm) and the [EPICS hardware simulations provided](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/describe_instrument.ipynb#Description).
- (helpful) Have a basic understanding of [running programs in Linux](https://maker.pro/linux/tutorial/basic-linux-commands-for-beginners).
- (helpful) [Basic understanding of programming Python.](https://www.python.org/about/gettingstarted/)

## Covered here

- The core parts of the [Bluesky](https://blueskyproject.io) Framework
- Start [Jupyter](https://jupyter.org/) [Lab](https://jupyterlab.readthedocs.io) (in web browser) for Bluesky sessions
- Connect with [EPICS](https://epics-controls.org/) (in the VM)
- Setup and scan scaler _v._ motor using the `bluesky.RunEngine` and `databroker.catalog`

## Not covered here

- How is Bluesky deployed at the APS? (hint: This class provides an example.)
- Are there other tutorials available online?  [Yes!](https://blueskyproject.io/tutorials/README.html)
- [How to access data from previous measurements?](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/after_measurement.ipynb)
- [How to plot data from previous scans?](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/plot_x_y_databroker.ipynb)
- [How to send data to users?](https://github.com/BCDA-APS/bluesky_training/blob/main/resources/example-data/README.md)
- How to use [EPICS area detectors](https://areadetector.github.io)? ([setup](https://apstools.readthedocs.io/en/latest/examples/_ad__pilatus.html), [measure](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/locate_image_peak.ipynb), [analyze from `databroker`](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/bluesky/databroker_analysis.ipynb))
- How to support complex [devices](https://blueskyproject.io/ophyd/tutorials/device.html?highlight=device)?
- How does [`databroker`](https://blueskyproject.io/databroker/) store the data?
- What is [MongoDB](https://www.mongodb.com/)?
- [How to execute Linux command from Bluesky?](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/demo_doodle.ipynb)
- [How to setup and use a diffractometer with Bluesky?](https://blueskyproject.io/hklpy/examples/index.html)

## Reference

- [Nice list](https://blueskyproject.io/tutorials/README.html#references)
- [Bluesky tutorials](https://blueskyproject.io/tutorials/README.html)
- [Jupyter Lab](https://jupyterlab.readthedocs.io)
- [EPICS](https://epics-controls.org/) ([old web site](https://epics.anl.gov/))
- [More on `EpicsSignal`](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/connect_epics.ipynb) including `ophyd.Device`
- For more about Juypter, see the Bluesky [Hello Python and Jupyter](https://blueskyproject.io/tutorials/Hello%20Python%20and%20Jupyter.html) Tutorial.
