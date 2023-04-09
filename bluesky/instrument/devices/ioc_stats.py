"""
IOC statistics: synApps iocStats
"""

# fmt: off
__all__ = [
    "gp_stats",
    # "ad_stats",
]
# fmt: on

import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

from .. import iconfig
from ophyd import Component, Device, EpicsSignalRO


IOC = iconfig.get("GP_IOC_PREFIX", "gp:")


class IocInfoDevice(Device):

    iso8601 = Component(EpicsSignalRO, "iso8601")
    uptime = Component(EpicsSignalRO, "UPTIME")


gp_stats = IocInfoDevice(IOC, name="gp_stats")

# Too bad, this ADSimDetector does not have iocStats
# IOC = iconfig.get("ADSIM_IOC_PREFIX", "ad:")
# ad_stats = IocInfoDevice(IOC, name="ad_stats")
