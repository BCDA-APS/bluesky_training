"""
ensure BlueSky is available
"""

__all__ = []

from ..session_logs import logger

logger.info(__file__)
import sys

# ensure BlueSky is available
try:
    import bluesky
except ImportError:
    raise ImportError(
        "No module named `bluesky`\n"
        f"This python is from directory: {sys.prefix}\n"
        "\n"
        "You should exit now and find the ipython with Bluesky."
    )


req_version = (1, 6)
cur_version = tuple(map(int, bluesky.__version__.split(".")[:2]))
if cur_version < req_version:
    ver_str = ".".join((map(str, req_version)))
    raise ValueError(f"Need bluesky version {ver_str} or higher" f", found version {bluesky.__version__}")


import ophyd

req_version = (1, 4)
cur_version = tuple(map(int, ophyd.__version__.split(".")[:2]))
if cur_version < req_version:
    ver_str = ".".join((map(str, req_version)))
    raise ValueError(f"Need ophyd version {ver_str} or higher" f", found version {ophyd.__version__}")
