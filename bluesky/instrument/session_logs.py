"""
configure session logging
"""

__all__ = [
    "logger",
]

import logging
import pathlib
# NOTE: no need for stdlogpj now


SESSION_NAME = "bluesky-session"
IPYTHON_LOGGER = "ipython_logger"

BYTE = 1
kB = 1024 * BYTE
MB = 1024 * kB


# TODO: hoist to apstools.utils
def get_log_path():
    path = pathlib.Path().cwd() / ".logs"
    if not path.exists():
        path.mkdir()
    return path


# TODO: hoist to apstools.utils
def setup_IPython_console_logging():
    from IPython import get_ipython

    console_io_file = get_log_path() / "ipython_console.log"
    try:
        # start logging console to file
        # https://ipython.org/ipython-doc/3/interactive/magics.html#magic-logstart
        _ipython = get_ipython()
        if _ipython is not None:
            _ipython.magic(f"logstart -o -t {console_io_file} rotate")
        logger.info("Console logging: %s", console_io_file)
    except Exception:
        logger.exception("Could not setup console logging.")


# TODO: hoist to apstools.utils
def stream_log_handler():
    handler = logging.StreamHandler()

    # nice output format
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    formatter = logging.Formatter(
        (
            "%(levelname)-.1s"		# only first letter
            " %(asctime)s"
            " - "
            "%(message)s"
        ),
        datefmt="%a-%H:%M:%S"
    )
    formatter.default_msec_format = "%s.%03d"
    handler.setFormatter(formatter)
    handler.setLevel("INFO")  # TODO:

    return handler


# TODO: hoist to apstools.utils
def file_log_handler(
    logger_name,
    file_name_base=None,
    maxBytes=0,
    backupCount=0,
    log_path=None,
    level=None,
):
    """
    standard setup for logging

    PARAMETERS

    logger_name : str
        name of the the logger

    file_name_base : str
        Part of the name to store the log file.
        Full name is `f"<log_path>/{file_name_base}.log"`
        in present working directory.

    log_path : str
        Part of the name to store the log file.
        Full name is `f"<log_path>/{file_name_base}.log"`
        in present working directory.
        default: (the present working directory)/LOG_DIR_BASE

    level : int
        Threshold for reporting messages with this logger.
        Logging messages which are less severe than *level* will be ignored.
        default: 10 (logging.DEBUG)
        see: https://docs.python.org/3/library/logging.html#levels

    maxBytes : (optional) int
        Log file *rollover* begins whenever the current
        log file is nearly *maxBytes* in length.
        default: 0

    backupCount : (optional) int
        When *backupCount* is non-zero, the system will keep
        up to *backupCount* numbered log files (with added extensions
        `.1`, '.2`, ...).  The current log file always has no
        numbered extension.  The previous log file is the
        one with the lowest extension number.
        default: 0

    **Note**:  When either *maxBytes* or *backupCount* are zero,
    log file rollover never occurs, so you generally want to set
    *backupCount* to at least 1, and have a non-zero *maxBytes*.
    """
    from logging.handlers import RotatingFileHandler

    file_name_base = file_name_base or logger_name
    log_path = log_path or get_log_path()
    log_file = log_path / f"{file_name_base}.log"
    level = level or logging.DEBUG

    if maxBytes > 0 or backupCount > 0:
        handler = RotatingFileHandler(
            log_file, maxBytes=maxBytes, backupCount=backupCount)
    else:
        handler = logging.FileHandler(log_file)

    handler.setLevel(level)

    formatter = logging.Formatter(
        (
            "|%(asctime)s"
            "|%(levelname)s"
            "|%(process)d"
            "|%(name)s"
            "|%(module)s"
            "|%(lineno)d"
            "|%(threadName)s"
            "| - "
            "%(message)s"
        )
    )
    formatter.default_msec_format = "%s.%03d"
    handler.setFormatter(formatter)

    return handler


logger = logging.getLogger(SESSION_NAME)
logger.setLevel(logging.DEBUG)  # allow any log content at this level
logger.addHandler(stream_log_handler())  # terse log to the console
logger.addHandler(
    file_log_handler(  # verbose log to a file
        SESSION_NAME, IPYTHON_LOGGER, maxBytes=1 * MB, backupCount=9
    )
)
setup_IPython_console_logging()

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
            logger_name,
            logger_name,
            maxBytes=1 * MB,
            backupCount=9,
            level=level,  # filter reporting to this level
        )
    )
