"""
Create a simulated temperature controller device.

Example with ``swait`` record::

    temperature = SimulatedTemperatureControllerSwait(
        "",
        name="temperature",
        swait_pv="gp:userCalc17",
        tolerance=1,
    )
    temperature.wait_for_connection()
    temperature.setup(25, label="temperature controller")

Example with ``transform`` record::

    temperature = SimulatedTemperatureControllerTransform(
        "",
        name="temperature",
        transform_pv="gp:userTran1",
    )
    temperature.wait_for_connection()
    temperature.setup(25, label="temperature controller", noise=0.2, max_change=0.2, tolerance=0.999)

.. note:: This code is used in the documentation.
   Leave it in the `user` directory.

.. autosummary::

    ~SimulatedTemperatureControllerSwait
    ~SimulatedTemperatureControllerTransform
"""

# TODO: Hoist this code to apstools.  For 1.6.18.
# TODO: After that, refactor and use here.

from apstools.devices import PVPositionerSoftDoneWithStop
from apstools.synApps import SwaitRecord
from apstools.synApps import TransformRecord
from ophyd import FormattedComponent as FC


class SimulatedTemperatureControllerSwait(PVPositionerSoftDoneWithStop):
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

    def setup(
        self,
        setpoint,
        label="controller",
        noise=1,
        period="1 second",
        max_change=1,
    ):
        """
        Configure the swait record as a temperature controller.
        """
        self.wait_for_connection()
        swait = self.loop
        swait.reset()  # remove any prior configuration
        swait.description.put(label)
        swait.channels.A.input_value.put(setpoint)  # readback
        swait.channels.A.input_pv.put(swait.calculated_value.pvname)
        swait.channels.B.input_value.put(setpoint)  # setpoint
        swait.channels.C.input_value.put(noise)
        swait.channels.D.input_value.put(max_change)
        swait.scanning_rate.put(period)
        swait.precision.put(3)
        swait.calculated_value.put(setpoint)  # preset initial value
        swait.calculation.put("A+max(-D,min(D,(B-A)))+C*(RNDM-0.5)")


class SimulatedTemperatureControllerTransform(PVPositionerSoftDoneWithStop):
    """
    Simulated temperature controller with transform record.

    The transform record completes the feedback loop, computing
    the next simulated temperature and reporting if the readback is
    "in position".
    """

    loop = FC(TransformRecord, "{transform_pv}", kind="config")

    def __init__(self, *args, transform_pv="", **kwargs):
        if len(transform_pv.strip()) == 0:
            raise ValueError("Must supply a value for 'transform_pv'.")

        self.transform_pv = transform_pv

        kwargs["readback_pv"] = f"{transform_pv}.H"
        kwargs["setpoint_pv"] = f"{transform_pv}.B"

        super().__init__(*args, **kwargs)

        self.following_error = self.loop.channels.E.current_value

    def setup(
        self,
        setpoint,
        label="controller",
        noise=2,
        period="1 second",
        max_change=2,
        tolerance=1,
    ):
        """
        Configure the transform record as a temperature controller.
        """
        self.wait_for_connection()
        self.tolerance.put(tolerance)

        transform = self.loop
        transform.reset()  # remove any prior configuration
        transform.description.put(label)

        transform.channels.A.comment.put("last readback")
        transform.channels.A.current_value.put(setpoint)  # readback
        transform.channels.A.input_pv.put(transform.channels.H.current_value.pvname)

        transform.channels.B.comment.put("setpoint")
        transform.channels.B.current_value.put(setpoint)  # setpoint

        transform.channels.C.comment.put("noise level")
        transform.channels.C.current_value.put(noise)

        transform.channels.D.comment.put("max_change")
        transform.channels.D.current_value.put(max_change)

        transform.channels.E.comment.put("following error")
        transform.channels.E.expression.put("B-A")

        transform.channels.F.comment.put("T step")
        transform.channels.F.expression.put("max(-D,min(D,E))")

        transform.channels.G.comment.put("T noise")
        transform.channels.G.expression.put("C*(RNDM-0.5)")

        transform.channels.H.comment.put("T readback")
        transform.channels.H.current_value.put(setpoint)  # preset initial value
        transform.channels.H.expression.put("A+F+G")

        transform.channels.I.comment.put("tolerance")
        transform.channels.I.current_value.put(tolerance)

        transform.channels.J.comment.put("in position")
        transform.channels.J.expression.put("abs(H-B)<=I")

        transform.precision.put(3)

        transform.scanning_rate.put(period)
