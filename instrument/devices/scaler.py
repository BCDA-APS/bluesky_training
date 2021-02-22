"""
example scaler
"""

__all__ = """
    scaler1
    timebase I0 scint diode
""".split()

from ..session_logs import logger

logger.info(__file__)

from ophyd.scaler import ScalerCH
from ophyd import Kind

# make an instance of the entire scaler, for general control
scaler1 = ScalerCH("ioc:scaler1", name="scaler1", labels=["scalers", "detectors"])
scaler1.wait_for_connection()

if not len(scaler1.channels.chan01.chname.get()):
    logger.info(f"{scaler1.name} has no channel names.  Assigning channel names.")
    scaler1.channels.chan01.chname.put("timebase")
    scaler1.channels.chan02.chname.put("I0")
    scaler1.channels.chan03.chname.put("scint")
    scaler1.channels.chan04.chname.put("diode")

# choose just the channels with EPICS names
scaler1.select_channels()

# examples: make shortcuts to specific channels assigned in EPICS

timebase = scaler1.channels.chan01.s
I0 = scaler1.channels.chan02.s
scint = scaler1.channels.chan03.s
diode = scaler1.channels.chan04.s

for item in (timebase, I0, scint, diode):
    item._ophyd_labels_ = set(["channel", "counter",])
