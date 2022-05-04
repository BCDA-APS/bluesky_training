#!/bin/bash

# manage the bluesky queueserver

#--------------------
# change the program defaults here
CONDA_ENVIRONMENT=training_2022
DATABROKER_CATALOG=training
#--------------------

# activate conda environment

# In GitHub Actions workflow,
# $CONDA is an environment variable pointing to the
# root of the miniconda directory
if [ -z "${CONDA}" ] ; then
    CONDA=/APSshare/miniconda/x86_64
    if [ ! -d "${CONDA}" ]; then
        CONDA_BASE_DIR=/opt/miniconda3
    fi
fi
CONDA_BASE_DIR="${CONDA}/bin"

source "${CONDA_BASE_DIR}/activate" "${CONDA_ENVIRONMENT}"

SHELL_SCRIPT_NAME=${BASH_SOURCE:-${0}}
if [ -z "$STARTUP_DIR" ] ; then
    # If no startup dir is specified, use the directory with this script
    STARTUP_DIR=$(dirname "${SHELL_SCRIPT_NAME}")
fi

start-re-manager \
    --startup-dir "${STARTUP_DIR}" \
    --update-existing-plans-devices ENVIRONMENT_OPEN \
    --zmq-publish-console ON \
    --databroker-config "${DATABROKER_CATALOG}"
