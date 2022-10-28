"""
simulated noisy detector
"""

__all__ = [
    "noisy",
    "change_noisy_parameters",
]

import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

from .. import iconfig
from .calculation_records import calcs
from .motors import m1
from ophyd import EpicsSignalRO
import apstools.devices
import numpy


IOC = iconfig.get("GP_IOC_PREFIX", "gp:")


def change_noisy_parameters(fwhm=0.15, peak=10000, noise=0.08):
    """
    Setup the swait record with new random numbers.

    BLOCKING calls, not a bluesky plan
    """
    calcs.calc1.reset()
    apstools.devices.setup_lorentzian_swait(
        calcs.calc1,
        m1.user_readback,
        center=2 * numpy.random.random() - 1,
        width=fwhm * numpy.random.random(),
        scale=peak * (9 + numpy.random.random()),
        noise=noise * (0.01 + numpy.random.random()),
    )


# demo: use swait records to make "noisy" detector signals
noisy = EpicsSignalRO(
    f"{IOC}userCalc1", name="noisy", labels=("detectors", "simulator")
)
change_noisy_parameters()
