"""
example motors
"""

__all__ = """
    m1  m2  m3  m4
    m5  m6  m7  m8
    m9  m10 m11 m12
    m13 m14 m15 m16
""".split()

from ..session_logs import logger

logger.info(__file__)

from ophyd import EpicsMotor, Component, EpicsSignal
import os

GP_IOC_PREFIX = os.environ.get("GP_IOC_PREFIX", "gp:")


class MyEpicsMotor(EpicsMotor):
    steps_per_revolution = Component(EpicsSignal, ".SREV", kind="omitted")

m1 = MyEpicsMotor(f"{GP_IOC_PREFIX}m1", name="m1", labels=("motor",))
m2 = MyEpicsMotor(f"{GP_IOC_PREFIX}m2", name="m2", labels=("motor",))
m3 = MyEpicsMotor(f"{GP_IOC_PREFIX}m3", name="m3", labels=("motor",))
m4 = MyEpicsMotor(f"{GP_IOC_PREFIX}m4", name="m4", labels=("motor",))
m5 = MyEpicsMotor(f"{GP_IOC_PREFIX}m5", name="m5", labels=("motor",))
m6 = MyEpicsMotor(f"{GP_IOC_PREFIX}m6", name="m6", labels=("motor",))
m7 = MyEpicsMotor(f"{GP_IOC_PREFIX}m7", name="m7", labels=("motor",))
m8 = MyEpicsMotor(f"{GP_IOC_PREFIX}m8", name="m8", labels=("motor",))
m9 = MyEpicsMotor(f"{GP_IOC_PREFIX}m9", name="m9", labels=("motor",))
m10 = MyEpicsMotor(f"{GP_IOC_PREFIX}m10", name="m10", labels=("motor",))
m11 = MyEpicsMotor(f"{GP_IOC_PREFIX}m11", name="m11", labels=("motor",))
m12 = MyEpicsMotor(f"{GP_IOC_PREFIX}m12", name="m12", labels=("motor",))
m13 = MyEpicsMotor(f"{GP_IOC_PREFIX}m13", name="m13", labels=("motor",))
m14 = MyEpicsMotor(f"{GP_IOC_PREFIX}m14", name="m14", labels=("motor",))
m15 = MyEpicsMotor(f"{GP_IOC_PREFIX}m15", name="m15", labels=("motor",))
m16 = MyEpicsMotor(f"{GP_IOC_PREFIX}m16", name="m16", labels=("motor",))

m1.wait_for_connection()
m1.steps_per_revolution.put(2000)
