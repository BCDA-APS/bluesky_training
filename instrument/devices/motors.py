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

from ophyd import EpicsMotor


m1 = EpicsMotor("gp:m1", name="m1", labels=("motor",))
m2 = EpicsMotor("gp:m2", name="m2", labels=("motor",))
m3 = EpicsMotor("gp:m3", name="m3", labels=("motor",))
m4 = EpicsMotor("gp:m4", name="m4", labels=("motor",))
m5 = EpicsMotor("gp:m5", name="m5", labels=("motor",))
m6 = EpicsMotor("gp:m6", name="m6", labels=("motor",))
m7 = EpicsMotor("gp:m7", name="m7", labels=("motor",))
m8 = EpicsMotor("gp:m8", name="m8", labels=("motor",))
m9 = EpicsMotor("gp:m9", name="m9", labels=("motor",))
m10 = EpicsMotor("gp:m10", name="m10", labels=("motor",))
m11 = EpicsMotor("gp:m11", name="m11", labels=("motor",))
m12 = EpicsMotor("gp:m12", name="m12", labels=("motor",))
m13 = EpicsMotor("gp:m13", name="m13", labels=("motor",))
m14 = EpicsMotor("gp:m14", name="m14", labels=("motor",))
m15 = EpicsMotor("gp:m15", name="m15", labels=("motor",))
m16 = EpicsMotor("gp:m16", name="m16", labels=("motor",))
