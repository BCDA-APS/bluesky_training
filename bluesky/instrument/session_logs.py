"""
Configure logging for this session.

There are many _loggers_ to control the level of detailed logging for some
bluesky/ophyd internals.  The next table shows some of the many possible logger
names.  Configure the ``ACTIVATE_LOGGERS`` dictionary (below, where the keys are
logger names and the values are logging level, as shown) with any of these
names, or others which you may find useful:

==========================  ====================================================
logger name                 description
==========================  ====================================================
``bluesky``                 logger to which all bluesky log records propagate
``bluesky.emit_document``   when a Document is emitted. The log record does not contain the full content of the Document.
``bluesky.RE``              Records from a RunEngine. INFO-level notes state changes. DEBUG-level notes when each message from a plan is about to be processed and when a status object has completed.
``bluesky.RE.msg``          when each ``Msg`` is about to be processed.
``bluesky.RE.state``        when the RunEngine’s state changes.
``databroker``              logger to which all databroker log records propagate
``ophyd``                   logger to which all ophyd log records propagate
``ophyd.objects``           records from all devices and signals (that is, OphydObject subclasses)
``ophyd.control_layer``     requests issued to the underlying control layer (e.g. pyepics, caproto)
``ophyd.event_dispatcher``  regular summaries of the backlog of updates from the control layer that are being processed on background threads
==========================  ====================================================

References:

* https://blueskyproject.io/ophyd/user_v1/reference/logging.html#logger-names
* https://blueskyproject.io/bluesky/debugging.html#logger-names
"""

__all__ = [
    "logger",
]

import logging
import pathlib

from apstools.utils import file_log_handler
from apstools.utils import setup_IPython_console_logging
from apstools.utils import stream_log_handler

from . import iconfig

SESSION_NAME = "bluesky-session"
IPYTHON_LOGGER = "ipython_logger"

BYTE = 1
kB = 1024 * BYTE
MB = 1024 * kB

CHOICES = dict(
    LOG_PATH=None,
    MAX_BYTES=1 * MB,
    NUMBER_OF_PREVIOUS_BACKUPS=9,
)
CHOICES.update(iconfig.get("LOGGING", {}))
if CHOICES["LOG_PATH"] is not None:
    CHOICES["LOG_PATH"] = pathlib.Path(CHOICES["LOG_PATH"])

# see the table above for details about this dictionary
ACTIVATE_LOGGERS = {
    # "bluesky": "DEBUG",
    # "bluesky.emit_document": "DEBUG",
    # "bluesky.RE.msg": "DEBUG",
    # "ophyd": "DEBUG",
    # "ophyd.control_layer": "DEBUG",
    # "ophyd.objects": "DEBUG",
    # "databroker": "DEBUG",
}


logger = logging.getLogger(SESSION_NAME)
logger.setLevel(logging.DEBUG)  # allow any log content at this level
logger.addHandler(stream_log_handler())  # terse log to the console
logger.addHandler(
    file_log_handler(  # verbose log to a file
        backupCount=CHOICES["NUMBER_OF_PREVIOUS_BACKUPS"],
        file_name_base=IPYTHON_LOGGER,
        log_path=CHOICES["LOG_PATH"],
        maxBytes=CHOICES["MAX_BYTES"],
    )
)
setup_IPython_console_logging(log_path=CHOICES["LOG_PATH"])

logger.info("#" * 60 + " startup")
logger.info("logging started")
logger.info(f"logging level = {logger.level}")

# log messages from the instrument package: '__package__'
_l = logging.getLogger(__package__)
_l.setLevel("DEBUG")
_l.addHandler(stream_log_handler())  # terse log to the console
_l.info(__file__)


for logger_name, level in ACTIVATE_LOGGERS.items():
    _l = logging.getLogger(logger_name)
    _l.setLevel(logging.DEBUG)  # allow any log content at this level
    _l.addHandler(
        file_log_handler(  # logger to a file
            backupCount=CHOICES["NUMBER_OF_PREVIOUS_BACKUPS"],
            file_name_base=logger_name,
            level=level,  # filter reporting to this level
            log_path=CHOICES["LOG_PATH"],
            maxBytes=CHOICES["MAX_BYTES"],
        )
    )
