"""
4-circle diffractometer, connected to EpicsMotor records.

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
    fourc
""".split()

import logging

logger = logging.getLogger(__name__)
logger.info(__file__)

import hkl
from ophyd import Component
from ophyd import EpicsMotor
from ophyd import EpicsSignalRO

from .. import iconfig

IOC = iconfig.get("GP_IOC_PREFIX", "gp:")
M_TTH = "m29"
M_TH = "m30"
M_CHI = "m31"
M_PHI = "m32"


class FourCircle(hkl.SimMixin, hkl.E4CV):
    """
    Our 4-circle.  Eulerian, vertical scattering orientation.

    Energy obtained (RO) from monochromator.
    """

    # the reciprocal axes are defined by SimMixin

    omega = Component(EpicsMotor, f"{M_TH}", kind="hinted", labels=["motor"])
    chi = Component(EpicsMotor, f"{M_CHI}", kind="hinted", labels=["motor"])
    phi = Component(EpicsMotor, f"{M_PHI}", kind="hinted", labels=["motor"])
    tth = Component(EpicsMotor, f"{M_TTH}", kind="hinted", labels=["motor"])

    energy = Component(EpicsSignalRO, "BraggERdbkAO", kind="hinted", labels=["energy"])
    energy_units = Component(EpicsSignalRO, "BraggERdbkAO.EGU", kind="config")


fourc = FourCircle(IOC, name="fourc")
fourc.wait_for_connection()
fourc._update_calc_energy()
