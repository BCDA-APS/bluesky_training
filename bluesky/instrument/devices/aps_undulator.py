"""
APS only: insertion device
"""

__all__ = [
    "undulator",
]

from ..session_logs import logger

logger.info(__file__)

import apstools.devices


undulator = apstools.devices.ApsUndulator("ID45", name="undulator")
# undulator = apstools.devices.ApsUndulatorDual("ID45", name="undulator")
