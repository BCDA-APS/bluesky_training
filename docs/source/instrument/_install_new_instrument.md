# Installation

Describes the steps to install a new bluesky instrument.

**Note**:  These *instructions have been written for workstations running the
Linux operating system*.  They may be used for other operating systems but
expect some modifications are necessary.  One such modification is that the
`libhkl` library, needed for diffractometer support, is only available for Linux
x86_64 host architectures.

**IMPORTANT**: In Linux, use the `bash` command shell.

<details>
<summary>What is <b>bash</b>?</summary>

 Bash is a type of shell, which is a program that provides a user interface for accessing the operating system's services.

To determine if you're using Bash, you can open up a terminal or command prompt on your computer and type in the following command:

<pre>
$ <b>echo $SHELL</b>
</pre>
 If the output is "/bin/bash" or something similar, then you're using the Bash shell.

If bash is not your default shell, type in the following command in a terminal to start a new instance of the Bash shell:

<pre>
$ <b>bash</b>
</pre>

 Press enter, and you should see a new prompt indicating that you're now using the Bash shell. You can now type in Bash commands. 
 Note that any changes you make to your environment variables or other system settings within this Bash session will only apply to this session and will not persist after you close the session. To change your default shell, contact your IT support. 

</details>
<br>

## Setup a bluesky instrument

Use the `new_bluesky_instrument.py`
[program](https://github.com/BCDA-APS/bluesky_training/blob/main/new_bluesky_instrument.py)
to install a new bluesky instrument configuration from the online [APS Bluesky
Training](https://github.com/BCDA-APS/bluesky_training) repository template. The program creates a new
`bluesky` directory in the home directory. 
Use `new_bluesky_instrument.py -h` for usage information.


The `new_bluesky_instrument.py` program requires Python 3.6+ and the
[requests](https://docs.python-requests.org/en/latest/index.html) package.

<details>
<summary>How can I tell the <b>python</b> version I am using?</summary>
Type the following command:

<pre>
$ <b>python --version</b>
</pre>
This will print the version of Python currently installed on your system. If you need to upgrade python, see [here](https://www.python.org/downloads/). 

</details>

<details>
<summary>How can I tell if the <b>requests</b> pacakage is installed?</summary>

In a terminal, launch Python by typing `python` or `python3` followed by Enter.

Type the following command and press Enter:
<pre>
$ <b>import requests</b>
</pre>
If the command runs without any errors, then you have the Requests package installed. If you don't have the package installed, you'll see an error message like `"ModuleNotFoundError: No module named 'requests'"`. 


</details>
<br>

To run the program:

<details>
<summary>On an APS machine with access to APSshare</summary>

This command can be run directly from a terminal:
<pre>
$ <b>python /APSshare/bin/new_bluesky_instrument.py ~/bluesky</b>
</pre>
</details>

<details>
<summary>On a machine with no access to APSshare</summary>
Workstations on other networks will need to download this program from the URL
above. Navigate to the directory where the program was downlowded and run the following command:

<pre>
$ <b>python new_bluesky_instrument.py ~/bluesky</b>
</pre>

</details>
<br>



When run successfully, the program output should look like this:

<pre>
INFO:__main__:Requested installation to: 'bluesky'
INFO:__main__:Downloading 'https://github.com/BCDA-APS/bluesky_training/archive/refs/heads/main.zip'
INFO:__main__:Extracting content from '/tmp/bluesky_training-main.zip'
INFO:__main__:Installing to '/home/user/bluesky'
</pre>

The installer downloads the ZIP file from the GitHub training repository if
it's not already present in the `/tmp` directory or if the existing file is old.


## Activate the bluesky conda environment

<details>
<summary> How to create a conda environment for bluesky?</summary>

See [here](./_create_conda_env.md).
</details>

<details>
<summary> How do I know if I have a conda environment for bluesky?</summary>

- **On a machine with access to APSshare:** Type the command `source /APSshare/miniconda/x86_64/bin/activate`
- **On a machine with no access to APSshare:** Type the command `conda activate`. If you are using an older version of conda, you may need to use the `source` command instead: `source activate`.

The prompt changes to displays `(base)`. Now you can use `conda env list` to see the environments you have and the directories in which they are installed.

If you are getting an error message (`bash: conda: command not found` or `bash: activate: No such file or directory`), conda is not installed on your computer or it is not added to the system's PATH environment variable.

You can try to install conda by following the installation instructions for your operating system. You can find the instructions for Windows, macOS, and Linux on the official conda documentation [website](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

Once conda is installed, you can activate it by opening a new terminal or command prompt and typing `conda activate`. If you still encounter the same error message, you may need to add the conda installation directory to your system's PATH environment variable manually. You can find instructions on how to do this in the Conda documentation. 

</details>

<br>
To use bluesky, you need to activate the bluesky conda environment.  Here's an example:

<pre>
$ <b>conda activate bluesky_2023_2</b>
</pre>
The prompt changes to display `(bluesky_2023_2)` . 

This activation will remain  in effect for the duration of the session (*i.e.* as long as the terminal stays open), unless you activate a different environment or deactivate it using the `conda deactivate` command.



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
