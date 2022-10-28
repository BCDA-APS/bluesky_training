"""
calculations
"""

__all__ = ["calcs", "calcouts"]

import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

from .. import iconfig
import apstools.synApps


IOC = iconfig.get("GP_IOC_PREFIX", "gp:")

calcs = apstools.synApps.UserCalcsDevice(IOC, name="calcs")
calcouts = apstools.synApps.UserCalcoutDevice(IOC, name="calcouts")

if iconfig.get("ENABLE_CALCS", False):
    # Normally, do not do _any_ actions (like these) in the instrument
    # package since that might affect other simultaneous use.  In this
    # case, the actions are probably OK.  Most users forget they even exist.
    # These steps enable all the userCalcN and userCalcoutN records to process.
    calcs.enable.put(1)
    calcouts.enable.put(1)
