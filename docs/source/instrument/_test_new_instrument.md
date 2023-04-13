# Test the New Bluesky Instrument

At this point, you have assembled enough of the parts to test the initial
installation with bluesky. Follow these steps:

<pre>
$ <b>cd ~/bluesky</b>
$ <b>conda activate bluesky_2023_2</b>
$ <b>ipython</b>
Python 3.10.9 | packaged by conda-forge | (main, Feb  2 2023, 20:20:04) [GCC 11.3.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.11.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
</pre>

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
I Mon-14:43:28 - CONDA_PREFIX = /home/user/.conda/envs/bluesky_2023_2
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

The time-stamped lines that start with `I ` are `Information` log messages from the logger.  The logger levels are:

starting | meaning
--- | ---
`E ` | error
`W ` | warning
`I ` | information (default)
`D ` | debugging (lots of detail!)

The logger output to the terminal is intentionally terse.  Greater detail may be available in log files in the `.logs/` subdirectory.

Load the `Hello, World!` example from the `user/` code directory:

<pre>
In [2]: <b>%run -i user/quick_hello.py</b>
Loading 'Hello, World!' example.

In [3]: 
</pre>

**Note**: The `Loading 'Hello, World!' example.` text came from a `print()` statement in the file.

This also loads `hello_world()`, a demonstration bluesky *plan*.  Run that plan with the bluesky RunEngine instance `RE`:

<pre>
In [3]: <b>RE(hello_world())</b>


Transient Scan ID: 877     Time: 2023-03-13 14:51:21
Persistent Unique Scan ID: '76e1f4c4-5e46-47ee-bfb2-729b183f3367'
New stream: 'primary'
+-----------+------------+------------+
|   seq_num |       time |      hello |
+-----------+------------+------------+
|         1 | 14:51:21.8 |          1 |
+-----------+------------+------------+
generator count ['76e1f4c4'] (scan num: 877)
Out[3]: ('76e1f4c4-5e46-47ee-bfb2-729b183f3367',)

In [4]: 
</pre>

We're using a temporary databroker catalog (as logged in the startup above). The
data from this run is available until we quite the IPython session. Let's take a
look at the data.  First, get a reference to the *run* from the databroker
catalog reference `cat`:

<pre>
In [4]: <b>run = cat[-1]</b>
</pre>

Show a brief description of that `run`:

<pre>
In [5]: <b>run</b>
Out[5]: 
BlueskyRun
  uid='76e1f4c4-5e46-47ee-bfb2-729b183f3367'
  exit_status='success'
  2023-03-13 14:51:21.874 -- 2023-03-13 14:51:21.880
  Streams:
    * primary
</pre>

The run's data is in the `primary` stream.  Show it:

<pre>
In [6]: <b>run.primary.read()</b>
Out[6]: 
&lt;xarray.Dataset>
Dimensions:     (time: 1)
Coordinates:
  * time        (time) float64 1.679e+09
Data variables:
    hello       (time) int64 1
    hello_text  (time) &lt;U13 'Hello, World!'
</pre>

Congratulations!  You've tested your new bluesky instrument.
