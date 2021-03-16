"""
analyze an image frame
"""

__all__ = [
    "analyze_image",
]

from ..session_logs import logger

logger.info(__file__)

import numpy as np
import pyRestTable
from scipy.ndimage.measurements import center_of_mass
from scipy.integrate import trapz


def analyze_peak(y_arr, x_arr=None):
    """Measures of peak center & width."""
    # clear all results
    center_position = None
    centroid_position = None
    maximum_position = None
    minimum_position = None
    crossings = None
    fwhm = None

    y = np.array(y_arr)
    num_points = len(y)
    if x_arr is None:
        x = np.arange(num_points)
    else:
        if len(x_arr) != num_points:
            raise ValueError("x and y arrays are not of the same length.")
        x = np.array(x_arr)

    # Compute x value at min and max of y
    y_max_index = y.argmax()
    y_min_index = y.argmin()
    maximum_position = (x[y_max_index], y[y_max_index])
    minimum_position = (x[y_min_index], y[y_min_index])

    (center_position,) = np.interp(center_of_mass(y), np.arange(num_points), x)

    # # for now, assume x is regularly spaced, otherwise, should be integrals
    # sumY = sum(y)
    # sumXY = sum(x*y)
    # sumXXY = sum(x*x*y)
    # # weighted_mean is same as center_position
    # # weighted_mean = sumXY / sumY
    # stdDev = np.sqrt((sumXXY / sumY) - (sumXY / sumY)**2)

    mid = (np.max(y) + np.min(y)) / 2
    crossings = np.where(np.diff((y > mid).astype(np.int)))[0]
    _cen_list = []
    for cr in crossings.ravel():
        _x = x[cr : cr + 2]
        _y = y[cr : cr + 2] - mid

        dx = np.diff(_x)[0]
        dy = np.diff(_y)[0]
        m = dy / dx
        _cen_list.append((-_y[0] / m) + _x[0])

    if _cen_list:
        centroid_position = np.mean(_cen_list)
        crossings = np.array(_cen_list)
        if len(_cen_list) >= 2:
            fwhm = np.abs(crossings[-1] - crossings[0], dtype=float)

    return dict(
        centroid_position=centroid_position,
        fwhm=fwhm,
        # half_max=mid,
        crossings=crossings,
        maximum=maximum_position,
        center_position=center_position,
        minimum=minimum_position,
        # stdDev=stdDev,
    )


def analyze_image(image):
    horizontal = analyze_peak(image.sum(axis=0))
    vertical = analyze_peak(image.sum(axis=1))

    table = pyRestTable.Table()
    table.addLabel("measure")
    table.addLabel("vertical (dim_1)")
    table.addLabel("horizontal (dim_2)")
    for key in horizontal.keys():
        table.addRow(
            (
                key,
                vertical[key],
                horizontal[key],
            )
        )

    print(table)
