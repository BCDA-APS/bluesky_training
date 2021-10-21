# First steps with bluesky-queueserver

Starting with the [bluesky-queueserver web
documentation](https://blueskyproject.io/bluesky-queueserver/cli_tools.html),
make a quick demonstration of what it can do out of the box from the linux
command line.

CONTENTS

- [First steps with bluesky-queueserver](#first-steps-with-bluesky-queueserver)
  - [One-time setup](#one-time-setup)
  - [Start a monitor on a qserver](#start-a-monitor-on-a-qserver)
  - [Run plans on the qserver](#run-plans-on-the-qserver)
    - [Available devices and plans](#available-devices-and-plans)
    - [Count](#count)
    - [Scan](#scan)
  - [Shutdown the queue server](#shutdown-the-queue-server)

## One-time setup

Install `redis` package in OS (if not already installed):

```bash
sudo apt install redis
```

Create conda environment

```bash
conda create -y -n qserver -c conda-forge bluesky-queueserver
```

## Start a monitor on a qserver

In a separate terminal:

```bash
conda activate qserver
start-re-manager --zmq-publish-console ON --databroker-config training
```

Here, the `training` catalog is subscribed to the RunEngine, in addition to a 0MQ stream (on port tcp://*:60615).

<details>

```
(qserver) prjemian@zap:~$ start-re-manager --zmq-publish-console ON --databroker-config training
INFO:bluesky_queueserver.manager.manager:Starting ZMQ server at 'tcp://*:60615'
INFO:bluesky_queueserver.manager.manager:ZMQ control channels: encryption disabled
INFO:bluesky_queueserver.manager.manager:Starting RE Manager process
INFO:bluesky_queueserver.manager.manager:Loading the lists of allowed plans and devices ...
INFO:bluesky_queueserver.manager.manager:Starting ZeroMQ server ...
INFO:bluesky_queueserver.manager.manager:ZeroMQ server is waiting on tcp://*:60615
```

</details>

## Run plans on the qserver

In a separate terminal ...

Get a queue started:

```bash
conda activate qserver
qserver queue start
qserver environment open
```

### Available devices and plans

Without any local configuration, the `bluesky-queueserver` starts with devices from  the ophyd simulators and the standard bluesky plans.

These commands show (in JSON) what is available:

```bash
qserver allowed devices
qserver allowed plans
```

### Count

Add a plan to count from two detectors (from the ophyd simulators):

```bash
qserver queue add plan '{"name": "count", "args": [["det1", "det2"]], "kwargs": {"num": 10, "delay": 1, "md": {"purpose": "test bluesky-queueserver"}}}'
```

The monitor shows this response:

<details>

```text
INFO:bluesky_queueserver.manager.manager:Adding new item to the queue ...
INFO:bluesky_queueserver.manager.manager:Item added: success=True item_type='plan' name='count' item_uid='33487d7a-d1c8-4639-9a77-eef753a79c8b' qsize=1.
```

</details>

Check the queue of plans to be run:

```bash
(qserver) prjemian@zap:~$ qserver queue get
Arguments: ['queue', 'get']
13:02:44 - MESSAGE: {'items': [{'args': [['det1', 'det2']],
            'item_type': 'plan',
            'item_uid': '33487d7a-d1c8-4639-9a77-eef753a79c8b',
            'kwargs': {'delay': 1,
                       'md': {'purpose': 'test bluesky-queueserver'},
                       'num': 10},
            'name': 'count',
            'user': 'qserver-cli',
            'user_group': 'admin'}],
 'msg': '',
 'plan_queue_uid': '40dc1e75-11b8-4331-8a03-24d5dff9f459',
 'running_item': {},
 'success': True}
```

Start running the queue:

```bash
qserver queue start
```

The monitor window shows this response:

<details>

```text
INFO:bluesky_queueserver.manager.manager:Starting queue processing ...
INFO:bluesky_queueserver.manager.manager:Processing the next queue item: 1 plans are left in the queue.
INFO:bluesky_queueserver.manager.manager:Starting the plan:
{'args': [['det1', 'det2']],
 'item_uid': '33487d7a-d1c8-4639-9a77-eef753a79c8b',
 'kwargs': {'delay': 1,
            'md': {'purpose': 'test bluesky-queueserver'},
            'num': 10},
 'meta': {},
 'name': 'count',
 'user': 'qserver-cli',
 'user_group': 'admin'}.
INFO:bluesky_queueserver.manager.worker:Starting execution of a plan ...
INFO:bluesky_queueserver.manager.worker:Starting a plan 'count'.
INFO:bluesky_queueserver.manager.plan_monitoring:New run was open: 'dc48f1b8-6f98-4da4-922e-4daff406849a'


Transient Scan ID: 1     Time: 2021-10-21 13:05:16
Persistent Unique Scan ID: 'dc48f1b8-6f98-4da4-922e-4daff406849a'
New stream: 'primary'
+-----------+------------+------------+------------+
|   seq_num |       time |       det1 |       det2 |
+-----------+------------+------------+------------+
|         1 | 13:05:16.8 |      5.000 |      1.765 |
|         2 | 13:05:17.8 |      5.000 |      1.765 |
|         3 | 13:05:18.8 |      5.000 |      1.765 |
|         4 | 13:05:19.8 |      5.000 |      1.765 |
|         5 | 13:05:20.8 |      5.000 |      1.765 |
|         6 | 13:05:21.8 |      5.000 |      1.765 |
|         7 | 13:05:22.8 |      5.000 |      1.765 |
|         8 | 13:05:23.8 |      5.000 |      1.765 |
|         9 | 13:05:24.8 |      5.000 |      1.765 |
|        10 | 13:05:25.8 |      5.000 |      1.765 |
Run was closed: 'dc48f1b8-6f98-4da4-922e-4daff406849a'
+-----------+------------+------------+------------+
generator count ['dc48f1b8'] (scan num: 1)



INFO:bluesky_queueserver.manager.manager:No items are left in the queue.
INFO:bluesky_queueserver.manager.manager:Queue is empty.
```

</details>

Check the queue now:

```bash
(qserver) prjemian@zap:~$ qserver queue get
Arguments: ['queue', 'get']
13:06:11 - MESSAGE: {'items': [],
 'msg': '',
 'plan_queue_uid': '747545db-a402-4568-9282-74eeb2f1ebf1',
 'running_item': {},
 'success': True}
```

In a new terminal window, check if we can see that run in our databroker:

```bash
conda activate qserver
ipython
```

<details>

```ipython
In [1]: import databroker
   ...: cat = databroker.catalog["training"]
   ...: run = cat[-1]
   ...: run
   ...:
Out[1]:
BlueskyRun
  uid='dc48f1b8-6f98-4da4-922e-4daff406849a'
  exit_status='success'
  2021-10-21 13:05:16.819 -- 2021-10-21 13:05:26.847
  Streams:
    * primary


In [2]: run.primary.read()
Out[2]:
<xarray.Dataset>
Dimensions:  (time: 10)
Coordinates:
  * time     (time) float64 1.635e+09 1.635e+09 ... 1.635e+09 1.635e+09
Data variables:
    det1     (time) float64 5.0 5.0 5.0 5.0 5.0 5.0 5.0 5.0 5.0 5.0
    det2     (time) float64 1.765 1.765 1.765 1.765 ... 1.765 1.765 1.765 1.765
```

</details>

That's our run!

### Scan

Pick the `noisy_det` and `motor1` from the ophyd simulators:

```bash
qserver queue add plan '{"name": "scan", "args": [["noisy_det"], "motor1", 0, 1, 5 ], "kwargs": {"md": {"purpose": "test bluesky-queueserver"}}}'
```

Start the queue again:

```bash
qserver queue start
```

Response (in monitor window):

<details>

```text
INFO:bluesky_queueserver.manager.manager:Starting queue processing ...
INFO:bluesky_queueserver.manager.manager:Processing the next queue item: 1 plans are left in the queue.
INFO:bluesky_queueserver.manager.manager:Starting the plan:
{'args': [['noisy_det'], 'motor1', 0, 1, 5],
 'item_uid': '9c10c3f2-2214-4a70-b3e8-8be4170e68be',
 'kwargs': {'md': {'purpose': 'test bluesky-queueserver'}},
 'meta': {},
 'name': 'scan',
 'user': 'qserver-cli',
 'user_group': 'admin'}.
INFO:bluesky_queueserver.manager.worker:Starting execution of a plan ...
INFO:bluesky_queueserver.manager.worker:Starting a plan 'scan'.


Transient Scan ID: 2     Time: 2021-10-21 13:17:04
Persistent Unique Scan ID: '0e076f4d-c7c3-4a59-bc7f-8fcc636e5d4b'
INFO:bluesky_queueserver.manager.plan_monitoring:New run was open: '0e076f4d-c7c3-4a59-bc7f-8fcc636e5d4b'
New stream: 'primary'
+-----------+------------+------------+------------+
|   seq_num |       time |     motor1 |  noisy_det |
+-----------+------------+------------+------------+
|         1 | 13:17:04.2 |      0.000 |      1.028 |
|         2 | 13:17:04.2 |      0.250 |      0.932 |
Run was closed: '0e076f4d-c7c3-4a59-bc7f-8fcc636e5d4b'
|         3 | 13:17:04.2 |      0.500 |      0.993 |
|         4 | 13:17:04.2 |      0.750 |      0.953 |
|         5 | 13:17:04.2 |      1.000 |      0.975 |
+-----------+------------+------------+------------+
generator scan ['0e076f4d'] (scan num: 2)



INFO:bluesky_queueserver.manager.manager:No items are left in the queue.
INFO:bluesky_queueserver.manager.manager:Queue is empty.
```

</details>

## Shutdown the queue server

```bash
qserver manager stop safe on
```

Note in the monitor window tells the monitor to shutdown:

<details>

```text
INFO:bluesky_queueserver.manager.worker:Closing RE Worker environment ...
INFO:bluesky_queueserver.manager.worker:Environment is waiting to be closed ...
INFO:bluesky_queueserver.manager.manager:Waiting for exit confirmation from RE worker ...
INFO:bluesky_queueserver.manager.worker:Run Engine environment was closed successfully
INFO:bluesky_queueserver.manager.manager:Wait for RE Worker process to close (join)
INFO:bluesky_queueserver.manager.start_manager:Joining RE Worker ...
INFO:bluesky_queueserver.manager.manager:RE Manager was stopped by ZMQ command.
INFO:bluesky_queueserver.manager.start_manager:RE Watchdog is stopped
(qserver) prjemian@zap:~$
```

</details>
