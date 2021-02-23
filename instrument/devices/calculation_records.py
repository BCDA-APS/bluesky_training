"""
calculations
"""

__all__ = ["calcs", "calcouts"]

from ..session_logs import logger

logger.info(__file__)

from ..framework import sd
from ophyd import EpicsSignalRO
import apstools.synApps

calcs = apstools.synApps.UserCalcsDevice("gp:", name="calcs")
calcouts = apstools.synApps.UserCalcoutDevice("gp:", name="calcouts")

calcs.enable.put(1)

sd.baseline.append(calcs)
sd.baseline.append(calcouts)
