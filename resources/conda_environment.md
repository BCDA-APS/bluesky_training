# Setup a conda environment

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

## Get the `conda` command

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

## Install the environment for bluesky

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

**Notes**:

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
