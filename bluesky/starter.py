"""
Load devices and plans for bluesky queueserver.

How to start the queueserver process::

    DATABROKER_CATALOG=training
    STARTUP_DIR=$(pwd)

    start-re-manager \
        --startup-dir "${STARTUP_DIR}" \
        --update-existing-plans-devices ENVIRONMENT_OPEN \
        --zmq-publish-console ON \
        --databroker-config "${DATABROKER_CATALOG}"

"""

import pathlib, sys

sys.path.append(
    str(pathlib.Path(__file__).absolute().parent)
)

from instrument.queueserver import *
