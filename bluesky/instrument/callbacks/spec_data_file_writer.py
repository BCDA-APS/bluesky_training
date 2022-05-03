"""
custom callbacks
"""

__all__ = [
    "specwriter",
    "spec_comment",
    "newSpecFile",
]

from ..session_logs import logger

logger.info(__file__)

try:
    import apstools.callbacks as APS_fw
except ModuleNotFoundError:
    import apstools.filewriters as APS_fw
import apstools.utils
import datetime
import pathlib

# write scans to SPEC data file
specwriter = APS_fw.SpecWriterCallback()
# make the SPEC file in current working directory (assumes is writable)
_path = pathlib.Path().cwd()
specwriter.newfile(str(_path / specwriter.spec_filename))


def spec_comment(comment, doc=None):
    # supply our specwriter to the standard routine
    APS_fw.spec_comment(comment, doc, specwriter)


def newSpecFile(title, scan_id=1):
    """
    user choice of the SPEC file name

    cleans up title, prepends month and day and appends file extension
    """
    global specwriter
    mmdd = str(datetime.datetime.now()).split()[0][5:].replace("-", "_")
    clean = apstools.utils.cleanupText(title)
    fname = pathlib.Path(f"{mmdd}_{clean}.dat")
    if fname.exists():
        logger.warning(f">>> file already exists: {fname} <<<")
        specwriter.newfile(str(fname))  # TODO: , RE=RE)
        handled = "appended"

    else:
        specwriter.newfile(str(fname), scan_id=scan_id)  # TODO: , RE=RE)
        handled = "created"

    logger.info(f"SPEC file name : {specwriter.spec_filename}")
    logger.info(f"File will be {handled} at end of next bluesky scan.")
