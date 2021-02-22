"""
support a .ipython/user directory for user files
"""

__all__ = []

from ..session_logs import logger

logger.info(__file__)

# import IPython.paths
import os
import sys

user_dir = os.path.join(
    # IPython.paths.get_ipython_dir(),
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "user",))
)
if os.path.exists(user_dir):
    sys.path.append(user_dir)
    logger.info(f"User code directory: {user_dir}")
del user_dir
