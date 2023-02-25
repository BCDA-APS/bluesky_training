"""
example custom scan plan

Find the peak of noisy v. m1 in the range of +/- 2.
"""

__all__ = [
    "two_pass_scan",
    "findpeak_multipass",
    "repeat_findpeak",
]

import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

from .. import iconfig
from ..devices import change_noisy_parameters
from ..devices import m1
from ..devices import noisy
from ..utils.image_analysis import analyze_peak
from bluesky import plans as bp
import pyRestTable

if iconfig.get("framework", "unknown") == "queueserver":
    from ..queueserver_framework import cat
else:
    from ..framework import cat


def _get_peak_stats(uid, yname, xname):
    """(internal) Convenience function."""
    logger.debug("compute scan statistics: '%s(%s)' uid: %s", yname, xname, uid)
    try:
        ds = cat[uid].primary.read()
        return analyze_peak(ds[yname].data, ds[xname].data)
    except NameError:
        logger.warning("Catalog object not defined.  No peak statistics.")
        return {}


def two_pass_scan(md=None):
    """
    Find the peak of noisy v. m1 in the range of +/- 2.

    We know the peak center of the simulated noisy detector
    is positioned randomly between -1 to +1.  Overscan that
    range to find both sides of the peak.

    This is a 2 scan procedure.  First scan passes through
    the full range.  Second scan is centered on the peak
    and width of the first scan.
    """
    md = md or {}

    change_noisy_parameters()

    sig = 2
    expansion_factor = 1.2  # expand search by FWHM*expansion_factor
    m1.move(0)
    for i in range(1, 3):
        md["scan_sequence"] = i
        uid = yield from bp.rel_scan([noisy], m1, -sig, +sig, 23, md=md)
        stats = _get_peak_stats(uid, noisy.name, m1.name)
        if len(stats) > 0:
            sig = stats["fwhm"] * expansion_factor
            m1.move(stats["centroid_position"])
        else:
            logger.warning("Catalog object not found.  No peak statistics.")
            break


def findpeak_multipass(number_of_scans=4, number_of_points=23, magnify=1.2, md=None):
    """
    find peak of noisy v. m1 by repeated scans with refinement

    basically::

        sig = 2.1
        m1.move(0.0)
        for _ in range(3):
            RE(bp.rel_scan([noisy], m1, -sig, sig, 23))
            stats = _get_peak_stats(uid, noisy.name, m1.name)
            sig = stats["fwhm"]
            m1.move(stats["centroid_position"])
    """
    md = md or {}
    md["number_of_scans"] = number_of_scans
    sig = 2.1 / magnify
    cen = 0
    results = []
    for _again in range(number_of_scans):
        md["scan_sequence_number"] = _again+1
        m1.move(cen)
        uid = yield from bp.rel_scan(
            [noisy], m1, -magnify * sig, magnify * sig, number_of_points, md=md
        )
        stats = _get_peak_stats(uid, noisy.name, m1.name)
        if len(stats) > 0:
            scan_id = cat[uid].metadata["start"]["scan_id"]
            sig = stats["fwhm"]
            cen = stats["centroid_position"]
            results.append((scan_id, cen, sig))
        else:
            break
    m1.move(cen)

    tbl = pyRestTable.Table()
    tbl.labels = "scan_id center FWHM".split()
    for row in results:
        tbl.addRow(row)
    logger.info("iterative results:\n%s", str(tbl))


def repeat_findpeak(iters=1, md=None):
    """Repeat findpeak_multipass() with new parameters each time."""
    md = md or {}
    for _i in range(iters):
        md["iteration"] = _i+1
        # FIXME: apstools.utils.trim_plot_lines(bec, 4, m1, noisy)
        change_noisy_parameters()
        yield from findpeak_multipass(md=md)
        logger.info("Finished #%d of %d iterations", _i + 1, iters)
