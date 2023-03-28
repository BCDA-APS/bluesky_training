"""
initialize the bluesky framework
"""

__all__ = """
    RE  cat  sd  bec  peaks
    bp  bps  bpp
    summarize_plan
    np
    """.split()

import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).absolute().parent.parent.parent))

from .. import iconfig
from bluesky import RunEngine
from bluesky import SupplementalData
from bluesky.callbacks.best_effort import BestEffortCallback
from bluesky.magics import BlueskyMagics
from bluesky.simulators import summarize_plan
from bluesky.utils import PersistentDict
from bluesky.utils import ProgressBarManager
from bluesky.utils import ts_msg_hook
from IPython import get_ipython
from ophyd.signal import EpicsSignalBase
import databroker
import ophyd
import warnings

# convenience imports
import bluesky.plans as bp
import bluesky.plan_stubs as bps
import bluesky.preprocessors as bpp
import numpy as np


def get_md_path():
    path = iconfig.get("RUNENGINE_MD_PATH")
    if path is None:
        path = pathlib.Path.home() / "Bluesky_RunEngine_md"
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
# from bluesky.callbacks.broker import verify_files_saved
# RE.subscribe(post_run(verify_files_saved), 'stop')

# Uncomment the following lines to turn on
# verbose messages for debugging.
# ophyd.logger.setLevel(logging.DEBUG)

ophyd.set_cl(iconfig.get("OPHYD_CONTROL_LAYER", "PyEpics").lower())
logger.info(f"using ophyd control layer: {ophyd.cl.name}")

# diagnostics
# RE.msg_hook = ts_msg_hook

# set default timeout for all EpicsSignal connections & communications
TIMEOUT = 60
if not EpicsSignalBase._EpicsSignalBase__any_instantiated:
    EpicsSignalBase.set_defaults(
        auto_monitor=True,
        timeout=iconfig.get("PV_READ_TIMEOUT", TIMEOUT),
        write_timeout=iconfig.get("PV_WRITE_TIMEOUT", TIMEOUT),
        connection_timeout=iconfig.get("PV_CONNECTION_TIMEOUT", TIMEOUT),
    )
