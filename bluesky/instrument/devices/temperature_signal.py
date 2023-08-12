"""
simulated noisy temperature controller using swait record
"""

__all__ = [
    "temperature",
]

import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

from .. import iconfig
from .calculation_records import calcs
from ophyd import Component
from ophyd import EpicsSignal
from ophyd import PVPositioner
from ophyd import Signal


IOC = iconfig.get("GP_IOC_PREFIX", "gp:")


class MyPvPositioner(PVPositioner):
    # positioner
    readback = Component(EpicsSignal, ".VAL")  # THIS readback IS writable!
    setpoint = Component(EpicsSignal, ".B")
    done = Component(Signal, value=True)
    done_value = True

    # additional, for the simulator
    calculation = Component(EpicsSignal, ".CALC", kind="config")
    description = Component(EpicsSignal, ".DESC", kind="config")
    max_change = Component(EpicsSignal, ".D", kind="config")
    noise = Component(EpicsSignal, ".C", kind="config")
    previous_value_pv = Component(EpicsSignal, ".INAN", kind="config")
    scanning_rate = Component(EpicsSignal, ".SCAN", kind="config")
    tolerance = Component(EpicsSignal, ".E", kind="config")
    report_dmov_changes = Component(Signal, value=True, kind="omitted")

    def cb_readback(self, *args, **kwargs):
        """
        Called when readback changes (EPICS CA monitor event).
        """
        diff = self.readback.get() - self.setpoint.get()
        dmov = abs(diff) <= self.tolerance.get()
        if self.report_dmov_changes.get() and dmov != self.done.get():
            logger.debug(f"{self.name} reached: {dmov}")
        self.done.put(dmov)

    def cb_setpoint(self, *args, **kwargs):
        """
        Called when setpoint changes (EPICS CA monitor event).

        When the setpoint is changed, force done=False.  For any move,
        done must go != done_value, then back to done_value (True).
        Without this response, a small move (within tolerance) will not return.
        Next update of readback will compute self.done.
        """
        self.done.put(not self.done_value)

    def __init__(self, *args, **kwargs):
        """
        These are the arguments in the full signature:

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
        """
        super().__init__(*args, **kwargs)

        # setup callbacks on readback and setpoint
        self.readback.subscribe(self.cb_readback)
        self.setpoint.subscribe(self.cb_setpoint)

        # the readback needs no adjective
        self.readback.name = self.name

    @property
    def inposition(self):
        """
        Report (boolean) if positioner is done.
        """
        return self.done.get() == self.done_value

    def stop(self, *, success=False):
        """
        Hold the current readback when the stop() method is called and not done.
        """
        if not self.done.get():
            self.setpoint.put(self.position)

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
    f"{IOC}userCalc8", name="temperature", limits=(-20, 255), egu="C",
)
temperature.wait_for_connection()
temperature.setup_temperature(
    setpoint=25, noise=1, rate=5, tol=1, max_change=2, report_dmov_changes=False
)
