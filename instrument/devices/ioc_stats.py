"""
IOC statistics: synApps iocStats
"""

# fmt: off
__all__ = [
    "gp_stats",
    # "ad_stats", 
]
# fmt: on

from ..session_logs import logger

logger.info(__file__)

from ophyd import Component, Device, EpicsSignalRO
import os

GP_IOC_PREFIX = os.environ.get("GP_IOC_PREFIX", "gp:")


class IocInfoDevice(Device):

    iso8601 = Component(EpicsSignalRO, "iso8601")
    uptime = Component(EpicsSignalRO, "UPTIME")


gp_stats = IocInfoDevice(GP_IOC_PREFIX, name="gp_stats")

# Too bad, this ADSimDetector does not have iocStats
# ad_stats = IocInfoDevice("ad:", name="ad_stats")
