"""
configure session logging
"""

__all__ = [
    "logger",
]

import logging

from apstools.utils import file_log_handler
from apstools.utils import setup_IPython_console_logging
from apstools.utils import stream_log_handler

SESSION_NAME = "bluesky-session"
IPYTHON_LOGGER = "ipython_logger"

BYTE = 1
kB = 1024 * BYTE
MB = 1024 * kB


logger = logging.getLogger(SESSION_NAME)
logger.setLevel(logging.DEBUG)  # allow any log content at this level
logger.addHandler(stream_log_handler())  # terse log to the console
logger.addHandler(
    file_log_handler(  # verbose log to a file
        file_name_base=IPYTHON_LOGGER,
        maxBytes=1 * MB,
        backupCount=9,
    )
)
setup_IPython_console_logging()  # TODO: upstream needs log_path= kwarg

logger.info("#" * 60 + " startup")
logger.info("logging started")
logger.info(f"logging level = {logger.level}")

# log messages from the instrument package: '__package__'
_l = logging.getLogger(__package__)
_l.setLevel("DEBUG")
_l.addHandler(stream_log_handler())  # terse log to the console
_l.info(__file__)

# Setup logging for some bluesky/ophyd internals
# https://blueskyproject.io/ophyd/user_v1/reference/logging.html#logger-names
# https://blueskyproject.io/bluesky/debugging.html#logger-names
# - 'bluesky' — the logger to which all bluesky log records propagate
# - 'bluesky.emit_document' — A log record is emitted whenever a Document is emitted. The log record does not contain the full content of the Document.
# - 'bluesky.RE' — Records from a RunEngine. INFO-level notes state changes. DEBUG-level notes when each message from a plan is about to be processed and when a status object has completed.
# - 'bluesky.RE.msg — A log record is emitted when each Msg is about to be processed.
# - 'bluesky.RE.state — A log record is emitted when the RunEngine’s state changes.
# - 'ophyd' — the logger to which all ophyd log records propagate
# - 'ophyd.objects' — logs records from all devices and signals (that is, OphydObject subclasses)
# - 'ophyd.control_layer' — logs requests issued to the underlying control layer (e.g. pyepics, caproto)
# - 'ophyd.event_dispatcher' — issues regular summaries of the backlog of updates from the control layer that are being processed on background threads

log_these_names = {
    # "bluesky": "DEBUG",
    # "bluesky.emit_document": "DEBUG",
    # "bluesky.RE.msg": "DEBUG",
    # "ophyd": "DEBUG",
    "ophyd.control_layer": "DEBUG",
    # "ophyd.objects": "DEBUG",
    # "databroker": "DEBUG",
}
for logger_name, level in log_these_names.items():
    _l = logging.getLogger(logger_name)
    _l.setLevel(logging.DEBUG)  # allow any log content at this level
    _l.addHandler(
        file_log_handler(  # logger to a file
            file_name_base=logger_name,
            maxBytes=1 * MB,
            backupCount=9,
            level=level,  # filter reporting to this level
        )
    )
