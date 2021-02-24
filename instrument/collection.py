"""
configure for data collection in a console session
"""

from .session_logs import logger

logger.info(__file__)

from . import mpl

logger.info("#### Bluesky Framework ####")
from .framework import *

logger.info("#### Devices ####")
from .devices import *

logger.info("#### Callbacks ####")
from .callbacks import *

logger.info("#### Plans ####")
from .plans import *

logger.info("#### Utilities ####")
from .utils import *
from apstools.utils import *

# last line: ensure we have the console's logger
from .session_logs import logger
logger.info("#### Startup is complete. ####")
