# notebooks

This directory contains lessons, tutorials, examples, other - all in Jupyter notebooks

## Lessons & Demonstrations

LESSONS

* [lesson1](https://nbviewer.jupyter.org/github/BCDA-APS/use_bluesky/blob/main/lessons/lesson1.ipynb) - EPICS : scaler and count
* [lesson2](https://nbviewer.jupyter.org/github/BCDA-APS/use_bluesky/blob/main/lessons/lesson2.ipynb) - EPICS : motor and scan
* [lesson3](https://nbviewer.jupyter.org/github/BCDA-APS/use_bluesky/blob/main/lessons/lesson3.ipynb) - EPICS : show data as it is acquired
* [lesson3: final](https://nbviewer.jupyter.org/github/BCDA-APS/use_bluesky/blob/main/lessons/lesson3_final.ipynb) - EPICS : final project
* [lesson4](https://nbviewer.jupyter.org/github/BCDA-APS/use_bluesky/blob/main/lessons/lesson4.ipynb) - simulator : scan scaler v. motor
* [lesson5](https://nbviewer.jupyter.org/github/BCDA-APS/use_bluesky/blob/main/lessons/lesson5.ipynb) - simulator : find a peak and lineup on it
* [lesson5: advanced](https://nbviewer.jupyter.org/github/BCDA-APS/use_bluesky/blob/main/lessons/lesson5_advanced.ipynb) - simulator : *advanced* assignment
* [lesson6](https://nbviewer.jupyter.org/github/BCDA-APS/use_bluesky/blob/main/lessons/lesson6.ipynb) - EPICS : area detector
* [lesson7](https://nbviewer.jupyter.org/github/BCDA-APS/use_bluesky/blob/main/lessons/lesson7.ipynb) - simulator : four-circle diffractometer

DOCUMENTATION

* [Command Review](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_instrument_training/blob/main/command_review.ipynb) *a.k.a.* **The Cheat Sheet**
* [Overview of the `instrument` package](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_instrument_training/blob/main/describe_instrument.ipynb) - Recommended way to configure your instrument to work with Bluesky.
* [The `aps` device](basic_aps_info.ipynb) - EPICS : Basic information for beam lines from the APS accelerator

DEMONSTRATIONS

* [Analyze data from a run](https://nbviewer.jupyter.org/github/BCDA-APS/epics-bluesky-vm/blob/main/after_measurement.ipynb) (accessing the data from  databroker)
* [Area Detector Image Types](sandbox/images_darks_flats.ipynb) - EPICS : Images, Darks, & Flats with EPICS area detector, ophyd, and Bluesky
* [Copy data to another workstation](https://github.com/BCDA-APS/bluesky_instrument_training/blob/main/resources/example-data/README.md) using `databroker-pack`
* [Count the scaler](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_instrument_training/blob/main/count_scaler.ipynb) using ophyd, bluesky, and the *instrument* package
* [Custom bluesky plan](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_instrument_training/blob/main/custom_plan.ipynb) using bluesky and the *instrument* package
* [Databroker: **Pack** - Export a few runs to give to a user](https://github.com/BCDA-APS/epics-bluesky-vm/blob/main/external_data/README.md) (accessing the data from databroker)
* [Databroker: **Unpack** - Import a package of runs.](https://nbviewer.jupyter.org/github/BCDA-APS/epics-bluesky-vm/blob/main/external_data/unpack.ipynb) using databroker-pack
* [Databroker: Analyze a 2-D image](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_instrument_training/blob/main/databroker_analysis.ipynb) using databroker
* [Databroker: Plot (x,y) data from a run](https://nbviewer.jupyter.org/github/BCDA-APS/use_bluesky/blob/main/lessons/plot_x_y_databroker.ipynb) using databroker
* [Diffractometer examples](https://blueskyproject.io/hklpy/examples/index.html) using hklpy
* [dynamic limits with 2 motors](demo_dynamic_limits_2motor.ipynb) - EPICS : Demo of dynamic limit signal to avoid two motor collision
* [Lineup a 1-D peak](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_instrument_training/blob/main/lineup_1d_peak.ipynb) using ophyd, bluesky, and the *instrument* package
* [Locate peak on 2-D area detector image](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_instrument_training/blob/main/locate_image_peak.ipynb) using ophyd, bluesky, and the *instrument* package
* [ophyd: Interface with XY positioner written with pure Python (no EPICS) support](https://github.com/prjemian/2DMotorXY#readme) using `ophyd.SoftPositioner`
* [ophyd: run a Linux command as a Device](https://nbviewer.jupyter.org/github/BCDA-APS/use_bluesky/blob/main/lessons/linux_command_as_Device/demo_doodle.ipynb) using ophyd
* [Watch a temperature](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_instrument_training/blob/main/watch_temperature.ipynb) using ophyd, bluesky, and the *instrument* package

## Tips

* [Windows](windows.md) - Installing ophyd, Bluesky, *et al.* on Windows 10
* *Known* [supported browsers](https://github.com/jupyterlab/jupyterlab#prerequisites-and-supported-browsers) - [Firefox, Chrome, Safari](https://jupyterlab.readthedocs.io/en/latest/getting_started/installation.html#supported-browsers), KDE's Konqueror did not work

## Starting a Jupyter notebook session at APS

This session was started from the linux command line:

```
jemian@otz ~/Documents $ source /APSshare/anaconda3/Bluesky/bin/activate
(base) jemian@otz ~/Documents $ jupyter-notebook
```

This command produced the following console output and then started my default web browser with a one-time-token-authenticated connection to the Jupyter Notebook server (still running in the console):

```
[I 15:16:57.546 NotebookApp] Serving notebooks from local directory: /home/oxygen18/JEMIAN/Documents
[I 15:16:57.546 NotebookApp] 0 active kernels
[I 15:16:57.546 NotebookApp] The Jupyter Notebook is running at:
[I 15:16:57.546 NotebookApp] http://localhost:8888/?token=e6a7584762c731a7c64f8f71246b3e616d779f7b4852c9d9
[I 15:16:57.546 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 15:16:57.547 NotebookApp] 

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=e6a7584762c731a7c64f8f71246b3e616d779f7b4852c9d9
[I 15:17:00.863 NotebookApp] Accepting one-time-token-authenticated connection from ::1
```

Next, found the **New** drop-down menu button (top right, below the Lougout button) and selected **Python 3** to start a new notebook page using a Python 3 shell (the only kind available here).

Finally, from the **File** menu in the jupyter notebook (in the browser), selected **Rename ...** to save the *Untitled* notebook with the name `lesson1` (default extension is `.ipynb`).
