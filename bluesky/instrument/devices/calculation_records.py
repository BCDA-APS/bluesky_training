"""
calculations
"""

__all__ = ["calcs", "calcouts"]

from ..session_logs import logger

logger.info(__file__)

from .. import iconfig
from ..framework import sd
import apstools.synApps


IOC = iconfig.get("GP_IOC_PREFIX", "gp:")

calcs = apstools.synApps.UserCalcsDevice(IOC, name="calcs")
calcouts = apstools.synApps.UserCalcoutDevice(IOC, name="calcouts")

# Normally, do not do _any_ actions (like these) in the instrument
# package since that might affect other simultaneous use.  In this
# case, the actions are probably OK.  Most users forget they even exist.
# These steps enable all the userCalcN and userCalcoutN records to process.
calcs.enable.put(1)
calcouts.enable.put(1)

# record all calculation signals before & after each run
sd.baseline.append(calcs)
sd.baseline.append(calcouts)
