"""
ensure BlueSky is available
"""

__all__ = []

import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

import sys
from .. import iconfig

# ensure BlueSky is available
try:
    import bluesky
except ImportError:
    raise ImportError(
        "No module named `bluesky`\n"
        f"This python is from directory: {sys.prefix}\n"
        "\n"
        "You should exit now and find a Python with Bluesky."
    )

# ensure minimum bluesky version

req_version = tuple(iconfig.get("MINIMUM_BLUESKY_VERSION", (1, 8)))
cur_version = tuple(map(int, bluesky.__version__.split(".")[:2]))
if cur_version < req_version:
    ver_str = ".".join((map(str, req_version)))
    raise ValueError(
        f"Need bluesky version {ver_str} or higher"
        f", found version {bluesky.__version__}"
    )

# ensure minimum ophyd version

import ophyd

req_version = tuple(iconfig.get("MINIMUM_OPHYD_VERSION", (1, 6)))
cur_version = tuple(map(int, ophyd.__version__.split(".")[:2]))
if cur_version < req_version:
    ver_str = ".".join((map(str, req_version)))
    raise ValueError(
        f"Need ophyd version {ver_str} or higher"
        f", found version {ophyd.__version__}"
    )


# ensure minimum databroker version

import databroker

req_version = tuple(iconfig.get("MINIMUM_DATABROKER_VERSION", (1, 2)))
cur_version = tuple(map(int, databroker.__version__.split(".")[:2]))
if cur_version < req_version:
    ver_str = ".".join((map(str, req_version)))
    raise ValueError(
        f"Need databroker version {ver_str} or higher"
        f", found version {databroker.__version__}"
    )
