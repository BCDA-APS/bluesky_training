"""
simulated noisy temperature using swait record
"""

__all__ = [
    "temperature",
]

from ..session_logs import logger

logger.info(__file__)

from .calculation_records import calcs
from apstools.synApps import SwaitRecord
from ophyd import Component
from ophyd import EpicsSignal
from ophyd import EpicsSignalRO
from ophyd import PVPositioner
from ophyd import Signal
import numpy as np


class MyPvPositioner(PVPositioner):
    setpoint = Component(EpicsSignal, ".B")
    readback = Component(EpicsSignalRO, ".VAL")
    done = Component(Signal, value=True)
    done_value = True
    tolerance = Component(EpicsSignal, ".E")

    def cb_done(self, *args, **kwargs):
        diff = self.readback.get() - self.setpoint.get()
        self.done.put(abs(diff) <= self.tolerance.get())

    def __init__(
        self,
        prefix,
        *,
        limits=None,
        name=None,
        read_attrs=None,
        configuration_attrs=None,
        parent=None,
        egu="",
        **kwargs
    ):
        super().__init__(
            prefix=prefix,
            limits=limits,
            name=name,
            read_attrs=read_attrs,
            configuration_attrs=configuration_attrs,
            parent=parent,
            egu=egu,
            **kwargs
        )
        self.readback.subscribe(self.cb_done)
        self.setpoint.subscribe(self.cb_done)

    def setup_temperature(self, setpoint=None, noise=2, rate=6, tol=1, max_change=2):
        """
        Setup the swait record with new random numbers.

        BLOCKING calls, not a bluesky plan
        """
        tcalc = calcs.calc8
        tcalc.reset()
        tcalc.description.put("temperature")
        tcalc.channels.A.input_pv.put(tcalc.calculated_value.pvname)
        if setpoint is not None:
            tcalc.channels.B.input_value.put(setpoint)
        tcalc.channels.C.input_value.put(noise)
        tcalc.channels.D.input_value.put(max_change)
        tcalc.channels.E.input_value.put(tol)
        tcalc.scanning_rate.put(rate)  # 1 second
        tcalc.calculation.put("A+min(D,(B-A))*RNDM+2*C*(RNDM-0.5)")


temperature = MyPvPositioner(
    "ioc:userCalc8", name="temperature", limits=(-20, 255), egu="C",
)
temperature.wait_for_connection()
temperature.setup_temperature(setpoint=25, noise=0.5, rate=5, tol=1, max_change=2)
