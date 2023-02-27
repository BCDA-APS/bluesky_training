# Conda environments

One way to control the versions of the packages used by your Python software is
to use Python virtual environments (`venv`s) or conda environments. This
document will describe the use of conda environments.

- [Conda environments](#conda-environments)
  - [base environment](#base-environment)
  - [Bluesky environment](#bluesky-environment)
  - [testing](#testing)
  - [Other reading](#other-reading)

## base environment

You might need to install a conda base environment (such a
[Miniconda](https://docs.conda.io/en/latest/miniconda.html)) if one is not
already available.  See [these instructions](./base.md) for the installation
steps.

Often, the base environment is installed read-only for normal users so they
cannot modify it directly.  Miniconda provides an ideal base environment since
it installs a minimal suite of Python packages, useful only the most basic
tasks, such as creating new, local environments for user.

## Bluesky environment

See these [instructions](./bluesky.md) to install a conda environment for Bluesky.

It is likely that you will have more than one conda environment available.  Each
of these has a complete installation of Python with a suite of packages.  The
suite may differ between the environments, as well as the package versions.
Even the Python version itself may be different.

When you install or update package(s) in one environment, this will not affect
any of the other environments.  This makes it easy to control which software is
installed.

You can list the conda environments available (such as this example listing):

```bash
(bluesky_2023_2) prjemian@zap:~/bluesky$ conda env list
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
```

The environment with the `*` is the activate one.  This is also described in the
command prompt.

## testing

You may find these [instructions](./testing.md) useful if you wish to test your
conda environment.

## Other reading

- [Getting started with conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)
- [conda environments - User Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html)
- [conda environments - Independent Guide](https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533)
- [Managing conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- [difference between base environment and no environment at all](https://stackoverflow.com/questions/55134440/)
- `venv`: [Python virtual environments](https://realpython.com/python-virtual-environments-a-primer/)
- [micromamba environments](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html)
