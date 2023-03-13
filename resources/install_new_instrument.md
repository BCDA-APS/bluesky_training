# Steps to install a new instrument

Contents

- [Steps to install a new instrument](#steps-to-install-a-new-instrument)
  - [Setup a bluesky instrument](#setup-a-bluesky-instrument)
  - [Setup a conda environment](#setup-a-conda-environment)
    - [Get the `conda` command](#get-the-conda-command)
    - [Install the environment for bluesky](#install-the-environment-for-bluesky)
  - [Activate the conda environment](#activate-the-conda-environment)
  - [Setup a databroker catalog configuration](#setup-a-databroker-catalog-configuration)
  - [Setup version control with git](#setup-version-control-with-git)
  - [Setup configuring bluesky instrument](#setup-configuring-bluesky-instrument)

Note:  These *instructions have been written for workstations running the
Linux operating system*.  They may be used for other operating systems but
expect some modifications are necessary.  One such modification is that the
`libhkl` library, needed for diffractometer support, is only available for Linux
x86_64 host architectures.

In Linux, use the `bash` command shell.

## Setup a bluesky instrument

Use the
[`new_bluesky_instrument.py`](https://github.com/BCDA-APS/bluesky_training/blob/main/resources/new_bluesky_instrument.py)
program to install a new bluesky instrument configuration from the online [APS
Bluesky Training](https://github.com/BCDA-APS/bluesky_training) repository
template.  (While you will need to download this program on other networks, at
APS workstations, this program should be available from
`/APSshare/bin/new_bluesky_instrument.py`.)

To run this program, only Python 3.8+ and the
[requests](https://docs.python-requests.org/en/latest/index.html) package are
required.

Here's an example:

```bash
(base) user@host:~$ new_bluesky_instrument.py  ~/bluesky
INFO:__main__:Installing to: '/tmp/tmp_instrument'
INFO:__main__:Downloading 'https://github.com/BCDA-APS/bluesky_training/archive/refs/heads/main.zip'
INFO:__main__:Extracting content from '/tmp/bluesky_training-main.zip'
INFO:__main__:Installing to '/home/user/bluesky'
```

See the program's help (`new_bluesky_instrument.py -h`) for usage information.

The installer will download the ZIP file from the repository if it's not already
present in the `/tmp` directory or if the existing file is old.

## Setup a conda environment

A bluesky instrument uses many Python packages not included in the Python
Standard Library.  Rather than add these directly into the system Python
installation, it is recommended to create a Python virtual environment which has
the suite of packages (and specific versions) required.

Principally, a Python virtual environment gives you control over the suite of
packages and insulates you from any system software updates.

Here, we describe the creation of a Python virtual environment managed by
[conda](https://docs.conda.io/projects/conda/en/latest/index.html).  While
opinions may vary, we see some advantages to using `conda` over
[`venv`](https://docs.python.org/3/library/venv.html).  Consequently, we use
`conda` to install most packages, falling back to `pip` to install any remaining
packages.  We use [YAML](https://yaml.org) files to describe these conda
environments.  See this
[article](https://medium.com/@balance1150/how-to-build-a-conda-environment-through-a-yaml-file-db185acf5d22)
for more instruction about conda environment YAML files.

### Get the `conda` command

Skip ahead to the next section if you already have a `conda` command available
in your `bash` shell.

If your (`bash` shell) command prompt does not start with `(base)` (or some
other conda aenvironment name), you probably do not have a conda environment
activated and probably do not have a `conda` command available.

Follow these steps:

1. Use the `bash` shell:

   ```bash
   $ bash
   user@host:~$
   ```

2. Activate the `conda` base environment:

   ```bash
   user@host:~$ source /PATH/TO/CONDA/bin/activate
   ```

   where `/PATH/TO/CONDA`  is the directory of your conda base installation.  At APS, that location is `/APSshare/miniconda/x86_64`.  For workstations on other networks, you may need to install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) for yourself.

### Install the environment for bluesky

Using the new instrument as setup above (where the installation directory was
`~/bluesky`), then look for the latest installation configuration file in the
`~bluesky/environments/` directory.  At this time, the latest file is
`environment_2023_2.yml`.

We create different versions of the YAML file, named for the APS operating cycle
(2021-1, 2023-2, ...), as the suite of packages for a working installation may
change over time.  By keeping all these files in a `environments/` subdirectory,
we can restore any of these environments with a simple command.

The instruction to (re)create the conda environment
is in (a comment in) the first few lines of the file:

```bash
(base) user@host:~/bluesky/environments $ head environment_2023_2.yml
name: bluesky_2023_2

# download:
#   wget https://raw.githubusercontent.com/BCDA-APS/bluesky_training/main/bluesky/environments/environment_2023_2.yml
# create:
#   conda env create --force -n bluesky_2023_2 -f ./environment_2023_2.yml --solver=libmamba
# activate:
#   conda activate bluesky_2023_2

# Note this advice about bash environment variables:
```

On a workstation with access to the outside network (some APS workstations are
restricted to APS-ONLY access), create the conda environment with the next
command.  Line breaks have been added for this documentation.

```bash
conda env create \
    --force \
    -n bluesky_2023_2 \
    -f ./environment_2023_2.yml \
    --solver=libmamba
```

Installation usually takes (at least) a few minutes to complete.

Notes:

- The `--force` option will replace any existing environment by this name
  **without asking for confirmation**.
  Remove this option if you wish.
- The `-n bluesky_2023_2` sets the name of the conda environment to be created.
- The `-f ./environment_2023_2.yml` option names the YAML file to be used (so
  the `./` part means you need to make this command **from within** the
  `/bluesky/environments/` directory or the YAML file will not be found).
- The `--solver=libmamba` option will use the (much faster)
  [`conda-libmamba-solver`](https://conda.github.io/conda-libmamba-solver/).
  Either install that in your `base` environment or remove this install option.


Once finished, the installer will report the commands to manage the new
environment:

```bash
#
# To activate this environment, use
#
#     $ conda activate bluesky_2023_2
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

## Activate the conda environment

As shown above, you will need to activate the conda environment in each console
session when you plan to use it.  Here, we activate the `bluesky_2023_2` environment:

```bash
(base) user@host:~/bluesky $ conda activate bluesky_2023_2
```

This activation will remain for the duration of the session, at least until you
change it with a `conda activate` or `conda deactivate` command or start a new
shell.

Use `conda env list` to discover the environments you have and the directories
in which they are installed.

## Setup a databroker catalog configuration

TODO

- use databroker to find default locations for config files
- create config file using assigned MongoDB catalog

## Setup version control with git

TODO

    git info
    # create github/gitlab repo
    # clone locally
    # add & commit content
    # push back to origin

## Setup configuring bluesky instrument

TODO

modify ~/bluesky/instrument/iconfig.yml`

- catalog name
- ...
