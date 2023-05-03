# Conda virtual environment

One way to control the versions of the packages used by your Python software is
to use Python virtual environments (`venv`s) or conda environments. This
document will describe the use of conda environments.

A bluesky instrument uses many Python packages not included in the Python
Standard Library.  Rather than add these directly into the system Python
installation, it is recommended to create a Python virtual environment which has
the suite of packages (and specific versions) required.

A Python virtual environment gives your account control over the suite of
installed packages and insulates you from any system software updates.

## Conda environment names

Each conda environment has a name, which corresponds to the file directory in
which the environments packages, libraries, and other resources are stored.  See
the table below for an example.

### base environment

You might need to install a conda base environment (such a
[Miniconda](https://docs.conda.io/en/latest/miniconda.html)) if one is not
already available.  See [these instructions](../reference/_conda_base.md) for
the installation steps.

Often, the base environment is installed read-only for normal users so they
cannot modify it directly.  Miniconda provides an ideal base environment since
it installs a minimal suite of Python packages, useful only the most basic
tasks, such as creating new, local environments for user.

### Bluesky environment

It is likely that you will have more than one conda environment available.  Each
of these has a complete installation of Python with a suite of packages.  The
suite may differ between the environments, as well as the package versions.
Even the Python version itself may be different.

<details>

Follow these
[steps](https://bcda-aps.github.io/bluesky_training/instrument/_install_new_instrument.html#create-the-conda-environment)
to create a conda environment for data collection with bluesky.

</details>

When you install or update package(s) in one environment, this will not affect
any of the other environments.  This makes it easy to control which software is
installed.

You can list the conda environments available (such as this example listing):

<pre>
$ <b>conda env list</b>
# conda environments:
#
bluesky_2022_3           /home/prjemian/.conda/envs/bluesky_2022_3
bluesky_2023_1           /home/prjemian/.conda/envs/bluesky_2023_1
bluesky_2023_2        *  /home/prjemian/.conda/envs/bluesky_2023_2
c2dv                     /home/prjemian/.conda/envs/c2dv
measComp                 /home/prjemian/.conda/envs/measComp
queue_server             /home/prjemian/.conda/envs/queue_server
test                     /home/prjemian/.conda/envs/test
training_2022            /home/prjemian/.conda/envs/training_2022
base                     /opt/miniconda3
</pre>

The environment with the `*` is the active one.  The full command prompt (not
shown here) will also be prefixed with the environment name, such as
`(bluesky_2023_2) `.

## Conda

Here, we describe the creation of a Python virtual environment managed by
[conda](https://docs.conda.io/projects/conda/en/latest/index.html).  While
opinions may vary, we see some advantages to using `conda` over
[`venv`](https://docs.python.org/3/library/venv.html).  Consequently, we use
`conda` to install most packages, falling back to `pip` to install any remaining
packages.  We use [YAML](https://yaml.org) files to describe these conda
environments.  See this
[article](https://medium.com/@balance1150/how-to-build-a-conda-environment-through-a-yaml-file-db185acf5d22)
for more instruction about conda environment YAML files.

If you need to install your own base environment, please See these
[instructions](../reference/_conda_base.md) to install your own base environment.

## Get the `conda` command

Skip ahead to the next section if you already have a `conda` command available
in your `bash` shell.  (This short
[Q&A](https://stackoverflow.com/questions/55134440) can help explain the
difference between a _conda base environment_ and _no environment at all_.)

<details>

If your (`bash` shell) command prompt does not start with `(base)` (or some
other conda aenvironment name), you probably do not have a conda environment
activated and probably do not have a `conda` command available.

Follow these steps:

1. Use the `bash` shell (sometimes, the comand prompt will change for bash):

   <pre>
   $ <b>bash</b>
   user@host:~$
   </pre>

2. Activate the `conda` base environment:

   <pre>
   $ <b>source /PATH/TO/CONDA/bin/activate</b>
   </pre>

   where `/PATH/TO/CONDA`  is the directory of your conda base installation.  At
   APS, that location is `/APSshare/miniconda/x86_64`.  For workstations on
   other networks, you may need to install
   [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or
   [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
   for yourself.

### conda channels

Conda channels are names (which are shortcuts to URLs) that provide conda
packages for installation.

Show your default conda channels:

```bash
conda config --show channels
```

Add more conda channels:

```bash
conda config --env --append channels conda-forge 
conda config --env --append channels apsu
```

### libmamba

In 2022, a [significant performance
enhancement](https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community)
was made available to `conda` by inclusion of the
[`conda-libmamba-solver`](https://conda.github.io/conda-libmamba-solver/)
package.  This package is added as part of the [base](../reference/_conda_base.md) installation
instructions here and configured as the default solver.

Install the libmamba solver in your conda environment:

```bash
conda install -c conda-forge libmamba
```

Confirm which solver is default for your conda:

```bash
conda config --show solver
```

Set `libmamba` as the default solver:

```bash
conda config --set solver libmamba
```

</details>

## Install the environment for bluesky

Using the new instrument as [setup](https://bcda-aps.github.io/bluesky_training/instrument/_install_new_instrument.html) above (with
`~/bluesky/` as the installation directory), look for the latest installation
configuration file in the `~bluesky/environments/` directory.  At this time, the
latest file is `environment_2023_2.yml`.

<details>

We create different versions of the YAML file, named for the APS operating cycle
(2021-1, 2023-2, ...), as the suite of packages for a working installation may
change over time.  By keeping all these files in a `environments/` subdirectory,
we can restore any of these environments with a simple command.

</details>

The instruction to (re)create the conda environment is in (a comment in) the
first few lines of the file:

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

<details>
<summary>Notes</summary>

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

</details>

Installation usually takes (at least) a few minutes to complete.

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

## Other reading

- [Getting started with conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)
- [conda environments - User Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html)
- [conda environments - Independent Guide](https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533)
- [Managing conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- [difference between base environment and no environment at all](https://stackoverflow.com/questions/55134440/)
- `venv`: [Python virtual environments](https://realpython.com/python-virtual-environments-a-primer/)
- [micromamba environments](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html)
