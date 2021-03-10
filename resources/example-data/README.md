# example-data

**Objective**

* Extract data from the Bluesky data collection database.
* Copy to a different computer.
* Repeat previous analyses of 2-D data.

- [example-data](#example-data)
  - [Pack: Extract measurements from the `databroker`](#pack-extract-measurements-from-the-databroker)
    - [compressed archive file](#compressed-archive-file)
  - [Unpack the data](#unpack-the-data)
  - [Load the data with databroker](#load-the-data-with-databroker)

## Pack: Extract measurements from the `databroker`

Previously, we collected a variety of measurements (bluesky *runs*)
using our simulated instrument. From a console log file, we can see the
commands used to collect the most recent scans:

```python
RE(findpeak_multipass(md=dict(motive="demo")))
#[Out]# ('0401c919-d6e8-49b1-87c8-8a99b8d69356',
#[Out]#  '483efa40-3ace-4803-bf98-fd5c91e1255f',
#[Out]#  'b4e4cbbb-a4b1-4146-aea5-ba8bc7ad7b76',
#[Out]#  'd19530f7-1ca6-4c02-a83b-229b3d92b6d1')
# Sat, 06 Mar 2021 14:11:04
listruns(plan_name="scan")
#[Out]# <pyRestTable.rest_table.Table at 0x7ff6a8094280>
# Sat, 06 Mar 2021 14:13:44
RE(bp.scan([noisy], m1, 0, 2, 5, md=dict(point_density="rough")))
#[Out]# ('7a497331-959c-4f4b-8b6b-3a2b67626d6b',)
# Sat, 06 Mar 2021 14:14:45
RE(bp.scan([noisy], m1, 0.8, 1.2, 11, md=dict(point_density="medium")))
#[Out]# ('e50cb383-7e75-47e0-9b97-9b7bf034900b',)
# Sat, 06 Mar 2021 14:15:35
RE(bp.scan([noisy], m1, 0.92, 1.0, 11, md=dict(point_density="fine")))
#[Out]# ('0d5f561c-57a3-448b-8b4d-dcd1ec57420f',)
# Sat, 06 Mar 2021 14:16:41
RE(bp.scan([noisy], m1, 0.944, 0.968, 21, md=dict(point_density="very fine")))
#[Out]# ('a8bcac2d-d3b5-47e8-aa2d-19525ea992d5',)
```

From another console log file, we see the `count` command was used to
collect one of the images:

```python
# Wed, 03 Mar 2021 10:01:31
RE(bp.count([adsimdet], md={"motive": "locate_image_peak"}))
#[Out]# ('eb1924b3-b051-4709-8d38-98a4bce487fc',)
```

The runs that we collected used three different plan commands from
[`bluesky.plans`](https://blueskyproject.io/bluesky/plans.html) (aliased
to `bp`):

command | type of measurement
:--- | :---
`bp.count` | area detector image
`bp.count` | temperature v. time scan
`bp.scan` | temperature scan
`bp.rel_scan` | 1-D scan of `noisy` v. `m1`

We collected all measurements since 2021-02-22 (with this linux
command):

    databroker-pack class_2021_03 -q "TimeRange(since='2021-02-22')" /tmp/class_data_examples  --copy-external

**NOTE**: For the older area detector image files, the (HDF5) image files were no
longer available on disk so the *packing* failed for just those runs.  Of
the 59 runs collected in that interval, 18 were not able to pack since
the image files had been deleted from disk.

<details>
<summary>typical error report due to missing image file</summary>

```
Error while exporting Run 'ec4915d9-f6f2-4b8d-85eb-cf4b3556b2f5'
Traceback (most recent call last):
  File "/home/prjemian/Apps/miniconda3/envs/bluesky_2021_1/lib/python3.8/site-packages/event_model/__init__.py", line 1041, in _attempt_with_retries
    return func(*args, **kwargs)
  File "/home/prjemian/Apps/miniconda3/envs/bluesky_2021_1/lib/python3.8/site-packages/area_detector_handlers/handlers.py", line 181, in __init__
    super().__init__(
  File "/home/prjemian/Apps/miniconda3/envs/bluesky_2021_1/lib/python3.8/site-packages/area_detector_handlers/handlers.py", line 117, in __init__
    self.open()
  File "/home/prjemian/Apps/miniconda3/envs/bluesky_2021_1/lib/python3.8/site-packages/area_detector_handlers/handlers.py", line 137, in open
    self._file = h5py.File(self._filename, "r")
  File "/home/prjemian/Apps/miniconda3/envs/bluesky_2021_1/lib/python3.8/site-packages/h5py/_hl/files.py", line 406, in __init__
    fid = make_fid(name, mode, userblock_size,
  File "/home/prjemian/Apps/miniconda3/envs/bluesky_2021_1/lib/python3.8/site-packages/h5py/_hl/files.py", line 173, in make_fid
    fid = h5f.open(name, flags, fapl=fapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5f.pyx", line 88, in h5py.h5f.open
OSError: Unable to open file (unable to open file: name = '/tmp/docker_ioc/iocad/tmp/images/742f7926-acb6-4346-b8e8_000.h5', errno = 2, error message = 'No such file or directory', flags = 0, o_flags = 0)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/prjemian/Apps/miniconda3/envs/bluesky_2021_1/lib/python3.8/site-packages/databroker_pack/_pack.py", line 228, in export_catalog
    artifacts, files = export_run(
  File "/home/prjemian/Apps/miniconda3/envs/bluesky_2021_1/lib/python3.8/site-packages/databroker_pack/_pack.py", line 346, in export_run
    files[key].update(run.get_file_list(doc))
  File "/home/prjemian/Apps/miniconda3/envs/bluesky_2021_1/lib/python3.8/site-packages/databroker/core.py", line 1132, in get_file_list
    handler = self.fillers['yes'].get_handler(resource)
  File "/home/prjemian/Apps/miniconda3/envs/bluesky_2021_1/lib/python3.8/site-packages/event_model/__init__.py", line 861, in get_handler
    handler = _attempt_with_retries(
  File "/home/prjemian/Apps/miniconda3/envs/bluesky_2021_1/lib/python3.8/site-packages/event_model/__init__.py", line 1052, in _attempt_with_retries
    raise error_to_raise from error
event_model.EventModelError: Error instantiating handler class <class 'event_model.SubclassedAreaDetectorHDF5Handler'> with Resource document Resource({'spec': 'AD_HDF5', 'root': '/', 'resource_path': 'tmp/docker_ioc/iocad/tmp/images/742f7926-acb6-4346-b8e8_000.h5', 'resource_kwargs': {'frame_per_point': 1}, 'path_semantics': 'posix', 'uid': '8d53eef4-2418-41d1-bdd6-122938631ecc', 'run_start': 'ec4915d9-f6f2-4b8d-85eb-cf4b3556b2f5'}). Its 'root' field / was *not* modified by root_map.
```

Additional files in this directory:

file | description
:--- | :---
`packing.log` | console output from `databroker-pack` command
`pack-log-errors.txt` | errors reported from `databroker-pack` command
`pack-uids-failed.txt` | uids of runs that could not be packed

</details>

### compressed archive file

Once the runs are packed, prepare a compressed archive file
[`class_data_examples.zip`](class_data_examples.zip) using the Windows
*zip* command (or the Linux *tar* and *gzip* commands):

    cd /tmp
    unzip class_data_examples.tgz class_data_examples/

## Unpack the data

Copy the compressed archive file to the data-analysis computer.  The
data analysis computer does not need the `bluesky` or `ophyd` packages;
those are for data collection and are note needed for analysis.

Unpack the `class_data_examples` folder to the desired location on the
data analysis computer.  Once the [unpack
operation](https://blueskyproject.io/databroker-pack/usage.html#unpacking-a-packed-catalog)
has been run, this folder should not be moved.

We'll demonstrate *unpacking* on a Windows 10 workstation (with an
existing conda environment for bluesky already installed):

    (bluesky_2021_1) C:\> databroker-unpack inplace C:\Users\Pete\Downloads\class_data_examples class_data_examples

The command finished with this output:

    Placed configuration file at C:\Users\Pete\AppData\Local\intake\intake\databroker_unpack_class_example_data.yml

## Load the data with databroker

Start an ipython console session or Jupyter lab notebook.  We'll
demonstrate with the [`demonstrate.ipynb`](demonstrate.ipynb) 
[notebook](https://nbviewer.jupyter.org/github/BCDA-APS/bluesky_instrument_training/blob/main/resources/example-data/demonstrate.ipynb).
