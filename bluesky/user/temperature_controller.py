"""
Create a simulated temperature controller device.

Example::

    temperature = SimulatedTemperatureController(
        "",
        name="temperature",
        swait_pv="gp:userCalc17",
        tolerance=1,
    )
    temperature.wait_for_connection()
    temperature.setup_controller(25, label="temperature controller")

.. note:: This code is used in the documentation.
   Leave it in the `user` directory.
"""

from apstools.devices import PVPositionerSoftDoneWithStop
from apstools.synApps import SwaitRecord
from ophyd import FormattedComponent as FC


class SimulatedTemperatureController(PVPositionerSoftDoneWithStop):
    """
    Simulated temperature controller with swait record.

    The swait record completes the feedback loop, computing
    the next simulated temperature.
    """

    loop = FC(SwaitRecord, "{swait_pv}", kind="config")

    def __init__(self, *args, swait_pv="", **kwargs):
        if len(swait_pv.strip()) == 0:
            raise ValueError("Must supply a value for 'swait_pv'.")

        self.swait_pv = swait_pv

        kwargs["readback_pv"] = f"{swait_pv}.VAL"
        kwargs["setpoint_pv"] = f"{swait_pv}.B"

        super().__init__(*args, **kwargs)

    def setup_controller(
        self,
        setpoint=None,
        label="controller",
        noise=2,
        period="1 second",
        max_change=2,
    ):
        """
        Configure the swait record as a temperature controller.
        """
        swait = self.loop
        swait.reset()  # remove any prior configuration
        swait.description.put(label)
        swait.channels.A.input_pv.put(swait.calculated_value.pvname)
        if setpoint is not None:
            swait.channels.A.input_value.put(setpoint)  # readback
            swait.channels.B.input_value.put(setpoint)  # setpoint
        swait.channels.C.input_value.put(noise)
        swait.channels.D.input_value.put(max_change)
        swait.scanning_rate.put(period)
        swait.calculation.put("A+max(-D,min(D,(B-A)))+C*(RNDM-0.5)")
