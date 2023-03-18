#!/bin/bash

# manage the bluesky queueserver

#--------------------
# change the program defaults here
# TODO: CONDA_ENVIRONMENT="${BLUESKY_CONDA_ENV:-training_2022}"
CONDA_ENVIRONMENT=training_2022
DATABROKER_CATALOG=training
#--------------------

# activate conda environment

# In GitHub Actions workflow,
# $CONDA is an environment variable pointing to the
# root of the miniconda directory
if [ "${CONDA}" == "" ] ; then
    CONDA=/APSshare/miniconda/x86_64
    if [ ! -d "${CONDA}" ]; then
        if [ "${CONDA_EXE}" != "" ]; then
            # CONDA_EXE is the conda exectuable
            CONDA=$(dirname $(dirname $(readlink -f "${CONDA_EXE}")))
        else
            # fallback
            CONDA=/opt/miniconda3
        fi
    fi
fi
CONDA_BASE_DIR="${CONDA}/bin"

# In GitHub Actions workflow,
# $ENV_NAME is an environment variable naming the conda environment to be used
if [ -z "${ENV_NAME}" ] ; then
    ENV_NAME="${CONDA_ENVIRONMENT}"
fi

# echo "Environment: $(env | sort)"

source "${CONDA_BASE_DIR}/activate" "${ENV_NAME}"

SHELL_SCRIPT_NAME=${BASH_SOURCE:-${0}}
if [ -z "$STARTUP_DIR" ] ; then
    # If no startup dir is specified, use the directory with this script
    STARTUP_DIR=$(dirname "${SHELL_SCRIPT_NAME}")
fi

start-re-manager \
    --startup-dir "${STARTUP_DIR}" \
    --update-existing-plans-devices ENVIRONMENT_OPEN \
    --zmq-publish-console ON \
    --keep-re
    # --databroker-config "${DATABROKER_CATALOG}"
