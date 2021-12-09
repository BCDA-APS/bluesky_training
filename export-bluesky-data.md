# Exporting data from Bluesky

An instrument scientist asks:

> How to export experiment data for a user?
> How do I get the data out of the databroker to send it to my user?

**_CONTENTS_**

- [Exporting data from Bluesky](#exporting-data-from-bluesky)
  - [Choices](#choices)
  - [databroker-pack](#databroker-pack)
  - [Identify experiment data in databroker](#identify-experiment-data-in-databroker)
  - [file export](#file-export)
    - [text files](#text-files)
      - [CSV](#csv)
      - [JSON](#json)
      - [SPEC](#spec)
    - [HDF5 files](#hdf5-files)
      - [raw](#raw)
      - [NeXus](#nexus)
      - [DX : Data Exchange](#dx--data-exchange)
  - [Callbacks](#callbacks)
    - [apstools](#apstools)
      - [NeXus - NXWriterAPS](#nexus---nxwriteraps)
      - [SPEC: SpecWriterCallback](#spec-specwritercallback)

## Choices

First, you have some choices:

- How frequently do you want to do this?
  - _one-time_: learn a set of Python commands
  - _occasional_: build Python command (or _callback_) to expedite the steps _for your users_.
  - _always_: write file as data is acquired using a Bluesky
    [`callback`](https://blueskyproject.io/bluesky/callbacks.html?highlight=callback#overview-of-callbacks) (to the bluesky `RunEngine`)
- What tool(s) will the user(s) be using to **_read_** the data received?
  - _python_: [`databroker`](https://blueskyproject.io/databroker/)
  - _file(s)_: What file format to use?
    - _text_:
      [CSV](https://docs.python.org/3/library/csv.html),
      [JSON](https://docs.python.org/3/library/json.html),
      [SPEC](https://certif.com/spec_manual/idx.html)
    - _HDF5_:
      [raw](https://portal.hdfgroup.org/display/HDF5/HDF5),
      [NeXus](https://www.nexusformat.org/),
      [DX](https://www.aps.anl.gov/Science/Scientific-Software/DataExchange)
    - _other_: image files?
  - _network_:
    - _[globus](https://www.globus.org/data-transfer)_:
      high-performance data transfers between systems within and across organizations
    - _[`tiled`](https://blueskyproject.io/tiled/)_:
      Bluesky **data access** service for data-aware portals and data science tools.

## databroker-pack

The [`databroker-pack`](https://blueskyproject.io/databroker-pack/) package
is used as part of the process to move a subset of a databroker catalog (or the entire catalog).

> The utility `databroker-pack` boxes up Bluesky Runs as a directory of
> files which can be archived or transferred to other systems. At their
> destination, a user can point `databroker` at this directory of files
> and use it like any other data store.

> The utility `databroker-unpack` installs a configuration file that
> makes this directory easily "discoverable" so the recipient can access
> it using `databroker.catalog["SOME_CATALOG_NAME"]`.

The APS bluesky training has an example of the
[pack](https://github.com/BCDA-APS/bluesky_training/blob/main/resources/example-data/README.md)
and
[unpack](https://github.com/BCDA-APS/bluesky_training/blob/main/resources/example-data/README.md#unpack-the-data)
processes. Once unpacked, the data can be used, as shown in [this
example Jupyter
notebook](https://github.com/BCDA-APS/bluesky_training/blob/main/resources/example-data/demonstrate.ipynb).

## Identify experiment data in databroker

To access your experiment's data, you need to get it from your _catalog_
(usually `cat` where `cat = databroker.catalog[CATALOG_NAME]`).  You can
access by providing a reference.  The reference is one of these:

- `scan_id` (some positive integer)
- `uid` (a hexadecimal text string)
- Python reference to a recent scan (a negative integer such `-1` for
  the most recent run).  

Take this example for the fictious `45id` catalog:

```python
import databroker
cat = databroker.catalog["45id"]
run = cat[554]  # access by scan_id
ds = run.primary.read()  # all data from the stream named: primary
md = run.metadata  # the run's metadata
```

NOTE: the run's metadata is here: `run.metadata`.
This is a Python dictionary with `start` and `stop` keys for the respective document's metadata.

A summary of the run is shown by just typing `run` on the command line:

```python
In [12]: run
Out[12]: 
BlueskyRun
  uid='c6b461f7-53aa-4941-9e38-ce842f08bf2d'
  exit_status='success'
  2021-12-06 15:46:36.397 -- 2021-12-06 15:46:40.430
  Streams:
    * baseline
    * PeakStats
    * primary
```

Similarly, the primary data can be seen in a table:

```python
In [13]: ds
Out[13]: 
<xarray.Dataset>
Dimensions:           (time: 31)
Coordinates:
  * time              (time) float64 1.639e+09 1.639e+09 ... 1.639e+09 1.639e+09
Data variables:
    noisy             (time) float64 1.783e+04 2.009e+04 ... 1.974e+04 1.745e+04
    m1                (time) float64 -0.679 -0.69 -0.702 ... -1.004 -1.015
    m1_user_setpoint  (time) float64 -0.6792 -0.6904 -0.7016 ... -1.004 -1.015
```

Knowing that the independent data (x) name is `m1` and the dependent data (y) name is `noisy`, this data can be plotted:

```python
In [11]: ds.plot.scatter("m1", "noisy")
Out[11]: <matplotlib.collections.PathCollection at 0x7f52602fc640>
```

![scan_id=554 plotted](./554-plot-scatter.png)

## file export

For one-time (or occasional) use, it might be simpler to export a data
stream to a file.  For simple data, text is very easy.  For more
structured data, you  might consider SPEC or NeXus at this time.

### text files

Text files represent an easy way to inspect the data contents outside of
any specific data analyasis software.  But it helps to have some kind of
structure (schema) to the content.  That's the purpose of CSV, JSON,
SPEC, or some other schema.

#### CSV

The xarray structure of `ds` does not have a method to export to CSV,
but `pandas` does and `ds` has a `to_pandas()` exporter:
`ds.to_pandas().to_csv()`.  Each stream can be written to a CSV file
(perhaps all together in one file but that looks complicated and is
against the objective keeping it simple).  Here is an example:

```python
with open("/tmp/run_554-primary.csv", "w") as f:
    f.write(ds.to_pandas().to_csv())
```

The `.to_csv()` method has many options for formatting.

Since `md` is a dictionary structure, it is not so easy to write into a CSV file.

#### JSON

While Python provides a
[`json`](https://docs.python.org/3/library/json.html) package to
read/write a JSON file, it may be easier to use the `xarray` structure
returned by the `databroker` from `run.primary.read()` (where  `primary`
is the name of the document stream named _primary_).  Export the data to
JSON strings.  These, in turn may be written to a file.  Here is an
example:

```python
import json

data = {"metadata": md}
for stream_name in list(run):  # get ALL the streams
    # such as data["primary"] = run.primary.read().to_dict()
    data[stream_name] = getattr(run, stream_name).read().to_dict()
with open("/tmp/run_554.json", "w") as f:
    f.write(json.dumps(data, indent=2))
```

#### SPEC

See section [SPEC: SpecWriterCallback](#spec-specwritercallback) below.

### HDF5 files

Python support for the HDF5 format is usally provided through use of the
[`h5py`](https://www.h5py.org/) package.  NeXus is an example of a specific

#### raw

HDF5 is a hierarchical data format, allowing much structure in how the
data is stored in an HDF5 data file.  Refer to the [HDF5
documentation](https://portal.hdfgroup.org/display/HDF5/HDF5) and/or the
[h5py documentation](https://www.h5py.org/) for details in how to write
raw data to this format.

#### NeXus

See section [NeXus - NXWriterAPS](#nexus---nxwriteraps) below.

#### DX : Data Exchange

not supported yet

Since there is no bluesky code yet to write data in the DX format, you
must refer to the [Data
Exchange](https://www.aps.anl.gov/Science/Scientific-Software/DataExchange)
documentation for details.

## Callbacks

In the context of data for bluesky, a _callback_ is python code that
subscribes to the bluesky `RunEngine` and receives documents during a
run.  The callback should handle each of those documents to pwrite the
data according to the terms of the file format.
### apstools

The
[`apstools`](https://bcda-aps.github.io/apstools/source/_filewriters.html)
package supports automatic data export to NeXus or SPEC data files via
callbacks.  The support is provided in python `class` definitions that
handle each of the document types from the `RunEngine`.

#### NeXus - NXWriterAPS

The
[documentation](https://bcda-aps.github.io/apstools/source/_filewriters.html#apstools.filewriters.NXWriterAPS)
is brief.  It may be more interesting to see the setup for the [USAXS
instrument](https://github.com/APS-USAXS/ipython-usaxs/blob/master/profile_bluesky/startup/instrument/callbacks/nxwriter_usaxs.py)

#### SPEC: SpecWriterCallback

The
[documentation](https://bcda-aps.github.io/apstools/source/_filewriters.html#apstools.filewriters.SpecWriterCallback)
is brief.  It may be more interesting to see the setup for the [bluesky
training
instrument](https://github.com/BCDA-APS/bluesky_training/blob/main/bluesky/instrument/callbacks/spec_data_file_writer.py).
