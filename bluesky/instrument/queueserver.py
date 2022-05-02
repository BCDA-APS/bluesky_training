"""
Configure for data collection using bluesky-queueserver.
"""

import logging
logger = logging.getLogger(__name__)

logger.info(__file__)
print(__file__)

from . import iconfig
from .epics_signal_config import scan_id_epics
from .queueserver_framework import *

from .devices import *
from .plans import *
from .utils import *
from .callbacks import *

from bluesky.plans import *
from bluesky.plan_stubs import sleep
from ophyd import Device
from ophyd import Signal
import pyRestTable


def print_devices_and_signals():
    glo = globals().copy()

    table = pyRestTable.Table()
    table.labels = "device/object pvprefix/pvname connected?".split()
    for k, v in sorted(glo.items()):
        if isinstance(v, (Device, Signal)) and not k.startswith("_"):
            v.wait_for_connection()
            p = ""
            for aname in "pvname prefix".split():
                if hasattr(v, aname):
                    p = getattr(v, aname)
            table.addRow((v.name, p, v.connected))
    if len(table.rows) > 0:
        print("Table of Devices and signals:")
        print(table)


def print_plans():
    glo = globals().copy()
    plans = [
        k
        for k, v in sorted(glo.items()) 
        if inspect.isgeneratorfunction(v)
    ]
    if len(plans) > 0:
        print("List of Plans:")
        for k in plans:
            print(f"* {k}{inspect.signature(glo[k])}")
        print("")


def startup_report():
    """Show instrument data on startup"""
    from . import iconfig
    from ophyd import Device, Signal
    import inspect
    import pyRestTable

    table = pyRestTable.Table()
    table.labels = "key value".split()
    for k, v in sorted(iconfig.items()):
        table.addRow((k, v))
    if len(table.rows) > 0:
        print("")
        print("Instrument configuration (iconfig):")
        print(table)

    glo = globals().copy()

    table = pyRestTable.Table()
    table.labels = "device/object pvprefix/pvname connected?".split()
    for k, v in sorted(glo.items()):
        if isinstance(v, (Device, Signal)) and not k.startswith("_"):
            v.wait_for_connection()
            p = ""
            for aname in "pvname prefix".split():
                if hasattr(v, aname):
                    p = getattr(v, aname)
            table.addRow((v.name, p, v.connected))
    if len(table.rows) > 0:
        print("Table of Devices and signals:")
        print(table)

    plans = [
        k
        for k, v in sorted(glo.items()) 
        if inspect.isgeneratorfunction(v)
    ]
    if len(plans) > 0:
        print("List of Plans:")
        for k in plans:
            print(f"* {k}{inspect.signature(glo[k])}")
        print("")


# startup_report()

if iconfig.get("APS_IN_BASELINE", False):
    sd.baseline.append(aps)
