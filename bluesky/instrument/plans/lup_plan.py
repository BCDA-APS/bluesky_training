"""
lup: lineup
"""

__all__ = [
    "lup",
]

import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

from bluesky import plan_stubs as bps
from bluesky import plans as bp

from ..framework.initialize import bec


def lup(detectors, motor, start, finish, npts=5, key="cen"):
    """
    Lineup a positioner.

    Step-scan the motor from start to finish and collect data from the detectors.
    The **first** detector in the list will be used to assess alignment.
    The statistical measure is selected by ``key`` with a default of
    center: ``key="cen"``.

    The bluesky ``BestEffortCallback``is required, with plots enabled, to
    collect the data for the statistical measure.

    If the chosen key is reported, the `lup()` plan will move the positioner to
    the new value at the end of the plan and print the new position.
    """
    det0 = detectors[0].name
    print(f"{det0=}")
    yield from bp.rel_scan(detectors, motor, start, finish, npts)

    yield from bps.sleep(1)

    if det0 in bec.peaks[key]:
        target = bec.peaks[key][det0]
        if isinstance(target, tuple):
            target = target[0]
        print(f"want to move {motor.name} to {target}")
        yield from bps.mv(motor, target)
        print(f"{motor.name}={motor.position}")
    else:
        print(f"'{det0}' not found in {bec.peaks[key]}")
