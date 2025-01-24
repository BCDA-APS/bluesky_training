# Setup APS Data Management

This document describes how to setup and submit a workflow job using the [APS
Data Management](https://git.aps.anl.gov/DM/dm-docs/-/wikis/home) (DM) Python
[API](https://git.aps.anl.gov/DM/dm-docs/-/wikis/DM/Beamline-Services/API-Reference)
(tools) in a Bluesky session.

This document provides guidance for workstations at the APS, where DM tools and
services are available.

For more information, see the DM API reference for more information about how to
use the DM API and tools. See the `apstools`
[documentation](https://bcda-aps.github.io/apstools/latest/api/_utils.html#apstools.utils.aps_data_management),
for a list of the support code available.

## About APS Data Management (DM)

As stated in the DM _Getting Started_
[guide](https://git.aps.anl.gov/DM/dm-docs/-/wikis/DM/HowTos/Getting-Started):

> The APS Data Management System is a system for gathering together experimental
> data, metadata about the experiment and providing users access to the data
> based on a users role.

## DM is configured by Environment Variables

The DM _Getting Started_
[guide](https://git.aps.anl.gov/DM/dm-docs/-/wikis/DM/HowTos/Getting-Started)
explains how to activate a pre-configured conda environment to use the DM tools
directly from the command line.  The setup procedure uses this shell command:

```bash
/home/DM_INSTALL_DIR/etc/dm.setup.sh
```

where `DM_INSTALL_DIR` is the deployment directory for this beamline.

<details>
<summary>NOTE</summary>

The exact path to this file will vary between beamline accounts.  Contact the DM
support team for details about your beamline.

</details>

The DM conda environment does not have the packages installed to run a Bluesky
session.

### Configure DM in Bluesky sessions

The Bluesky conda environment has all the packages for both Bluesky and DM
already installed (for APS installations).  One of those packages,
[apstools](https://bcda-aps.github.io/apstools/latest/api/_utils.html#aps-data-management),
provides support for using DM in a Bluesky session.

<details>

The `dm_source_environ()`
[function](https://bcda-aps.github.io/apstools/latest/api/_utils.html#apstools.utils.aps_data_management.dm_source_environ)
is used internally to install the environment variables.  It expects a global
variable `DM_SETUP_FILE` to be defined in the module.  

**Do not call `dm_source_environ()` directly.**

Use `dm_setup("/home/DM_INSTALL_DIR/etc/dm.setup.sh")`.

</details>

Use these Python commands to install DM's environment variables:

```py
from apstools.utils import dm_setup

dm_setup("/home/DM_INSTALL_DIR/etc/dm.setup.sh")
```

**CAUTION**:  `dm_setup()` must be run **before** any other DM tools are used.
Do this each time a Bluesky session is started (where the DM API is to be used).

In typical Bluesky installations at APS, this file name is defined in the
`iconfig.yml` file, such as for [XPCS at station
8-ID-I](https://github.com/aps-8id-dys/bluesky/blob/6bbcfeceab7a6695d3be81ffd56954d362bf25ea/src/instrument/configs/iconfig.yml#L29):

```yaml
# APS Data Management
# Use bash shell, deactivate all conda environments, source this file:
DM_SETUP_FILE: "/home/dm/etc/dm.setup.sh"
```

### Example at APS XPCS station 8-ID-I

Show how many DM workflow jobs are processing now:

```py
In [1]: from apstools.utils import dm_setup
   ...: 
   ...: dm_setup("/home/dm/etc/dm.setup.sh")
   ...: 
Out[1]: '8idi'

In [2]: from dm.proc_web_service.api.procApiFactory import ProcApiFactory
   ...: api = ProcApiFactory.getWorkflowProcApi()
   ...: jobs = api.listProcessingJobs()
   ...: for j in jobs:
   ...:     if j["status"] not in ("done", "failed"):
   ...:         print(f"{j['id']=!r}  {j.get('submissionTimestamp')=!r}  {j['status']=!r}")
Out[2]:  # lots of jobs, only showing a few of them
j['id']='6754e679-cedb-482b-bb4d-b58137f84001'  j.get('submissionTimestamp')='2024/11/08 04:48:31 CST'  j['status']='pending'
j['id']='ad7328ae-35ba-4418-a9fd-b3dcc873348f'  j.get('submissionTimestamp')='2024/11/08 04:48:34 CST'  j['status']='pending'
...
j['id']='72b6d1b7-b6e0-4eb8-87d5-5f52792a043b'  j.get('submissionTimestamp')='2024/11/08 08:31:22 CST'  j['status']='running'
j['id']='19252b7d-8961-4994-8977-86929811a988'  j.get('submissionTimestamp')='2024/11/08 08:31:28 CST'  j['status']='running'

```

## Submit a DM workflow job from a Bluesky session

Here, we demonstrate one way to start a DM workflow from a Bluesky session.

To submit a workflow job from a Bluesky session, first call `dm_setup()` as described above.  Then,
get the "DM Processing API" as follows:

```py
from apstools.utils import dm_api_proc

api = dm_api_proc()
```

Choose the workflow by name:

```py
workflowOwner = api.username
workflowName = "xpcs8-02-gladier-boost"
```

Define the workflow arguments in a Python dictionary (these arguments are
specific to the XPCS workflow named above):

```py
argsDict = {
    "filePath": "H001_005_test_Feb_7-01000.h5",
    "qmap": "eiger4M_qmap_d36_s360.h5",
    "experimentName": "zhang202402",
    # any other keyword arguments required by the workflow come next ...
}
```

Start the processing job:

```py
job = api.startProcessingJob(workflowOwner, workflowName, argsDict)
```

Show the processing job ID:

```py
print(f"{job['id']=!r}")
'c322e87c-ec43-4077-b074-eeef8522889c'
```
