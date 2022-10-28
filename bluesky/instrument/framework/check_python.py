"""
make sure we have the software packages we need
"""

__all__ = []

import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

from .. import iconfig
import sys

# ensure minimum Python version

req_version = tuple(iconfig.get("MINIMUM_PYTHON_VERSION", (3, 7)))
cur_version = sys.version_info
if cur_version < req_version:
    ver_str = ".".join((map(str, req_version)))
    raise RuntimeError(
        f"Requires Python {ver_str}+ with the Bluesky framework.\n"
        f"You have Python {sys.version} from {sys.prefix}\n"
        "\n"
        "You should exit now and start a Python"
        " with the Bluesky framework."
    )
