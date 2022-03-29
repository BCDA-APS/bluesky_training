#!/bin/bash

# manage the bluesky queueserver

#--------------------
# change the program defaults here
CONDA_ENVIRONMENT=bluesky_2022_2
DATABROKER_CATALOG=training
#--------------------

# activate conda environment

CONDA_BASE_DIR=/APSshare/miniconda/x86_64/bin
if [ ! -d "${CONDA_BASE_DIR}" ]; then
    CONDA_BASE_DIR=/opt/miniconda3/bin
fi
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
