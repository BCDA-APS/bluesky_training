## Configure bluesky instrument

Settings for various aspects of data collection are distributed amongst the many
directories and files of the `instrument/` subdirectory.  We call this directory
the `instrument` package (it is configured as a Python package for use by an
`import` statement).  See this [advice](./configure_bluesky_instrument.md) for
configuration of the `instrument` package.

The `instrument/iconfig.yml` file is an effort to gather
these many configurations into one location, easily found in the root directory
of the `instrument` package.  The definitions in this file are easily
(re)configured.

Contents

- [Configure bluesky instrument](#configure-bluesky-instrument)
- [Initial configuration](#initial-configuration)
- [Parts of the instrument package](#parts-of-the-instrument-package)
  - [Framework](#framework)
  - [matplotlib](#matplotlib)
  - [Callbacks](#callbacks)
  - [Devices](#devices)
  - [Plans](#plans)
  - [Utils](#utils)

## Initial configuration

Amongst the many items you might edit in the `instrument/iconfig.yml` file,
the databroker catalog name is the first.

Change:

```yml
DATABROKER_CATALOG: &databroker_catalog training
```

to (assuming *your* catalog is named `45ida_abcd`):

```yml
DATABROKER_CATALOG: &databroker_catalog 45ida_abcd
```

You should change this line:

```yml
ALLOW_AREA_DETECTOR_WARMUP: true
```

to

```yml
ALLOW_AREA_DETECTOR_WARMUP: false
```

You may comment these lines (used by the training IOCs, not so likely to use them with your instrument):

```yml
ADSIM_IOC_PREFIX: "ad:"
GP_IOC_PREFIX: "gp:"
AD_IMAGE_DIR: "adsimdet/%Y/%m/%d"
AD_MOUNT_PATH: /tmp
BLUESKY_MOUNT_PATH: /tmp/docker_ioc/iocad/tmp
```

## Parts of the instrument package

### Framework

The `instrument.framework` directory contains the files that setup the core of Bluesky (and related packages).

### matplotlib

The `instrument.mpl` directory contains the matplotlib configuration for data visualizations.

### Callbacks

The `instrument.callbacks` directory contains custom handling of the documents
from the Bluesky RunEngine.

If your instrument does not need to generate data files as if they came from the
SPEC data collection software, then change this line in your
`instrument/iconfig.yml` file:

from

```yml
WRITE_SPEC_DATA_FILES: true
```

to

```yml
WRITE_SPEC_DATA_FILES: false
```

Other callbacks are possible.  For example, the APS USAXS instrument writes
NeXus files using a
[callback](https://github.com/APS-USAXS/usaxs-bluesky/blob/master/instrument/callbacks/nxwriter.py).

The order of file loading is controlled by the lines in the
[`__init__.py`](./about_init_files.md) file.  In some cases, the sequence of
loading is important.

### Devices

On startup, Devices (which describe your hardware controls) are configured
before Plans.  This pattern is designed to avoid import loops (A needs B which
needs A).

There are many files in the `instrument/devices/` directory.  None of them are
in use until they are uncommented in the `./instrument/devices/__init__.py` file
(and then the IPython session is restarted). Before you uncomment one of these
files, you might need to adjust the contents of the file first to match your
hardware. These files are leftovers as used in the bluesky training examples and
provide ideas for what is possible with your instrument.

The order of file loading is controlled by the lines in the
[`__init__.py`](./about_init_files.md) file.  In some cases, the sequence of
loading is important.

**Note**: A major principle is that any activities on startup **should not
change settings in EPICS**.  With this in mind, you gain the confidence that
EPICS will not be affected just beacuse a Bluesky session was started.
(This is why you changed `ALLOW_AREA_DETECTOR_WARMUP` to `false` above.)

**Tip**: SPEC users:
[`spec2ophyd`](https://bcda-aps.github.io/apstools/latest/applications/spec2ophyd.html#spec2ophyd)
can translate much of your SPEC config file into content for the Devices
directory.

### Plans

The `instrument/plans/` directory contains Python files that define the custom
Bluesky plans for your instrument.  The existing files serve as examples.

The order of file loading is controlled by the lines in the
[`__init__.py`](./about_init_files.md) file.  In some cases, the sequence of
loading is important.

### Utils

This directory is for Python code your instrument needs but is not easily
classified as Callbacks, Devices, or Plans.  For example, standard analytical
routines might be best placed in Utils.

The order of file loading is controlled by the lines in the
[`__init__.py`](./about_init_files.md) file.  In some cases, the sequence of
loading is important.
