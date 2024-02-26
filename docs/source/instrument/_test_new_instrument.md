# Test the New Bluesky Instrument

Test the new bluesky instrument package.

<details>
<summary>How to install a new instrument?</summary>

Visit <a href=https://bcda-aps.github.io/bluesky_training/instrument/_install_new_instrument.html> Bluesky Installation</a>.
</details>

<details>
<summary>How to test my Bluesky installation?</summary>
Test (verify) the installation by running the <a
href=https://bcda-aps.github.io/bluesky_training/tutor/hello_world.html>Hello, World!</a>
tutorial.
</details>

<br>

Navigate to the in the `~/bluesky` directory:

<pre>
$ <b>cd ~/bluesky</b>
</pre>

and start a Bluesky session (TODO add link).





<details>
<summary>What does the (~) means in <b>~/bluesky</b>?</summary>
The tilde (~) character represents the current user's home directory. This is a shortcut that can be used to specify file paths without having to type out the entire path to the home directory.
</details>

<br>

Load the `instrument` package for data collection activities.  The name of each module is logged as it is loaded.

<pre>
In [1]: <b>from instrument.collection import *</b>
/home/user/bluesky/instrument/_iconfig.py
Activating auto-logging. Current session state plus future input saved.
Filename       : /home/user/bluesky/.logs/ipython_console.log
Mode           : rotate
Output logging : True
Raw input log  : False
Timestamping   : True
State          : active
I Mon-14:43:28 - Console logging: /home/user/bluesky/.logs/ipython_console.log
I Mon-14:43:28 - ############################################################ startup
I Mon-14:43:28 - logging started
I Mon-14:43:28 - logging level = 10
I Mon-14:43:28 - /home/user/bluesky/instrument/session_logs.py
I Mon-14:43:28 - /home/user/bluesky/instrument/collection.py
I Mon-14:43:28 - CONDA_PREFIX = /home/user/.conda/envs/bluesky_2023_3
Exception reporting mode: Minimal
I Mon-14:43:28 - xmode exception level: 'Minimal'
I Mon-14:43:28 - /home/user/bluesky/instrument/mpl/console.py
I Mon-14:43:28 - #### Bluesky Framework ####
I Mon-14:43:28 - /home/user/bluesky/instrument/framework/check_python.py
I Mon-14:43:28 - /home/user/bluesky/instrument/framework/check_bluesky.py
I Mon-14:43:30 - /home/user/bluesky/instrument/framework/initialize.py
I Mon-14:43:30 - using TEMPORARY databroker catalog 'temp'
I Mon-14:43:30 - using ophyd control layer: pyepics
I Mon-14:43:30 - /home/user/bluesky/instrument/framework/metadata.py
I Mon-14:43:30 - /home/user/bluesky/instrument/epics_signal_config.py
I Mon-14:43:30 - Using RunEngine metadata for scan_id
I Mon-14:43:30 - #### Devices ####
I Mon-14:43:30 - #### Callbacks ####
I Mon-14:43:30 - /home/user/bluesky/instrument/callbacks/spec_data_file_writer.py
I Mon-14:43:30 - #### Plans ####
I Mon-14:43:30 - #### Utilities ####
I Mon-14:43:30 - /home/user/bluesky/instrument/utils/image_analysis.py
I Mon-14:43:30 - writing to SPEC file: /home/user/bluesky/20230313-144330.dat
I Mon-14:43:30 -    >>>>   Using default SPEC file name   <<<<
I Mon-14:43:30 -    file will be created when bluesky ends its next scan
I Mon-14:43:30 -    to change SPEC file, use command:   newSpecFile('title')
I Mon-14:43:30 - #### Startup is complete. ####

In [2]:
</pre>

The time-stamped lines that start with `I ` are `Information` log messages from the logger.
<details>
<summary>More about the logger</summary>
The logger levels are:

starting | meaning
--- | ---
`E ` | error
`W ` | warning
`I ` | information (default)
`D ` | debugging (lots of detail!)

The logger output to the terminal is intentionally terse.  Greater detail may be available in log files in the `.logs/` subdirectory.

</details>

<br>

The IPython output should end with  the message: 

<pre>#### Startup is complete. ####
</pre>



Congratulations!  You've tested your new bluesky instrument.
