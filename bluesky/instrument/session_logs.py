"""
configure session logging
"""

__all__ = [
    "logger",
]

import logging


try:
    from IPython import get_ipython
    import pathlib
    import stdlogpj  # pip install stdlogpj

    SESSION_NAME = "bluesky-session"
    IPYTHON_LOGGER = "ipython_logger"

    BYTE = 1
    kB = 1024 * BYTE
    MB = 1024 * kB

    _log_path = pathlib.Path().cwd() / ".logs"
    if not _log_path.exists():
        _log_path.mkdir()
    CONSOLE_IO_FILE = _log_path / "ipython_console.log"

    # start logging console to file
    # https://ipython.org/ipython-doc/3/interactive/magics.html#magic-logstart
    _ipython = get_ipython()
    if _ipython is not None:
        _ipython.magic(f"logstart -o -t {CONSOLE_IO_FILE} rotate")
    # %logstart -o -t .ipython_console.log "rotate"

    logger = stdlogpj.standard_logging_setup(SESSION_NAME, IPYTHON_LOGGER, maxBytes=1 * MB, backupCount=9)

except Exception as exc:
    logger = logging.basicConfig(level=logging.INFO)
    logger.warning(
        "Use standard logging (could not setup custom logging: %s", exc
    )

# TODO: setting for iconfig?
logger.setLevel(logging.DEBUG)

logger.info("#" * 60 + " startup")
logger.info("logging started")
logger.info(f"logging level = {logger.level}")
