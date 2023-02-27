# testing

You may want to test the software in a conda environment.

First you must activate that environment (if not already activated). This will
reconfigure some environment variables so that the chosen environment's
executables and libraries will be found first.

```bash
conda activate bluesky_2023_2
```

Here, we show how to test two packages that are part of the APS bluesky
environment installation.

## ophyd

The `ophyd` package is the control system abstraction layer that describes the
hardware connections (such as EPICS process variables) and how they are
coordinated.  The structures from `ophyd` are used by the `bluesky` package from
data acquisition procedures.

Confirm that some part of Bluesky is working.  One easy item to test is
an EPICS PV such as the APS storage ring current (`S:SRcurrentAI`).
This should print the storage current.

```bash
CMD="import ophyd;"
CMD+=" pv = ophyd.EpicsSignal('S:SRcurrentAI', name='pv');"
CMD+=" pv.wait_for_connection();"
CMD+=" print(pv.get());"
python -c "${CMD}"
```

## APS Data Management

The APS Data Management software is used to process data file workflows after
the data has been collected (by Bluesky or other software).  The workflows are
sets of instructions that describe how to find the data and what should happen
next with its processing.

Add the APS data management API and test it.  If successful, this will
not print any errors to standard output.

```bash
# install
conda install -c apsu aps-dm-api(base)

# test
CMD="from dm.cat_web_service.api.catApiFactory import CatApiFactory;"
CMD+=" api = CatApiFactory.getRunCatApi()"
python -c "${CMD}"
```
