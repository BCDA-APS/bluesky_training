"""
APS only: connect with facility information
"""

__all__ = [
    "undulator",
]

from ..session_logs import logger

logger.info(__file__)

import apstools.devices

# from ..framework import sd

undulator = apstools.devices.ApsUndulator("ID45", name="undulator")
# undulator = apstools.devices.ApsUndulatorDual("ID45", name="undulator")
# sd.baseline.append(undulator)
