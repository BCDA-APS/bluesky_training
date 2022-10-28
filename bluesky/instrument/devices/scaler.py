"""
example scaler
"""

__all__ = """
    scaler1
    timebase I0 I00 I000 scint diode
""".split()

import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

from .. import iconfig
from ophyd.scaler import ScalerCH
import time


IOC = iconfig.get("GP_IOC_PREFIX", "gp:")

# make an instance of the entire scaler, for general control
scaler1 = ScalerCH(f"{IOC}scaler1", name="scaler1", labels=["scalers", "detectors"])
scaler1.wait_for_connection()

if not len(scaler1.channels.chan01.chname.get()):
    # CAUTION: define channel names JUST for this simulation.
    # For a real instrument, the names are assigned when the
    # detector pulse cables are connected to the scaler channels.
    logger.info(
        f"{scaler1.name} has no channel names.  Assigning channel names."
    )
    scaler1.channels.chan01.chname.put("timebase")
    scaler1.channels.chan02.chname.put("I0")
    scaler1.channels.chan03.chname.put("scint")
    scaler1.channels.chan04.chname.put("diode")
    scaler1.channels.chan05.chname.put("I000")
    scaler1.channels.chan06.chname.put("I00")
    time.sleep(1)  # wait for IOC

# choose just the channels with EPICS names
scaler1.select_channels()

# examples: make shortcuts to specific channels assigned in EPICS

timebase = scaler1.channels.chan01.s
I0 = scaler1.channels.chan02.s
scint = scaler1.channels.chan03.s
diode = scaler1.channels.chan04.s
I000 = scaler1.channels.chan05.s
I00 = scaler1.channels.chan06.s

for item in (timebase, I0, I00, I000, scint, diode):
    item._ophyd_labels_ = set(["channel", "counter"])
