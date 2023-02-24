"""
Simulated Kohzu Double-Crystal Monochromator (DCM)
"""

__all__ = [
    "dcm",
]

import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

from .. import iconfig
from apstools.devices import KohzuSeqCtl_Monochromator
from bluesky import plan_stubs as bps
from ophyd import Component
from ophyd import EpicsMotor


IOC = iconfig.get("GP_IOC_PREFIX", "gp:")


class MyKohzu(KohzuSeqCtl_Monochromator):
    m_theta = Component(EpicsMotor, "m45", kind="normal", labels=["motor"])
    m_y = Component(EpicsMotor, "m46", kind="normal", labels=["motor"])
    m_z = Component(EpicsMotor, "m47", kind="normal", labels=["motor"])

    def into_control_range(self, p_theta=2, p_y=-15, p_z=90):
        """
        Move the Kohzu motors into range so the energy controls will work.

        Written as a bluesky plan so that all motors can be moved
        simultaneously.  Return early if the motors are already in range.

        USAGE::

            RE(dcm.into_control_range())
        """
        args = []
        if self.m_theta.position < p_theta:
            args += [self.m_theta, p_theta]
        if self.m_y.position > p_y:
            args += [self.m_y, p_y]
        if self.m_z.position < p_z:
            args += [self.m_z, p_z]
        if (len(args) == 0):
            # all motors in range, no work to do, MUST yield something
            yield from bps.null()
            return
        yield from bps.sleep(1)  # allow IOC to react
        yield from bps.mv(
            self.operator_acknowledge, 1,
            self.mode, "Auto"
        )

    def stop(self):
        self.m_theta.stop()
        self.m_y.stop()
        self.m_z.stop()


dcm = MyKohzu(IOC, name="dcm")
