# Installation

Describes the steps to install a new instrument.

**Note**:  These *instructions have been written for workstations running the
Linux operating system*.  They may be used for other operating systems but
expect some modifications are necessary.  One such modification is that the
`libhkl` library, needed for diffractometer support, is only available for Linux
x86_64 host architectures.

**IMPORTANT**: In Linux, use the `bash` command shell.

## Setup a bluesky instrument

Use the `new_bluesky_instrument.py`
[program](https://github.com/BCDA-APS/bluesky_training/blob/main/resources/new_bluesky_instrument.py)
to install a new bluesky instrument configuration from the online [APS Bluesky
Training](https://github.com/BCDA-APS/bluesky_training) repository template.

**Note**: APS users can run this program with this command to create a new
`bluesky` directory in their home directory:

<pre>
<b>python /APSshare/bin/new_bluesky_instrument.py ~/bluesky</b>
</pre>

Workstations on other networks will need to download this program from the URL
above.

`new_bluesky_instrument.py` only needs Python 3.6+ and the
[requests](https://docs.python-requests.org/en/latest/index.html) package.

Here's an example:

<pre>
$ <b>python new_bluesky_instrument.py  ./bluesky</b>
INFO:__main__:Requested installation to: 'bluesky'
INFO:__main__:Downloading 'https://github.com/BCDA-APS/bluesky_training/archive/refs/heads/main.zip'
INFO:__main__:Extracting content from '/tmp/bluesky_training-main.zip'
INFO:__main__:Installing to '/home/user/bluesky'
</pre>

Use `new_bluesky_instrument.py -h` for usage information.

The installer will download the ZIP file from the GitHub training repository if
it's not already present in the `/tmp` directory or if the existing file is old.

## Create the conda environment

A bluesky instrument uses many Python packages not included in the Python
Standard Library.  Rather than add these directly into the system Python
installation, it is recommended to create a Python virtual environment which has
the suite of packages (and specific versions) required.

Follow these steps to create a conda environment for data collection with
bluesky.

**IMPORTANT**:  You must use `bash` shell.

Here's an example for the `bluesky_2023_2` environment:

<pre>
$ <b>cd ~/bluesky</b>
$ <b>conda env create \
    --force \
    -n bluesky_2023_2 \
    -f ./environments/environment_2023_2.yml \
    --solver=libmamba</b>
</pre>

<details>

In the commands above, a long command has been split over several lines to make
it clearer to read and also to take less screen width. We could enter the
<code>conda env</code> command all one one line.  These commands work the same
as the one above.

<pre>
$ <b>cd ~/bluesky</b>
$ <b>conda env create --force -n bluesky_2023_2 -f ./environments/environment_2023_2.yml --solver=libmamba</b>
</pre>

</details>

The [`blueskyStarter.sh`](../instrument/_directory_layout.rst) script looks for the
`BLUESKY_CONDA_ENV` (bash shell) environment variable to choose the correct
conda environment for Bluesky.  Suggest setting this in `~/.bash_aliases` (if
that does not exist, then add it to `~/.bashrc`).

```bash
export BLUESKY_CONDA_ENV=bluesky_2023_2
alias become_bluesky='conda activate ${BLUESKY_CONDA_ENV}'
```

More documentation about [conda](../reference/_conda_base.md) is available
[elsewhere](../instrument/_conda_environment.md) in this repository.

### bash environment variables

The `blueskyStarter.sh` script looks for the `BLUESKY_CONDA_ENV` (bash shell)
environment variable to choose the correct conda environment for Bluesky.
Suggest setting this in `~/.bash_aliases` (if that does not exist, then add it
to `~/.bashrc`).

```bash
export BLUESKY_CONDA_ENV=bluesky_2023_2
```

## Activate the conda environment

As shown above, you will need to activate the conda environment in each console
session when you plan to use it.  Here's an example:

<pre>
$ <b>conda activate bluesky_2023_2</b>
</pre>

This activation will remain for the duration of the session, at least until you
change it with a `conda activate` or `conda deactivate` command or start a new
shell.

Use `conda env list` to discover the environments you have and the directories
in which they are installed.

## Test the new bluesky instrument

At this point, you have assembled enough of the parts to test the initial
installation with bluesky. Follow the steps in this
[guide](./_test_new_instrument.md) to test the installation.  
Additional instructions are available to
[test](./_testing.md) the installation with EPICS.

In the remaining steps, we'll configure the instrument for your catalog and
specific hardware configuration.

## Setup your databroker catalog configuration

Contact BCDA (bcda@aps.anl.gov) for assignment of a databroker catalog
configuration.

Let's assume (for example purposes), you have been given this bluesky/databroker
catalog assignment:

- name: `45ida_abcd`
- MongoDB server: `mongoserver.xray.aps.anl.gov`
- MongoDB collection: `45ida_abcd-bluesky`

See this [guide](./_configure_databroker.md) to configure databroker.

Confirm that databroker can find the `45ida_abcd` catalog (by running the python
executable and passing the python commands as a command-line option):

<pre>
$ <b>python -c "import databroker; print(list(databroker.catalog))"</b>
['45ida_abcd']
</pre>

## IPython profile

If there is an existing `~/.ipython` directory (perhaps created for other use
from this account), then choose a unique directory for bluesky.  Typical
alternative is `~/.ipython-bluesky`.  These bash script commands create the
[IPython profile](https://ipython.readthedocs.io/en/stable/config/intro.html)
for bluesky, then create a starter script for the `instrument` package within
that profile's `startup` directory.

```bash
ipython profile create bluesky --ipython-dir="~/.ipython"
cat > ~/.ipython/profile_bluesky/startup/00-start-bluesky.py  << EOF
import pathlib, sys
sys.path.append(str(pathlib.Path().home() / "bluesky"))
from instrument.collection import *
EOF
```

## Start version control

While this step is optional, it is **highly recommended** that you place your
bluesky instrument directory under some form of software version control.  At
minimum, this can provide some form of backup protection.  It also helps others
to collaborate with similar bluesky instruments by sharing your instrument's
implementations.

Instructions for using [`git`](https://git-scm.com/) as software version control
with [GitHub](https://github.com/) or the
[APS GitLab server](https://git.aps.anl.gov/) are provided in
[this separate document](../reference/_git-help.rst).

## Configure bluesky instrument

See this [advice](./_configure_bluesky_instrument.md) for configuration of the
`instrument` package (content in the `instrument/` directory).
