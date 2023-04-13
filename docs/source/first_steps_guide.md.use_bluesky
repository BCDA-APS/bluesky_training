# Guide: First Steps with Bluesky

This is a quick-reference guide for those learning how
to use the Bluesky Framework for data acquisition.

Use these commands to verify the existing configuration works as expected:

  * motors have values matching EPICS
  * scaler(s) match EPICS

**Contents**
- [Guide: First Steps with Bluesky](#guide-first-steps-with-bluesky)
  - [Read](#read)
  - [Move](#move)
  - [Count](#count)
  - [List, Describe, Summary](#list-describe-summary)
  - [Bluesky Plans _vs_. Command-line Actions](#bluesky-plans-vs-command-line-actions)
  - [Log files](#log-files)

## Read

command | description
--- | ---
`OBJECT.get()` | low-level command to show value of ophyd *Signal* named `OBJECT`
`OBJECT.read()` | data acquisition command, includes timestamp
`listdevice(OBJECT)` | table-version of `.read()`
`MOTOR.position` | get readback, only for motor objects
`MOTOR.user_readback.get()` | alternative to `MOTOR.position`
`OBJECT.summary()` | more information about `OBJECT`

<details>
<summary>Examples:</summary>

```python
In [10]: m1.user_setpoint.get()
Out[10]: 0.0

In [11]: m1.user_setpoint.read()
Out[11]: {'m1_user_setpoint': {'value': 0.0, 'timestamp': 1613878949.1092}}

In [12]: listdevice(m1)
================ ===== ==========================
name             value timestamp                 
================ ===== ==========================
m1               0.0   2021-02-20 21:42:29.109200
m1_user_setpoint 0.0   2021-02-20 21:42:29.109200
================ ===== ==========================

Out[12]: <pyRestTable.rest_table.Table at 0x7fe0649cbd00>

In [13]: m1.position
Out[13]: 0.0

In [14]: m1.summary()
data keys (* hints)
-------------------
*m1
 m1_user_setpoint

read attrs
----------
user_readback        EpicsSignalRO       ('m1')
user_setpoint        EpicsSignal         ('m1_user_setpoint')

config keys
-----------
m1_acceleration
m1_motor_egu
m1_user_offset
m1_user_offset_dir
m1_velocity

configuration attrs
-------------------
user_offset          EpicsSignal         ('m1_user_offset')
user_offset_dir      EpicsSignal         ('m1_user_offset_dir')
velocity             EpicsSignal         ('m1_velocity')
acceleration         EpicsSignal         ('m1_acceleration')
motor_egu            EpicsSignal         ('m1_motor_egu')

unused attrs
------------
offset_freeze_switch EpicsSignal         ('m1_offset_freeze_switch')
set_use_switch       EpicsSignal         ('m1_set_use_switch')
motor_is_moving      EpicsSignalRO       ('m1_motor_is_moving')
motor_done_move      EpicsSignalRO       ('m1_motor_done_move')
high_limit_switch    EpicsSignalRO       ('m1_high_limit_switch')
low_limit_switch     EpicsSignalRO       ('m1_low_limit_switch')
high_limit_travel    EpicsSignal         ('m1_high_limit_travel')
low_limit_travel     EpicsSignal         ('m1_low_limit_travel')
direction_of_travel  EpicsSignal         ('m1_direction_of_travel')
motor_stop           EpicsSignal         ('m1_motor_stop')
home_forward         EpicsSignal         ('m1_home_forward')
home_reverse         EpicsSignal         ('m1_home_reverse')
soft_limit_lo        EpicsSignal         ('m1_soft_limit_lo')
soft_limit_hi        EpicsSignal         ('m1_soft_limit_hi')
steps_per_rev        EpicsSignal         ('m1_steps_per_rev')


```

</details>

## Move

command | description
--- | ---
`%mov MOTOR value` | interactive command move MOTOR to value (command line only)
`%movr MOTOR value` | interactive command relative move (command line only)
`MOTOR.move(value)` | ophyd command to `%mov`
`MOTOR.user_setpoint.put(value)` | ophyd to set motor `.VAL` field but not wait
`bps.mv(MOTOR, value)` | bluesky plan command to move and wait for completion
`bps.mv(MOTOR.user_setpoint, value)` | bluesky plan command, same
`bps.mvr(MOTOR, value)` | bluesky plan command, relative move

<details>
<summary>Examples:</summary>

```python
In [15]: %mov m1 1
                                                                                                                                            
In [16]: %movr m1 -1
                                                                                                                                            
In [17]: m1.move(.5)
Out[17]: MoveStatus(done=True, pos=m1, elapsed=0.8, success=True, settle_time=0.0)

In [18]: m1.user_setpoint.put(1)

In [19]: RE(bps.mv(m1, 0))
Out[19]: ()                                                                                                                                 
```

</details>


## Count

command | description
--- | ---
`%ct` | count _all_ objects with label `detectors` and format output (command line only)
`SCALER.trigger().wait(); SCALER.read()` | ophyd command to count SCALER
`bp.count([SCALER])` | bluesky plan to count

Count time setting is different for various types of detectors:

detector | set count time
--- | ---
scaler | `SCALER.preset_time.put(COUNT_TIME_S)`
area detector | `AD.cam.acquire_time.put(COUNT_TIME_S)`

<details>
<summary>Examples:</summary>

```python
In [20]: scaler.preset_time.get()
Out[20]: 1.0

In [21]: %mov scaler.preset_time 2.5

In [22]: scaler.preset_time.get()
Out[22]: 2.5

In [23]: %ct
[This data will not be saved. Use the RunEngine to collect data.]
noisy                          68.56615083963807
I0Mon                          12.0
ROI1                           0.0
ROI2                           0.0
scaler_time                    2.6

In [24]: scaler.trigger().wait()

In [25]: scaler.read()
Out[25]: 
OrderedDict([('I0Mon', {'value': 12.0, 'timestamp': 1613880362.609086}),
             ('ROI1', {'value': 0.0, 'timestamp': 1613880362.609086}),
             ('ROI2', {'value': 0.0, 'timestamp': 1613880362.609086}),
             ('scaler_time', {'value': 2.6, 'timestamp': 1613880338.961804})])

In [26]: scaler.trigger().wait(); scaler.read()
Out[26]: 
OrderedDict([('I0Mon', {'value': 11.0, 'timestamp': 1613880389.315847}),
             ('ROI1', {'value': 0.0, 'timestamp': 1613880389.315847}),
             ('ROI2', {'value': 0.0, 'timestamp': 1613880389.315847}),
             ('scaler_time', {'value': 2.6, 'timestamp': 1613880362.609086})])

```

</details>

## List, Describe, Summary

command | description
--- | ---
`wa` | show all labeled objects
`listobjects()` | table of all global objects
`listruns()` | table of runs (default: last 20)
`OBJECT.describe()` | OBJECT metadata: PV, type, units, limits, precision, ... (written as part of a run)
`OBJECT.summary()` | OBJECT details in human readable terms

<details>
<summary>Examples:</summary>

```python
In [43]: %wa
motor
  Positioner                     Value       Low Limit   High Limit  Offset     
  m1                             0.0         -32000.0    32000.0     0.0        
  m2                             0.0         -32000.0    32000.0     0.0        
  m3                             0.0         -32000.0    32000.0     0.0        
  m4                             0.0         -32000.0    32000.0     0.0        
  m5                             0.0         -32000.0    32000.0     0.0        
  m6                             0.0         -32000.0    32000.0     0.0        
  m7                             0.0         -32000.0    32000.0     0.0        
  m8                             0.0         -32000.0    32000.0     0.0        

  Local variable name                    Ophyd name (to be recorded as metadata)
  m1                                     m1                                    
  m2                                     m2                                    
  m3                                     m3                                    
  m4                                     m4                                    
  m5                                     m5                                    
  m6                                     m6                                    
  m7                                     m7                                    
  m8                                     m8                                    

detectors
  Local variable name                    Ophyd name (to be recorded as metadata)
  noisy                                  noisy                                 
  scaler                                 scaler                                

counter
  Local variable name                    Ophyd name (to be recorded as metadata)
  I0                                                                           
  I0Mon                                  I0Mon                                 
  ROI1                                   ROI1                                  
  ROI2                                   ROI2                                  
  clock                                                                        
  diode                                                                        
  scaler.channels.chan08.s               I0Mon                                 
  scaler.channels.chan10.s               ROI1                                  
  scaler.channels.chan11.s               ROI2                                  
  scint                                                                        


In [44]: listobjects()
====== =============== =============== =========
name   ophyd structure EPICS PV        label(s) 
====== =============== =============== =========
I0     EpicsSignalRO   sky:scaler1.S2  counter  
I0Mon  EpicsSignalRO   sky:scaler1.S8  counter  
ROI1   EpicsSignalRO   sky:scaler1.S10 counter  
ROI2   EpicsSignalRO   sky:scaler1.S11 counter  
_2     EpicsSignal     sky:scaler1.CNT          
clock  EpicsSignalRO   sky:scaler1.S1  counter  
diode  EpicsSignalRO   sky:scaler1.S5  counter  
m1     MyMotor         sky:m1          motor    
m2     MyMotor         sky:m2          motor    
m3     MyMotor         sky:m3          motor    
m4     MyMotor         sky:m4          motor    
m5     MyMotor         sky:m5          motor    
m6     MyMotor         sky:m6          motor    
m7     MyMotor         sky:m7          motor    
m8     MyMotor         sky:m8          motor    
mover2 EpicsSignal     IOC:float2               
noisy  EpicsSignalRO   sky:userCalc1   detectors
scaler ScalerCH        sky:scaler1     detectors
scint  EpicsSignalRO   sky:scaler1.S3  counter  
====== =============== =============== =========

Out[44]: <pyRestTable.rest_table.Table at 0x7fe064171fd0>

In [45]: listruns()
catalog name: bs2021
========= ========================== ======= ======= ========================================
short_uid date/time                  exit    scan_id command                                 
========= ========================== ======= ======= ========================================
e070882   2021-02-06 22:50:08.118423 success 131     rel_scan(detectors=['noisy'], num=19 ...
15621a3   2021-02-06 22:49:58.051389 success 130     rel_scan(detectors=['noisy'], num=19 ...
7322f2f   2021-02-06 22:47:39.789684 success 129     rel_scan(detectors=['noisy'], num=19 ...
02732c2   2021-02-06 22:47:28.456452 success 128     rel_scan(detectors=['noisy'], num=19 ...
1a7f0ce   2020-12-29 22:54:57.604267 success 127     scan(detectors=['fourc'], num=41, ar ...
7dd58eb   2020-12-29 22:46:09.629373 success 126     scan(detectors=['fourc'], num=41, ar ...
d1f5f4f   2020-12-29 22:36:20.358277 success 125     scan(detectors=['fourc'], num=41, ar ...
0f6eac8   2020-12-29 22:34:22.757687 success 124     scan(detectors=['fourc'], num=41, ar ...
23a642d   2020-12-16 22:08:17.257659 success 123     scan(detectors=['fourc_h', 'fourc_k' ...
e89dbed   2020-12-16 22:08:03.778558 success 122     scan(detectors=['fourc_h', 'fourc_k' ...
699c827   2020-12-16 22:07:08.838917 success 121     scan(detectors=['fourc_h', 'fourc_k' ...
978ec2b   2020-12-16 21:00:33.380914 success 120     rel_scan(detectors=['noisy'], num=19 ...
bb22936   2020-12-16 20:59:58.870435 success 119     scan(detectors=['noisy'], num=19, ar ...
3c04995   2020-12-16 20:58:43.471627 success 118     count(detectors=['scaler'], num=1)      
========= ========================== ======= ======= ========================================

Out[45]: <pyRestTable.rest_table.Table at 0x7fe064174190>

In [48]: scaler.describe()
Out[48]: 
OrderedDict([('I0Mon',
              {'source': 'PV:sky:scaler1.S8',
               'dtype': 'number',
               'shape': [],
               'units': '',
               'lower_ctrl_limit': 0.0,
               'upper_ctrl_limit': 0.0,
               'precision': 0}),
             ('ROI1',
              {'source': 'PV:sky:scaler1.S10',
               'dtype': 'number',
               'shape': [],
               'units': '',
               'lower_ctrl_limit': 0.0,
               'upper_ctrl_limit': 0.0,
               'precision': 0}),
             ('ROI2',
              {'source': 'PV:sky:scaler1.S11',
               'dtype': 'number',
               'shape': [],
               'units': '',
               'lower_ctrl_limit': 0.0,
               'upper_ctrl_limit': 0.0,
               'precision': 0}),
             ('scaler_time',
              {'source': 'PV:sky:scaler1.T',
               'dtype': 'number',
               'shape': [],
               'units': '',
               'lower_ctrl_limit': 0.0,
               'upper_ctrl_limit': 0.0,
               'precision': 3})])

In [49]: scaler.summary()
data keys (* hints)
-------------------
*I0Mon
*ROI1
*ROI2
 scaler_time

read attrs
----------
channels             Channels            ('scaler_channels')
channels.chan08      ScalerChannel       ('scaler_channels_chan08')
channels.chan08.s    EpicsSignalRO       ('I0Mon')
channels.chan10      ScalerChannel       ('scaler_channels_chan10')
channels.chan10.s    EpicsSignalRO       ('ROI1')
channels.chan11      ScalerChannel       ('scaler_channels_chan11')
channels.chan11.s    EpicsSignalRO       ('ROI2')
time                 EpicsSignal         ('scaler_time')

config keys
-----------
scaler_auto_count_delay
scaler_auto_count_time
scaler_channels_chan08_chname
scaler_channels_chan08_gate
scaler_channels_chan08_preset
scaler_channels_chan10_chname
scaler_channels_chan10_gate
scaler_channels_chan10_preset
scaler_channels_chan11_chname
scaler_channels_chan11_gate
scaler_channels_chan11_preset
scaler_count_mode
scaler_delay
scaler_egu
scaler_freq
scaler_preset_time

configuration attrs
-------------------
channels             Channels            ('scaler_channels')
channels.chan08      ScalerChannel       ('scaler_channels_chan08')
channels.chan08.chname EpicsSignal         ('scaler_channels_chan08_chname')
channels.chan08.preset EpicsSignal         ('scaler_channels_chan08_preset')
channels.chan08.gate EpicsSignal         ('scaler_channels_chan08_gate')
channels.chan10      ScalerChannel       ('scaler_channels_chan10')
channels.chan10.chname EpicsSignal         ('scaler_channels_chan10_chname')
channels.chan10.preset EpicsSignal         ('scaler_channels_chan10_preset')
channels.chan10.gate EpicsSignal         ('scaler_channels_chan10_gate')
channels.chan11      ScalerChannel       ('scaler_channels_chan11')
channels.chan11.chname EpicsSignal         ('scaler_channels_chan11_chname')
channels.chan11.preset EpicsSignal         ('scaler_channels_chan11_preset')
channels.chan11.gate EpicsSignal         ('scaler_channels_chan11_gate')
count_mode           EpicsSignal         ('scaler_count_mode')
delay                EpicsSignal         ('scaler_delay')
auto_count_delay     EpicsSignal         ('scaler_auto_count_delay')
freq                 EpicsSignal         ('scaler_freq')
preset_time          EpicsSignal         ('scaler_preset_time')
auto_count_time      EpicsSignal         ('scaler_auto_count_time')
egu                  EpicsSignal         ('scaler_egu')

unused attrs
------------
count                EpicsSignal         ('scaler_count')
update_rate          EpicsSignal         ('scaler_update_rate')
auto_count_update_rate EpicsSignal         ('scaler_auto_count_update_rate')

```

</details>

## Bluesky Plans _vs_. Command-line Actions

There is a difference in the commands to use depending on the context.

context | blocking? | command style
--- | --- | ---
plan function | NOT allowed | call Bluesky [plans](https://blueskyproject.io/bluesky/plans.html) written as [generator](https://wiki.python.org/moin/Generators) functions using `yield from a_plan()`
command line | allowed | use magics (such as `%mov`), `.put()`, and/or `RE(a_plan())`

<details>
<summary>Examples:</summary>

<b>plan function</b>

```python
def _insertFilters_(a, b):
    """plan: insert the EPICS-specified filters"""
    yield from bps.mv(pf4_AlTi.fPosA, int(a), pf4_AlTi.fPosB, int(b))
    yield from bps.sleep(0.5)       # allow all blades to re-position

# then call from another plan such as

    yield from _insertFilters_(0, 0)
```

<b>command line actions</b>

```python
%mov pf4_AlTi.fPosA int(a) pf4_AlTi.fPosB int(b)
# or
pf4_AlTi.fPosA.put(int(a))
pf4_AlTi.fPosB.put(int(b))
# or
RE(bps.mv(pf4_AlTi.fPosA, int(a), pf4_AlTi.fPosB, int(b)))
```

NOTE: On the command line, we can ignore the 0.5 s sleep needed by automated
procedures.

</details>

If you are translating PyEpics code to Bluesky plans, consult this
[guide](https://blueskyproject.io/bluesky/from-pyepics-to-bluesky.html?highlight=blocking).

## Log files

In the working directory, the log files are written to a `./.logs` subdirectory.
There are two kinds of file, one that records user commands and the python
result, the other records items sent to the
[customized](https://github.com/prjemian/stdlogpj#example-directing-logs-to-a-specific-directory)
Python [logging](https://docs.python.org/3/library/logging.html) package.

In the IPython session, use the `!` to run a linux command:

<details>
<summary>Examples:</summary>

```python
In [50]: !ls -lAFgh .logs
total 36K
-rw-rw-r-- 1 prjemian prjemian 1.6K Feb 20 12:31 ipython_console.log
-rw-rw-r-- 1 prjemian prjemian  411 Feb 20 12:23 ipython_console.log.001~
-rw-rw-r-- 1 prjemian prjemian  832 Feb 20 12:19 ipython_console.log.002~
-rw-rw-r-- 1 prjemian prjemian  154 Feb 20 12:17 ipython_console.log.003~
-rw-rw-r-- 1 prjemian prjemian  250 Feb 20 12:17 ipython_console.log.004~
-rw-rw-r-- 1 prjemian prjemian  13K Feb 20 12:23 ipython_logger.log

In [51]: !head .logs/ipython_console.log
# IPython log file

# Sat, 20 Feb 2021 12:23:20
listobjects()
#[Out]# <pyRestTable.rest_table.Table at 0x7f65265a9ee0>
# Sat, 20 Feb 2021 12:23:26
listruns()
#[Out]# <pyRestTable.rest_table.Table at 0x7f64b9e912b0>
# Sat, 20 Feb 2021 12:23:28
db

In [52]: !head .logs/ipython_logger.log
|2021-02-20 12:14:55.966|INFO|92929|bluesky-session|session_logs|35|MainThread| - ############################################################ startup
|2021-02-20 12:14:55.966|INFO|92929|bluesky-session|session_logs|36|MainThread| - logging started
|2021-02-20 12:14:55.966|INFO|92929|bluesky-session|session_logs|37|MainThread| - logging level = 10
|2021-02-20 12:14:55.966|INFO|92929|bluesky-session|collection|7|MainThread| - /home/prjemian/.ipython/profile_bluesky/startup/instrument/collection.py
|2021-02-20 12:14:55.966|INFO|92929|bluesky-session|console|11|MainThread| - /home/prjemian/.ipython/profile_bluesky/startup/instrument/mpl/console.py
|2021-02-20 12:14:56.182|INFO|92929|bluesky-session|collection|11|MainThread| - bluesky framework
|2021-02-20 12:14:56.183|INFO|92929|bluesky-session|check_python|9|MainThread| - /home/prjemian/.ipython/profile_bluesky/startup/instrument/framework/check_python.py
|2021-02-20 12:14:56.183|INFO|92929|bluesky-session|check_bluesky|9|MainThread| - /home/prjemian/.ipython/profile_bluesky/startup/instrument/framework/check_bluesky.py
|2021-02-20 12:14:56.688|INFO|92929|bluesky-session|initialize|15|MainThread| - /home/prjemian/.ipython/profile_bluesky/startup/instrument/framework/initialize.py
|2021-02-20 12:14:57.281|INFO|92929|bluesky-session|initialize|67|MainThread| - New directory to store RE.md between sessions: /home/prjemian/.config/Bluesky_RunEngine_md

```

</details>
