"""
configure for data collection in a console session
"""

from .session_logs import logger

logger.info(__file__)

from . import mpl

logger.info("bluesky framework")

from .framework import *
from .devices import *
from .callbacks import *
from .plans import *
from .utils import *

from apstools.utils import *

# last line: ensure we have the console's logger
from .session_logs import logger
logger.info("Startup is complete.")
