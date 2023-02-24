"""
6-circle diffractometer, connected to EpicsMotor records.

https://github.com/prjemian/epics-docker/tree/main/v1.1/n5_custom_synApps#motor-assignments


=====   ==================
motor	assignment
=====   ==================
m29	    4-circle diffractometer M_TTH
m30	    4-circle diffractometer M_TH
m31	    4-circle diffractometer M_CHI
m32	    4-circle diffractometer M_PHI
=====   ==================
"""

__all__ = """
    sixc
""".split()

import logging

logger = logging.getLogger(__name__)
logger.info(__file__)

import hkl
from ophyd import Component, EpicsMotor, EpicsSignalRO

from .. import iconfig

IOC = iconfig.get("GP_IOC_PREFIX", "gp:")
# No defined motor assignments, pick different than fourc (m29-32)
M_TTH = "m23"
M_OMEGA = "m24"
M_CHI = "m25"
M_PHI = "m26"
M_GAMMA = "m27"
M_MU = "m28"


class SixCircle(hkl.SimMixin, hkl.E6C):
    """
    Our 6-circle.  Eulerian.

    Energy obtained (RO) from monochromator.
    """

    # the reciprocal axes are defined by SimMixin

    mu = Component(EpicsMotor, f"{M_MU}", kind="hinted", labels=["motor"])
    omega = Component(EpicsMotor, f"{M_OMEGA}", kind="hinted", labels=["motor"])
    chi = Component(EpicsMotor, f"{M_CHI}", kind="hinted", labels=["motor"])
    phi = Component(EpicsMotor, f"{M_PHI}", kind="hinted", labels=["motor"])
    gamma = Component(EpicsMotor, f"{M_GAMMA}", kind="hinted", labels=["motor"])
    delta = Component(EpicsMotor, f"{M_TTH}", kind="hinted", labels=["motor"])

    energy = Component(EpicsSignalRO, "BraggERdbkAO", kind="hinted", labels=["energy"])
    energy_units = Component(EpicsSignalRO, "BraggERdbkAO.EGU", kind="config")


sixc = SixCircle(IOC, name="sixc")
sixc.wait_for_connection()
sixc._update_calc_energy()
