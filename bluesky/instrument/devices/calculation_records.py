"""
calculations
"""

__all__ = ["calcs", "calcouts"]

from ..session_logs import logger

logger.info(__file__)

from ..framework import sd
from ophyd import EpicsSignalRO
import apstools.synApps
import os

GP_IOC_PREFIX = os.environ.get("GP_IOC_PREFIX", "gp:")

calcs = apstools.synApps.UserCalcsDevice(GP_IOC_PREFIX, name="calcs")
calcouts = apstools.synApps.UserCalcoutDevice(GP_IOC_PREFIX, name="calcouts")

# Normally, do not do _any_ actions (like these) in the instrument
# package since that might affect other simultaneous use.  In this
# case, the actions are probably OK.  Most users forget they even exist.
# These steps enable all the userCalcN and userCalcoutN records to process.
calcs.enable.put(1)
calcouts.enable.put(1)

# record all calculation signals before & after each run
sd.baseline.append(calcs)
sd.baseline.append(calcouts)
