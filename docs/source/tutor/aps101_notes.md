# APS Bluesky 101

## Overview

<u>Note</u>: The following content are notes for the presenter, not the training itself.

The *APS Bluesky 101* class provides a basic, yet
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

<u>Note</u>: time spans are estimates

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

  - check that IOC is running: `caget gp:UPTIME` in terminal

- half-hour
  - start Jupyter lab: `blueskyStarter.sh lab`
  - Bluesky: Brief Introduction
    - Open file [_intro2bluesky.md](../reference/_intro2bluesky.md) with *Markdown preview* in Jupyter lab session
- hour - interactive notebooks
  - `hello_world.ipynb` notebook
  - `basic-motor-scaler-scan.ipynb` notebook
    - start caQtDM and view motor `gp:m1`: `start_caQtDM_gp` (in a new terminal tab)
    - Connect the motor
    - Connect the scaler
    - Prepare to scan
  - **Break**
- half-hour
  - First scan
  - discussion
  - Fix a few _problems_
- half-hour
  - Scan with a *different* counting time : _staging_
  - Custom plan with configurable count time
  - Discussion

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
- How to use [EPICS area detectors](https://areadetector.github.io)? ([setup](https://apstools.readthedocs.io/en/latest/examples/_ad__pilatus.html), [measure](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/locate_image_peak.ipynb), [analyze from `databroker`](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/bluesky/databroker_analysis.ipynb))
- How to support complex [devices](https://blueskyproject.io/ophyd/tutorials/device.html?highlight=device)?
- How does [`databroker`](https://blueskyproject.io/databroker/) store the data?
- What is [MongoDB](https://www.mongodb.com/)?
- [How to execute Linux command from Bluesky?](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/demo_doodle.ipynb)
- [How to setup and use a diffractometer with Bluesky?](https://blueskyproject.io/hklpy/examples/index.html)

## Reference

Links to the videos from the training sessions of 2021 August and September are publicly-available on Box.com: https://anl.box.com/s/5ovic1hhoxrek9as0idawy61z9a32n4l

### Community

- APS Bluesky Office Hours
  - [every Wednesday, 2:00-3:00 pm](https://teams.microsoft.com/l/meetup-join/19%3ameeting_MzJjNGY5MTktOTRhZC00YmM4LThkMWMtOTJjMTYwYWU5ZGI2%40thread.v2/0?context=%7b%22Tid%22%3a%220cfca185-25f7-49e3-8ae7-704d5326e285%22%2c%22Oid%22%3a%22cd8e408e-f2c5-4590-937e-df9d934296ad%22%7d)
- [APS Teams channel for Bluesky](https://teams.microsoft.com/l/channel/19%3af9523bff12844888b25bd7d49a5fad56%40thread.skype/Bluesky?groupId=334721bd-e27f-4663-add0-9941fb4e98e8&tenantId=0cfca185-25f7-49e3-8ae7-704d5326e285)
- [Bluesky community chat on Slack](https://nikea.slack.com)
- [NSLS-II/DAMA open Q&A on Gitter](https://gitter.im/NSLS-II/DAMA)

### Information

- [Bluesky tutorials](https://blueskyproject.io/tutorials/README.html)
- [References from Bluesky Tutorials](https://blueskyproject.io/tutorials/README.html#references)
- [Jupyter Lab](https://jupyterlab.readthedocs.io)
- [EPICS](https://epics-controls.org/) ([old web site](https://epics.anl.gov/))
- [More on `EpicsSignal`](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_training/blob/main/connect_epics.ipynb) including `ophyd.Device`
- For more about Juypter, see the Bluesky [Hello Python and Jupyter](https://blueskyproject.io/tutorials/Hello%20Python%20and%20Jupyter.html) Tutorial.
