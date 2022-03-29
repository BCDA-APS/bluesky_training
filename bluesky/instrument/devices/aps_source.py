"""
APS only: connect with facility information
"""

__all__ = [
    "aps",
]

from ..session_logs import logger

logger.info(__file__)

import apstools.devices


aps = apstools.devices.ApsMachineParametersDevice(name="aps")
