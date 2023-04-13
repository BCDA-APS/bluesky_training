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

With _normal_ (not _elevated_) privileges, install the latest conda environment
for Bluesky.  Use the YAML (`.yml`) file to define the package requirements.

```bash
wget https://raw.githubusercontent.com/BCDA-APS/bluesky_training/main/bluesky/environments/environment_2023_2.yml
date -Iseconds
conda env create --force -f ./environment_2023_2.yml
date -Iseconds
```

## libmamba

Note: content moved to `docs/source/reference/_conda_environment`

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

The [`blueskyStarter.sh`](/bluesky/blueskyStarter.sh) script looks for the
`BLUESKY_CONDA_ENV` (bash shell) environment variable to choose the correct
conda environment for Bluesky.  Suggest setting this in `~/.bash_aliases` (if
that does not exist, then add it to `~/.bashrc`).

```bash
export BLUESKY_CONDA_ENV=bluesky_2023_2
```
