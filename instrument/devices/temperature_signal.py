"""
simulated noisy temperature controller using swait record
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
    # positioner
    setpoint = Component(EpicsSignal, ".B")
    readback = Component(EpicsSignal, ".VAL")  # THIS readback IS writable!
    done = Component(Signal, value=True)
    done_value = True

    # additional, for the simulator
    calculation = Component(EpicsSignal, ".CALC")
    description = Component(EpicsSignal, ".DESC")
    max_change = Component(EpicsSignal, ".D")
    noise = Component(EpicsSignal, ".C")
    previous_value_pv = Component(EpicsSignal, ".INAN")
    scanning_rate = Component(EpicsSignal, ".SCAN")
    tolerance = Component(EpicsSignal, ".E")
    report_dmov_changes = Component(Signal, value=True, kind="omitted")

    def cb_done(self, *args, **kwargs):
        """
        Called when either setpoint or readback change (EPICS CA monitor event).
        """
        # fmt: off
        if (
            kwargs.get("obj") is not None 
            and
            kwargs["obj"].name == self.setpoint.name
        ):
            # When the setpoint is changed, force done=False.
            # For any move, done must go != done_value, then back to done_value (True).
            # Without this part, a small move (within tolerance) will not return.
            # Next update of readback will compute self.done.
            self.done.put(not self.done_value)
            return
        # fmt: on
        diff = self.readback.get() - self.setpoint.get()
        dmov = abs(diff) <= self.tolerance.get()
        if self.report_dmov_changes.get() and dmov != self.done.get():
            logger.debug(f"{self.name} reached: {dmov}")
        self.done.put(dmov)

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
        **kwargs,
    ):
        super().__init__(
            prefix=prefix,
            limits=limits,
            name=name,
            read_attrs=read_attrs,
            configuration_attrs=configuration_attrs,
            parent=parent,
            egu=egu,
            **kwargs,
        )
        self.readback.subscribe(self.cb_done)
        self.setpoint.subscribe(self.cb_done)

    def setup_temperature(
        self,
        setpoint=None,
        noise=2,
        rate=6,
        tol=1,
        max_change=2,
        report_dmov_changes=True,
    ):
        """
        Setup the swait record with new random numbers.

        BLOCKING calls, not a bluesky plan
        """
        calcs.calc8.reset()  # remove any prior configuration
        self.description.put("temperature")
        self.report_dmov_changes.put(report_dmov_changes)
        self.previous_value_pv.put(self.readback.pvname)
        if setpoint is not None:
            self.setpoint.put(setpoint)
            self.readback.put(setpoint)
        self.noise.put(noise)
        self.max_change.put(max_change)
        self.tolerance.put(tol)
        self.scanning_rate.put(rate)  # 1 second
        self.calculation.put("A+max(-D,min(D,(B-A)))+C*(RNDM-0.5)")


temperature = MyPvPositioner(
    "gp:userCalc8", name="temperature", limits=(-20, 255), egu="C",
)
temperature.wait_for_connection()
temperature.setup_temperature(
    setpoint=25, noise=1, rate=5, tol=1, max_change=2, report_dmov_changes=False
)
