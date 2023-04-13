# Instrument Package Guide

The instrument package defines the features of your equipment for use with data
acquisition using the Bluesky framework.  It is structured as a Python
[package](https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html)
so that it will be easy to use with the Python `import` command, like much other
Python software.

There are many ways to define your equipment so consider this guide as a
reference for ideas rather than a set of requirements.

**Contents**
- [Instrument Package Guide](#instrument-package-guide)
  - [Basic Structure](#basic-structure)
  - [Add Motor(s)](#add-motors)
  - [Add Scaler(s)](#add-scalers)
  - [Re-organize into Devices](#re-organize-into-devices)
  - [Add Area Detector(s)](#add-area-detectors)
  - [Other Device Support](#other-device-support)
  - [Implement Custom Plans](#implement-custom-plans)
  - [Callbacks](#callbacks)
  - [Review Metadata](#review-metadata)
  - [Experiment-specific User Code](#experiment-specific-user-code)

## Basic Structure

The basic structure is organized into components of the Bluesky framework.  All
these directories may contain python file(s).

```
instrument/       <-- all aspects of the equipment
    callbacks/    <-- your custom Python code that responds to RunEngine documents or other
    devices/      <-- your equipment and its connections with EPICS
    framework/    <-- Configure the Bluesky framework
    mpl/          <-- Configure MatPlotLib for pltting in a console or Jupyter notebook
    plans/        <-- your custom measurement actions (_bluesky plans_)
    utils/        <-- (utilities) other Python code that does not fit above
```

Each directory has a `__init__.py` file (which _can_ be empty).  The very
existence of this file informs Python that the directory is a Python *package*
which means that it can be imported.  The `__init__.py` file can be used to control
what is imported and the order in which that import is sequenced.

In any of the Python files, the
[`__all__`](https://stackoverflow.com/questions/44834) symbol is a Python list
that identifies which Python symbols from that file will be imported by default.
(Any Python symbol may be imported by name, this just controls the more general
case.)

## Add Motor(s)

To add an EPICS [motor](https://github.com/epics-modules/motor) to your
instrument package, edit the file `instrument/devices/motors.py`.  You'll need
the EPICS PV for the motor (example is `ioc:m1`).  There may be comments in your
`motors.py` file to give you a suggestion of the correct command.  Add this line
_after_ the various `import` lines (where the EPICS motor PV is the first
argument):

```python
m1 = EpicsMotor("ioc:m1", name="m1", labels=("motor",))
```

The left side (LHS) assigns the new (ophyd) `EpicsMotor()` object to the symbol
`m1`.  Follow the [rules for naming Python
symbols](https://www.python.org/dev/peps/pep-0008/#naming-conventions).  By
convention, the `name=` keyword has the same value as the LHS.  The keyword
`labels=()` is an optional
[tuple](https://docs.python.org/3/library/stdtypes.html?highlight=tuple#sequence-types-list-tuple-range).
When the `motor` value is added to the tuple, then this motor will show up in
the report provided by the
[`%wa`](https://blueskyproject.io/bluesky/magics.html?highlight=magic#listing-available-motors-using-wa-post-v1-3-0)
(bluesky IPython) magic command.

CAUTION: Avoid certain names such as
[`del`](https://docs.python.org/3/reference/simple_stmts.html?highlight=del#the-del-statement)
and
[`lambda`](https://docs.python.org/3/reference/expressions.html?highlight=lambda#lambda)
since these are reserved Python names with very important meanings.  

Be sure to add this new motor symbol to the `__all__` list near the top of the file.

Once you add motors to the `instrument/devices/motors.py` file, you should
enable its automatic import by removing the comment from the line in
`instrument/devices/__init__.py`:

change

```python
# from .motors import *
```

to be

```python
from .motors import *
```

## Add Scaler(s)

Often, an instrument will use a single scaler to collect pulse signals from
various counting detectors aush as ionization chambers, photodiodes, and
scintillation counters.  These are coordinated by the EPICS
[scaler](https://github.com/epics-modules/scaler) record.

There are [two different ophyd objects to describe an EPICS
scaler](https://blueskyproject.io/ophyd/generated/ophyd.scaler.html#module-ophyd.scaler).
We use the `ScalerCH` here since it uses the user-defined scaler record channel
names with the acquired data.

Like the motor example above, you'll need the EPICS scaler PV name.  Edit the
file `instrument/devices/scaler.py` and change the `ScalerCH` line.  There are
additional lines if your scaler has predefined names you wish to call in other
Python code.  Otherwise, comment out these lines by placing a `#` character at
the start of each line.

The `detectors` label is used by the `%wa` magic for reporting and also the
`%ct` for convenient counting from the command line.  The `scalers` label helps
to distinguish this type of detector from, for example, area detectors.

Again, edit the `__all__` symbol with any new symbol names and enable the import
of scaler.py by editing `instrument/devices/__init__.py`.

## Re-organize into Devices

Once many motors have been entered, it might be convenient to group them in
terms of a common structure.  Consider a sample X-Y stage might have motors
`sample_x` and `sample_y`.  These can be grouped together into an [ophyd
Device](https://blueskyproject.io/ophyd/device-overview.html).  Also note that a
Device can contain other Devices, in addition to Signals, such as the
[ApsMachineParametersDevice](https://apstools.readthedocs.io/en/latest/_modules/apstools/devices.html#ApsMachineParametersDevice).

On ophyd Device organizes one or more ophyd Signals and/or Devices into a larger
structure, for grouping or to provide custom controls.

<details>
<summary>Device Example</summary>
Consider this hypothetical case

motor description | EPICS PV
--- | ---
sample x motion | `ioc:m11`
sample y motion | `ioc:m12`

We'll make a new file (don't forget to import the new file in `__init__.py`)
with these contents (logging and other parts omitted for clarity, follow the
example in `motors.py` for these.):

```python
__all__ = ["sample_stage", ]
from ophyd import Device, EpicsMotor
from ophyd import Component

class StageXY(Device):
    x = Component(EpicsMotor, 'm11', labels=("motor",))
    y = Component(EpicsMotor, 'm12', labels=("motor",))

sample_stage = StageXY('ioc:', name='sample_stage')
```

The first argument to our `StageXY()` is the common prefix for the EPICS PV.
Note also that we do not have to provide the `name=` keyword for the Components
since ophyd can determine the name as each Component is added into the Device.
Only at the outermost level must the `name=` keyword be provided. Each of the
components provides the remaining part of the EPICS PV.

motor description | EPICS PV | ophyd symbol | data name
--- | --- | --- | ---
sample x motion | `ioc:m11` | `sample_stage.x` | `sample_stage_x`
sample y motion | `ioc:m12` | `sample_stage.y` | `sample_stage_y`

Use the ophyd name in your Python code.  The _data name_ is how the values are
labeled in the data.  (There's a reason for this difference beyond this scope.)

NOTE:  Once you have used a PV in a custom Device, remove it from any other file such as `motors.py`.  The adminition from the ophyd developers is that you _connect a PV once and only once_.

</details>

## Add Area Detector(s)

EPICS Area Detectors are implemented as custom ophyd Devices that subclass (use) various standard parts
from ophyd.

See these examples:

* [Dectris Pilatus](https://apstools.readthedocs.io/en/latest/examples/_ad__pilatus.html) (with explanations)
* [Perkin-Elmer](https://apstools.readthedocs.io/en/latest/examples/_ad_pe.html) (no explanations, just example code)

## Other Device Support

The examples so far only begin to demonstrate the variety of Device
customizations.  Consult the various instrument configurations on the
[wiki](https://github.com/BCDA-APS/use_bluesky/wiki) and the
[apstools](https://github.com/BCDA-APS/apstools/blob/main/apstools/devices.py)
package for more device examples.

TIP: Organize your custom Device code into separate files to make it easy to manage.  Don't forget to edit the `__add__` symbol and also edit the `__init__.py` file so the new code is imported automatically.

## Implement Custom Plans

Plans describe your custom sequence of actions.  They can be a complete plan that acquires a _run_ or just part of a measurement sequence.

Consult the various instrument configurations on the
[wiki](https://github.com/BCDA-APS/use_bluesky/wiki) and the
[apstools](https://github.com/BCDA-APS/apstools/blob/main/apstools/plans.py)
package for more plan examples.

If you are translating PyEpics code to Bluesky plans, consult this
[guide](https://blueskyproject.io/bluesky/from-pyepics-to-bluesky.html?highlight=blocking).

Keep in mind that a plan should not call code that blocks execution of the bluesky
*RunEngine* from conducting its periodic background actions. One such example is
the [`sleep()`
action](https://blueskyproject.io/bluesky/tutorial.html?highlight=blocking)
sometimes used to control sequencing of events.  More discussion of _blocking_
is provided in the context of how the RunEngine processes its
[Messages](https://blueskyproject.io/bluesky/msg.html?highlight=blocking).

## Callbacks

One custom RunEngine callback has been added to the `instrument` package
template for the APS.  The [SPEC file writer
callback](https://apstools.readthedocs.io/en/latest/source/_filewriters.html#apstools.filewriters.SpecWriterCallback)
(added before the `callbacks/` subpackage was added) is configured in
`instrument/framework/callbacks.py`.  It writes bluesky runs to a text file in
the format of the [SPEC data acquisition software](https://certif.com).
Different from SPEC (which appends the file line-by-line as data is acquired),
the SPEC callback here appends the file once the run's `stop` document is
received.

If you do not want SPEC files to be written, then comment out the associated
`import` in `instrument/framework/__init__.py`.

## Review Metadata

A strength of the Bluesky framework is the coordination in a database of
acquired data with metadata about the acquisition.  This enables a variety of
data science after the measurement is complete.

The template `instrument` package installed initially
configures (in `instrument/framework/metadata.py`) some simple information that is added to every
bluesky run (in dictionary `RE.md`):

key | meaning
--- | ---
`beamline_id` | value of [BEAMLINE](/install/README.md#install-instrument-package)
`instrument_name` | value of [INSTRUMENT](/install/README.md#install-instrument-package)
`proposal_id` | (default is `comissioning`) You should modify this for each proposal
`pid` | process identifier (for diagnostics and logging)
`login_id` | user and workstation collecting the data (for diagnostics and logging)
`versions` | version numbers of various Python packages (for diagnostics and logging)

The motivation for adding any metadata to a measurement is to use that later as
search keys.  Sample information, experimenters, proposal and safety form terms:
all could be useful later in retrieving related bluesky
[_runs_](https://blueskyproject.io/bluesky/documents.html?highlight=runs#overview-of-a-run)
from the database.

Consult this
[guide](https://blueskyproject.io/bluesky/metadata.html?highlight=metadata) for
more information about recording metadata.  Configurations can be for all runs,
specific runs, or even specific types of runs.  The system for adding metadata
is versatile.

## Experiment-specific User Code

Sometimes, a user may need experiment-specific code that is not for general
inclusion in the instrument package.  Components from the `instrument` package
may be imported from such custom user code by writing a file in the working
directory with the support.  The file can be loaded and run in an IPython
session with the [`%run -i
filename.py`](https://ipython.org/ipython-doc/3/interactive/magics.html#magic-run)
magic command.

<details>
<summary>Example User Code</summary>

Here is a contrived example of custom user code.

First, go to a new working directory before starting a bluesky session:

    cd /tmp
    mkdir demo
    cd /tmp/demo

Save this "custom user code" to local file `/tmp/demo/my_code.py`:

```python
from instrument.devices import m1

print(f"m1 is now at {m1.position:.3f}")
```

Start the bluesky session:

```
(base) prjemian@zap:/tmp/demo$ blueskyZap.sh 
Python 3.8.5 (default, Sep  4 2020, 07:30:14) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.20.0 -- An enhanced Interactive Python. Type '?' for help.

IPython profile: bluesky
Activating auto-logging. Current session state plus future input saved.
Filename       : /tmp/demo/.logs/ipython_console.log
Mode           : rotate
Output logging : True
Raw input log  : False
Timestamping   : True
State          : active
I Sun-15:20:22 - ############################################################ startup
I Sun-15:20:22 - logging started
I Sun-15:20:22 - logging level = 10
I Sun-15:20:22 - /home/prjemian/.ipython/profile_bluesky/startup/instrument/collection.py
I Sun-15:20:22 - /home/prjemian/.ipython/profile_bluesky/startup/instrument/mpl/console.py
I Sun-15:20:22 - bluesky framework
I Sun-15:20:22 - /home/prjemian/.ipython/profile_bluesky/startup/instrument/framework/check_python.py
I Sun-15:20:22 - /home/prjemian/.ipython/profile_bluesky/startup/instrument/framework/check_bluesky.py
I Sun-15:20:23 - /home/prjemian/.ipython/profile_bluesky/startup/instrument/framework/initialize.py
I Sun-15:20:23 - /home/prjemian/.ipython/profile_bluesky/startup/instrument/framework/metadata.py
I Sun-15:20:23 - /home/prjemian/.ipython/profile_bluesky/startup/instrument/framework/callbacks.py
I Sun-15:20:23 - writing to SPEC file: /tmp/demo/20210221-152023.dat
I Sun-15:20:23 -    >>>>   Using default SPEC file name   <<<<
I Sun-15:20:23 -    file will be created when bluesky ends its next scan
I Sun-15:20:23 -    to change SPEC file, use command:   newSpecFile('title')
I Sun-15:20:23 - /home/prjemian/.ipython/profile_bluesky/startup/instrument/devices/motors.py
I Sun-15:20:23 - /home/prjemian/.ipython/profile_bluesky/startup/instrument/devices/scaler.py

In [1]: 
```

Run the `my_code.py` file:

```python
In [1]: %run -i my_code.py
m1 is now at 3.000

In [2]: 
```

</details>
