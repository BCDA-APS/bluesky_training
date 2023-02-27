# Conda environment for Bluesky

You might need to install a conda base environment if one is not already
available.  See [these instructions](./base.md) for the installation steps.

- [Conda environment for Bluesky](#conda-environment-for-bluesky)
  - [Install the environment](#install-the-environment)
  - [libmamba](#libmamba)
  - [Initialize shell for this base environment](#initialize-shell-for-this-base-environment)
  - [conda channels](#conda-channels)
  - [bash environment variables](#bash-environment-variables)

## Install the environment

With _normal_ ( not _elevated_) privileges, install the latest conda environment
for Bluesky.  Use the YAML (`.yml`) file to define the package requirements.

```bash
wget https://raw.githubusercontent.com/BCDA-APS/bluesky_training/main/bluesky/environments/environment_2023_2.yml
date -Iseconds
conda env create --force -f ./environment_2023_2.yml
date -Iseconds
```

## libmamba

In 2022, a [significant performance
enhancement](https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community)
was made available to `conda` by inclusion of the
[`conda-libmamba-solver`](https://conda.github.io/conda-libmamba-solver/)
package.  This package is added as part of the [base](./base.md) installation
instructions here and configured as the default solver.

Confirm which solver is default for your conda:

```bash
conda config --show solver
```

Set `libmamba` as the default solver:

```bash
conda config --set solver libmamba
```

## Initialize shell for this base environment

Initialize this base environment with each new login session:

```bash
conda init
```

## conda channels

Conda channels are URLs that provide conda packages for installation.

Show your default conda channels:

```bash
conda config --show channels
```

Add more conda channels:

```bash
conda config --env --append channels conda-forge 
conda config --env --append channels apsu
```

## bash environment variables

The [`blueskyStarter.sh`](../../blueskyStarter.sh) script looks for any of these
(bash shell) environment variables to choose the correct conda environment for
Bluesky.  It will search in the order below. Suggest setting one of these in
either `~/.bashrc` or `~/.bash_aliases`.

```bash
export BLUESKY_ENVIRONMENT=bluesky_2023_2
export BLUESKY_ENV=bluesky_2023_2
export BLUESKY_CONDA_ENV=bluesky_2023_2
```
