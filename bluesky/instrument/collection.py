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

from ._iconfig import iconfig
if iconfig.get("WRITE_SPEC_DATA_FILES", False):
    if specwriter is not None:
        RE.subscribe(specwriter.receiver)
        logger.info(f"writing to SPEC file: {specwriter.spec_filename}")
        logger.info("   >>>>   Using default SPEC file name   <<<<")
        logger.info("   file will be created when bluesky ends its next scan")
        logger.info("   to change SPEC file, use command:   newSpecFile('title')")

# last line: ensure we have the console's logger
from .session_logs import logger
logger.info("#### Startup is complete. ####")
