"""
shutter
"""

__all__ = [
    "shutter",
]

from ..session_logs import logger

logger.info(__file__)

import apstools.devices

shutter = apstools.devices.SimulatedApsPssShutterWithStatus(
    name="shutter", labels=("shutters",)
)

# shutter needs short recovery time after moving
shutter.delay_s = 0.05
