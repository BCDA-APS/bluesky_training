"""
APS only: connect with facility information
"""

__all__ = [
    "aps",
]

from ..session_logs import logger

logger.info(__file__)

import apstools.devices

# from ..framework import sd

aps = apstools.devices.ApsMachineParametersDevice(name="aps")
# sd.baseline.append(aps)
