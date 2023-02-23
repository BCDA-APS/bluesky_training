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


def newSpecFile(title, scan_id=1, RE=None):
    """
    User choice of the SPEC file name.

    Cleans up title, prepends month and day and appends file extension.
    If ``RE`` is passed, then resets ``RE.md["scan_id"] = scan_id``.
    """
    global specwriter
    mmdd = str(datetime.datetime.now()).split()[0][5:].replace("-", "_")
    clean = apstools.utils.cleanupText(title)
    fname = pathlib.Path(f"{mmdd}_{clean}.dat")
    if fname.exists():
        logger.warning(f">>> file already exists: {fname} <<<")
        if RE is None:
            specwriter.newfile(fname)
        else:
            specwriter.newfile(fname, RE=RE)
        handled = "appended"

    else:
        if RE is None:
            specwriter.newfile(fname, scan_id=scan_id)
        else:
            specwriter.newfile(fname, scan_id=scan_id, RE=RE)
        handled = "created"

    logger.info(f"SPEC file name : {specwriter.spec_filename}")
    logger.info(f"File will be {handled} at end of next bluesky scan.")
