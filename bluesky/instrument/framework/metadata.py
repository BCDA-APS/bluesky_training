"""
define standard experiment metadata
"""

__all__ = []

import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

from .. import iconfig
from ..epics_signal_config import epics_scan_id_source
from ..epics_signal_config import scan_id_epics
import apstools
import bluesky
import databroker
from datetime import datetime
import epics
import getpass
import h5py
import intake
import matplotlib
import numpy
import ophyd
import os
import pyRestTable
import socket
import spec2nexus

from .initialize import cat, RE


HOSTNAME = socket.gethostname() or "localhost"
USERNAME = getpass.getuser() or "Bluesky user"

# useful diagnostic to record with all data
versions = dict(
    apstools=apstools.__version__,
    bluesky=bluesky.__version__,
    databroker=databroker.__version__,
    epics=epics.__version__,
    h5py=h5py.__version__,
    intake=intake.__version__,
    matplotlib=matplotlib.__version__,
    numpy=numpy.__version__,
    ophyd=ophyd.__version__,
    pyRestTable=pyRestTable.__version__,
    spec2nexus=spec2nexus.__version__,
)

# Set up default metadata
RE.md["databroker_catalog"] = cat.name
RE.md["login_id"] = USERNAME + "@" + HOSTNAME
RE.md.update(iconfig.get("RUNENGINE_METADATA", {}))
RE.md["versions"] = versions
RE.md["pid"] = os.getpid()
if scan_id_epics is not None:
    RE.md["scan_id"] = scan_id_epics.get()
conda_prefix = os.environ.get("CONDA_PREFIX")
if conda_prefix is not None:
    RE.md["conda_prefix"] = conda_prefix
del conda_prefix
