# Create the conda environment

A bluesky instrument uses many Python packages not included in the Python
Standard Library.  Rather than add these directly into the system Python
installation, it is recommended to create a Python virtual environment which has
the suite of packages (and specific versions) required.

Follow these steps to create a conda environment for data collection with
bluesky.

**IMPORTANT**:  You must use `bash` shell. For more info
see [what is
bash?](https://bcda-aps.github.io/bluesky_training/reference/_FAQ.html#faq-bash>)


## Activate conda

- On a machine with access to APSshare, type the command:

    <pre>$ <b>source /APSshare/miniconda/x86_64/bin/activate</b></pre>

    If you are getting an error, contact the Bluesky support team.

- On a machine with no access to APSshare, type the command:

     <pre>$ <b>`which conda`</b></pre>

    If the output prints the path to conda, you can activate it by using:

    <pre>$ <b>source /PATH/TO/CONDA/bin/activate</b></pre>

    However, if the command `which conda` does not return anything, or if you are getting an error message (`bash: conda: command not found`
    or `bash: activate: No such file or directory`), conda is not
    installed on your computer or it is not added to the system's PATH
    environment variable.    

    You can install conda by following the installation instructions
    for your operating system. You can find the instructions for Windows,
    macOS, and Linux on the official conda documentation
    [website](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

    If you still encounter the same error message after installing conda, you may need to add the conda installation directory to your system's PATH environment variable manually. You can find instructions on how to do this in the Conda documentation.



When `conda` is activated, the prompt changes to displays `(base)`. Now you can use
`conda env list` to see the environments you have and the directories
in which they are installed.

Note that more documentation about [conda](../reference/_conda_base.md) is available
[elsewhere](../reference/_conda_environment.md) in this repository.

## Install the bluesky environment
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
<br>

## Create an alias to activate the bluesky environment

The [`blueskyStarter.sh`](https://bcda-aps.github.io/bluesky_training/instrument/_getting_started.html) script looks for the
`BLUESKY_CONDA_ENV` (bash shell) environment variable to choose the correct
conda environment for Bluesky.  Suggest setting this in `~/.bash_aliases` (if
that does not exist, then add it to `~/.bashrc`).

```bash
export BLUESKY_CONDA_ENV=bluesky_2023_2
alias become_bluesky='conda activate ${BLUESKY_CONDA_ENV}'
```


TODO: how to create an alias to activate the bluesky environment (with access to APSshare vs not) and add to FAQ.

The `blueskyStarter.sh` script looks for the `BLUESKY_CONDA_ENV` (bash shell)
environment variable to choose the correct conda environment for Bluesky.
Suggest setting this in `~/.bash_aliases` (if that does not exist, then add it
to `~/.bashrc`).

```bash
export BLUESKY_CONDA_ENV=bluesky_2023_2
```