"""
custom callbacks
"""

__all__ = [
    "specwriter",
    "spec_comment",
    "newSpecFile",
]

import logging

logger = logging.getLogger(__name__)
logger.info(__file__)

try:
    import apstools.callbacks as APS_fw
except ModuleNotFoundError:
    import apstools.filewriters as APS_fw

import datetime
import pathlib

import apstools.utils

from ..framework.initialize import RE

# write scans to SPEC data file
specwriter = APS_fw.SpecWriterCallback()
# make the SPEC file in current working directory (assumes is writable)
_path = pathlib.Path().cwd()
specwriter.newfile(_path / specwriter.spec_filename)

try:
    # feature new in apstools 1.6.14
    from apstools.plans import label_stream_wrapper

    def motor_start_preprocessor(plan):
        return label_stream_wrapper(plan, "motor", when="start")

    RE.preprocessors.append(motor_start_preprocessor)
except Exception:
    logger.warning("Could load support to log motors positions.")


def spec_comment(comment, doc=None):
    # supply our specwriter to the standard routine
    APS_fw.spec_comment(comment, doc, specwriter)


def RE_finder():
    """
    Find RunEngine object from namespaces of the stack.

    * Search backwards through each frame in the stack.
        * Find any RunEngine objects.
            * Prefer one with name 'RE'.
            * Otherwise, pick the first one.
    * Otherwise, return 'None'.
    
    suggestion: Hoist to apstools.utils
    """
    import inspect
    from bluesky import RunEngine

    fallback = None
    for fr in inspect.stack():  # Walk backwards from this frame.
        static = fr.frame.f_locals.copy()  # f_locals will change during 'for'.
        for k, v in static.items():
            if isinstance(v, RunEngine):  # Got one!
                if k == "RE":
                    return v  # Ideal selection.
                fallback = fallback or None
    return fallback


def newSpecFile(title, scan_id=None, RE=None):
    """
    User choice of the SPEC file name.

    Cleans up title, prepends month and day and appends file extension.
    If ``RE`` is passed, then resets ``RE.md["scan_id"] = scan_id``.

    If the SPEC file already exists, then ``scan_id`` is ignored and
    ``RE.md["scan_id"]`` is set to the last scan number in the file.
    """
    kwargs = {}
    RE = RE or RE_finder()  # Search for a defined RunEngine instance
    if RE is not None:
        kwargs["RE"] = RE

    mmdd = str(datetime.datetime.now()).split()[0][5:].replace("-", "_")
    clean = apstools.utils.cleanupText(title)
    fname = pathlib.Path(f"{mmdd}_{clean}.dat")
    if fname.exists():
        logger.warning(f">>> file already exists: {fname} <<<")
        handled = "appended"
    else:
        kwargs["scan_id"] = scan_id or 1
        handled = "created"

    specwriter.newfile(fname, **kwargs)

    logger.info(f"SPEC file name : {specwriter.spec_filename}")
    logger.info(f"File will be {handled} at end of next bluesky scan.")
