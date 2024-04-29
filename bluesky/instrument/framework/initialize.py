"""
Initialize the bluesky framework.
"""

__all__ = """
    RE  cat  sd  bec  peaks
    bp  bps  bpp
    summarize_plan
    np
    oregistry
""".split()

import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).absolute().parent.parent.parent))

from .. import iconfig
from apstools.utils import warn_if_not_aps_controls_subnet
from bluesky import RunEngine
from bluesky import SupplementalData
from bluesky.callbacks.best_effort import BestEffortCallback
from bluesky.magics import BlueskyMagics
from bluesky.simulators import summarize_plan  # noqa
from bluesky.utils import PersistentDict
from bluesky.utils import ProgressBarManager
from bluesky.utils import ts_msg_hook  # noqa
from IPython import get_ipython
from ophydregistry import Registry
import databroker
import ophyd
import warnings  # noqa

# convenience imports
import bluesky.plans as bp  # noqa
import bluesky.plan_stubs as bps  # noqa
import bluesky.preprocessors as bpp  # noqa
import numpy as np  # noqa

# Post a warning if at APS but not on controls subnet.
warn_if_not_aps_controls_subnet()


def get_md_path():
    path = iconfig.get("RUNENGINE_MD_PATH")
    if path is None:
        path = pathlib.Path.home() / ".config" / "Bluesky_RunEngine_md"
    else:
        path = pathlib.Path(path)
    logger.info("RunEngine metadata saved in directory: %s", str(path))
    return str(path)


# Set up a RunEngine and use metadata backed PersistentDict
RE = RunEngine({})
RE.md = PersistentDict(get_md_path())

# Connect with our mongodb database
catalog_name = iconfig.get("DATABROKER_CATALOG", "training")
# databroker v2 api
try:
    cat = databroker.catalog[catalog_name]
    logger.info("using databroker catalog '%s'", cat.name)
except KeyError:
    cat = databroker.temp().v2
    logger.info("using TEMPORARY databroker catalog '%s'", cat.name)

# Subscribe metadatastore to documents.
# If this is removed, data is not saved to metadatastore.
RE.subscribe(cat.v1.insert)

# Set up SupplementalData.
sd = SupplementalData()
RE.preprocessors.append(sd)

if iconfig.get("USE_PROGRESS_BAR", False):
    # Add a progress bar.
    pbar_manager = ProgressBarManager()
    RE.waiting_hook = pbar_manager

# Register bluesky IPython magics.
_ipython = get_ipython()
if _ipython is not None:
    _ipython.register_magics(BlueskyMagics)

# Set up the BestEffortCallback.
bec = BestEffortCallback()
RE.subscribe(bec)
peaks = bec.peaks  # just as alias for less typing
bec.disable_baseline()

# At the end of every run, verify that files were saved and
# print a confirmation message.
if iconfig.get("VERIFY_FILES_SAVED", False):
    from bluesky.callbacks.broker import post_run
    from bluesky.callbacks.broker import verify_files_saved

    RE.subscribe(post_run(verify_files_saved), "stop")

ophyd.logger.setLevel(iconfig.get("LOGGING", {}).get("OPHYD_LOGGER_LEVEL", "WARNING"))
ophyd.set_cl(iconfig.get("OPHYD_CONTROL_LAYER", "PyEpics").lower())
logger.info(f"using ophyd control layer: {ophyd.cl.name}")

if iconfig.get("ADD_DIAGNOSTIC_MESSAGES", False):
    # Log bluesky Message objects in RunEngine (follow plan's progress).
    RE.msg_hook = ts_msg_hook

if iconfig.get("RUN_ENGINE_SCAN_ID_PV") is not None:
    from ..epics_signal_config import epics_scan_id_source
    from ..epics_signal_config import scan_id_epics

    # tell RunEngine to use the EPICS PV to provide the scan_id.
    RE.scan_id_source = epics_scan_id_source
    scan_id_epics.wait_for_connection()
    RE.md["scan_id"] = scan_id_epics.get()

# Create a registry of ophyd devices
oregistry = Registry(auto_register=True)
