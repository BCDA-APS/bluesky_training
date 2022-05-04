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

from .. import iconfig
from ophyd import Component, Device, EpicsSignalRO


IOC = iconfig.get("GP_IOC_PREFIX", "gp:")


class IocInfoDevice(Device):

    iso8601 = Component(EpicsSignalRO, "iso8601")
    uptime = Component(EpicsSignalRO, "UPTIME")


gp_stats = IocInfoDevice(IOC, name="gp_stats")

# Too bad, this ADSimDetector does not have iocStats
# ad_stats = IocInfoDevice("ad:", name="ad_stats")
