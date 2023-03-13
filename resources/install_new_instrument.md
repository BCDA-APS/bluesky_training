# Steps to install a new instrument

Contents

- [Steps to install a new instrument](#steps-to-install-a-new-instrument)
  - [Setup a bluesky instrument](#setup-a-bluesky-instrument)
  - [Create the conda environment](#create-the-conda-environment)
  - [Activate the conda environment](#activate-the-conda-environment)
  - [Test the new bluesky instrument](#test-the-new-bluesky-instrument)
  - [Setup your databroker catalog configuration](#setup-your-databroker-catalog-configuration)
  - [IPython startup](#ipython-startup)
  - [Start version control](#start-version-control)
  - [Configure bluesky instrument](#configure-bluesky-instrument)

**Note**:  These *instructions have been written for workstations running the
Linux operating system*.  They may be used for other operating systems but
expect some modifications are necessary.  One such modification is that the
`libhkl` library, needed for diffractometer support, is only available for Linux
x86_64 host architectures.

In Linux, use the `bash` command shell.

## Setup a bluesky instrument

Use the program
[`new_bluesky_instrument.py`](https://github.com/BCDA-APS/bluesky_training/blob/main/resources/new_bluesky_instrument.py)
to install a new bluesky instrument configuration from the online [APS Bluesky
Training](https://github.com/BCDA-APS/bluesky_training) repository template.
(While you will need to download this program on other networks, at APS
workstations, this program should be available from
`/APSshare/bin/new_bluesky_instrument.py`.)

`new_bluesky_instrument.py` only needs Python 3.8+ and the
[requests](https://docs.python-requests.org/en/latest/index.html) package.

Here's an example:

```bash
(base) user@host:~$ new_bluesky_instrument.py  ~/bluesky
INFO:__main__:Installing to: '/tmp/tmp_instrument'
INFO:__main__:Downloading 'https://github.com/BCDA-APS/bluesky_training/archive/refs/heads/main.zip'
INFO:__main__:Extracting content from '/tmp/bluesky_training-main.zip'
INFO:__main__:Installing to '/home/user/bluesky'
```

Use `new_bluesky_instrument.py -h` for usage information.

The installer will download the ZIP file from the GitHub training repository if it's not already
present in the `/tmp` directory or if the existing file is old.

## Create the conda environment

A bluesky instrument uses many Python packages not included in the Python
Standard Library.  Rather than add these directly into the system Python
installation, it is recommended to create a Python virtual environment which has
the suite of packages (and specific versions) required.

Follow this [guide](./conda_environment.md) to create the `bluesky_2023_2` conda
environment for
data collection with bluesky.

Here's an example:

```bash
(base) user@host:~$ cd ~/bluesky
(base) user@host:~$ conda env create \
    --force \
    -n bluesky_2023_2 \
    -f ./environments/environment_2023_2.yml \
    --solver=libmamba
```

## Activate the conda environment

As shown above, you will need to activate the conda environment in each console
session when you plan to use it.  Here's an example:

```bash
(base) user@host:~/bluesky $ conda activate bluesky_2023_2
```

This activation will remain for the duration of the session, at least until you
change it with a `conda activate` or `conda deactivate` command or start a new
shell.

Use `conda env list` to discover the environments you have and the directories
in which they are installed.

## Test the new bluesky instrument

At this point, you have assembled enough of the parts to test the initial
installation with bluesky. Follow the steps in [this
guide](./test_new_bluesky_instrument.md) to test the installation.

In the remaining steps, we'll configure the instrument for your catalog and
specific hardware configuration.

## Setup your databroker catalog configuration

Let's assume (for example purposes), you have been given this bluesky/databroker
catalog assignment:

- name: `45ida_abcd`
- MongoDB server: `mongoserver.xray.aps.anl.gov`
- MongoDB collection: `45ida_abcd-bluesky`

See this [guide](./configure_databroker.md) to configure databroker.

Confirm that databroker can find the `45ida_abcd` catalog:

```bash
(bluesky_2023_2) user@host:~/bluesky$ python -c "import databroker; print(list(databroker.catalog))"
['45ida_abcd']
```

## IPython startup

TODO

- ipython directory
- ipython profile
- file in the startup directory

## Start version control

While this step is optional, it is **highly recommended** that you place your
bluesky instrument directory under some form of software version control.  At
minimum, this can provide some form of backup protection.  It also helps others
to collaborate with similar bluesky instruments by sharing your instrument's
implementations.

Instructions for using [`git`](https://git-scm.com/) as software version control
with [GitHub](https://github.com/) or the [APS GitLab
server](https://git.aps.anl.gov/) are provided in [this separate
document](./git-help.md).

## Configure bluesky instrument

See this [advice](./configure_bluesky_instrument.md) for configuration of the
`instrument` package (content in the `instrument/` directory).
