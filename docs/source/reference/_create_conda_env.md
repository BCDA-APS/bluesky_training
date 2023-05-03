# Create the conda environment

A bluesky instrument uses many Python packages not included in the Python
Standard Library.  Rather than add these directly into the system Python
installation, it is recommended to create a Python virtual environment which has
the suite of packages (and specific versions) required.

Follow these steps to create a conda environment for data collection with
bluesky.

**IMPORTANT**:  You must use `bash` shell.

TODO: add how to get the conda command (for APSshare and without)

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
[elsewhere](../reference/_conda_environment.md) in this repository.

TODO: how to create an alias to activate the bluesky environment (with access to APSshare vs not).

## bash environment variables

The `blueskyStarter.sh` script looks for the `BLUESKY_CONDA_ENV` (bash shell)
environment variable to choose the correct conda environment for Bluesky.
Suggest setting this in `~/.bash_aliases` (if that does not exist, then add it
to `~/.bashrc`).

```bash
export BLUESKY_CONDA_ENV=bluesky_2023_2
```