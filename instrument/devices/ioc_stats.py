"""
IOC statistics: synApps iocStats
"""

# fmt: off
__all__ = [
    "ioc_stats",
    # "ad_stats", 
]
# fmt: on

from ..session_logs import logger

logger.info(__file__)

from ophyd import Component, Device, EpicsSignalRO


class IocInfoDevice(Device):

    iso8601 = Component(EpicsSignalRO, "iso8601")
    uptime = Component(EpicsSignalRO, ":UPTIME")


ioc_stats = IocInfoDevice("ioc:", name="ioc_stats")

# Too bad, this ADSimDetector does not have iocStats
# ad_stats = IocInfoDevice("ad:", name="ad_stats")
