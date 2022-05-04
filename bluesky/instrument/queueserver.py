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

# guides choice of module to import cat
iconfig["framework"] = "queueserver"

from .devices import *
from .plans import *
from .utils import *
from .callbacks import *

from bluesky.plans import *
from bluesky.plan_stubs import sleep
from ophyd import Device
from ophyd import Signal
import pyRestTable


if iconfig.get("WRITE_SPEC_DATA_FILES", False):
    if specwriter is not None:
        RE.subscribe(specwriter.receiver)
        logger.info(f"writing to SPEC file: {specwriter.spec_filename}")
        logger.info("   >>>>   Using default SPEC file name   <<<<")
        logger.info("   file will be created when bluesky ends its next scan")
        logger.info("   to change SPEC file, use command:   newSpecFile('title')")


def print_devices_and_signals():
    """
    Print the Devices and Signals in the current global namespace.
    """
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
    """
    Print the plans in the current global namespace.
    """
    glo = globals().copy()
    # fmt: off
    plans = [
        k
        for k, v in sorted(glo.items())
        if inspect.isgeneratorfunction(v)
    ]
    # fmt: on
    if len(plans) > 0:
        print("List of Plans:")
        for k in plans:
            print(f"* {k}{inspect.signature(glo[k])}")
        print("")


if iconfig.get("APS_IN_BASELINE", False):
    sd.baseline.append(aps)
