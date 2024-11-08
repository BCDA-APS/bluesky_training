# Setup APS Data Management

This document describes how to setup and use the [APS Data
Management](https://git.aps.anl.gov/DM/dm-docs/-/wikis/home) (DM) Python
[API](https://git.aps.anl.gov/DM/dm-docs/-/wikis/DM/Beamline-Services/API-Reference)
(tools) in a Bluesky session.

This document provides guidance for workstations at the APS, where DM tools and
services are available.

## Background

As stated in the DM [_Getting
Started_](https://git.aps.anl.gov/DM/dm-docs/-/wikis/DM/HowTos/Getting-Started)
guide:

> The APS Data Management System is a system for gathering together experimental
> data, metadata about the experiment and providing users access to the data
> based on a users role.

## DM is configured by Environment Variables

The [_Getting
Started_](https://git.aps.anl.gov/DM/dm-docs/-/wikis/DM/HowTos/Getting-Started#setting-up-the-environment)
guide explains how to setup a pre-configured conda environment to use the DM
tools from the command line directly.  The setup procedure uses this shell command:

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
[`apstools`](https://bcda-aps.github.io/apstools/latest/api/_utils.html#aps-data-management),
provides support for using DM in a Bluesky session.

<details>

Function
[`dm_source_environ()`](https://bcda-aps.github.io/apstools/latest/api/_utils.html#apstools.utils.aps_data_management.dm_source_environ)
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
