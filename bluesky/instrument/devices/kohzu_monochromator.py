"""
Simulated Kohzu Double-Crystal Monochromator (DCM)
"""

__all__ = [
    "dcm",
]

from ..session_logs import logger

logger.info(__file__)

from apstools.devices import KohzuSeqCtl_Monochromator
from bluesky import plan_stubs as bps
from ophyd import Component
from ophyd import EpicsMotor

import os


IOC = os.environ.get("GP_IOC_PREFIX", "gp:")


class MyKohzu(KohzuSeqCtl_Monochromator):
    m_theta = Component(EpicsMotor, "m45", kind="normal")
    m_y = Component(EpicsMotor, "m46", kind="normal")
    m_z = Component(EpicsMotor, "m47", kind="normal")

    def into_control_range(self, p_theta=2, p_y=-15, p_z=90):
        """
        Move the Kohzu motors into range so the energy controls will work.

        Written as a bluesky plan so that all motors can be moved
        simultaneously.  Return early if the motors are already in range.

        USAGE::

            RE(dcm.into_control_range())
        """
        if (
            self.m_theta.position >= p_theta
            and self.m_y.position <= p_y
            and self.m_z.position >= p_z
        ):
            # all motors in range, no work to do, MUST yield something
            yield from bps.null()
            return
        # fmt: off
        yield from bps.mv(
            self.m_theta, p_theta,
            self.m_y, p_y,
            self.m_z, p_z,
        )
        # fmt: on
        yield from bps.sleep(1)  # allow IOC to react
        yield from bps.mv(self.operator_acknowledge, 1)

    def stop(self):
        self.m_theta.stop()
        self.m_y.stop()
        self.m_z.stop()


dcm = MyKohzu(IOC, name="dcm")
