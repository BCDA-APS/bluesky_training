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

calcs.enable.put(1)

sd.baseline.append(calcs)
sd.baseline.append(calcouts)
