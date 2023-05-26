#!/bin/bash

# Start the bluesky queueserver.

#--------------------
# change the program defaults here
export CONDA_ENVIRONMENT="${BLUESKY_CONDA_ENV:-training_2022}"
export DATABROKER_CATALOG=${DATABROKER_CATALOG:-training}
export QS_SERVER_HOST=$(hostname)
export QS_UPDATE_PLANS_DEVICES=ENVIRONMENT_OPEN
export QS_USER_GROUP_PERMISSIONS_FILE="./user_group_permissions.yaml"
export QS_USER_GROUP_PERMISSIONS_RELOAD=ON_STARTUP

# REDIS_ADDR is __always__ localhost.
# Override if it is not, but you may encounter access issues.  YOYO.
export REDIS_ADDR=localhost
#--------------------

# QS and redis must be on the same workstation
if [ "$(hostname)" != "${QS_SERVER_HOST}" ]; then
    echo "Must run queueserver on ${QS_SERVER_HOST}.  This is $(hostname)"
    exit 1
fi

SHELL_SCRIPT_NAME=${BASH_SOURCE:-${0}}
if [ -z "$STARTUP_DIR" ] ; then
    # If no startup dir is specified, use the directory with this script
    export STARTUP_DIR=$(dirname "${SHELL_SCRIPT_NAME}")
fi

# activate conda environment

# $CONDA: root directory of miniconda or anaconda
# In GitHub Actions workflow, $CONDA is defined (miniconda).
# Otherwise, we have to find the conda root.
if [ "${CONDA}" == "" ] ; then
    CONDA=/APSshare/miniconda/x86_64
    if [ ! -d "${CONDA}" ]; then
        if [ "${CONDA_EXE}" != "" ]; then
            # CONDA_EXE is the conda executable
            CONDA=$(dirname $(dirname $(readlink -f "${CONDA_EXE}")))
        else
            # fallback
            CONDA=/opt/miniconda3
        fi
    fi
fi
CONDA_BASE_BIN="${CONDA}/bin"

# In GitHub Actions workflow,
# $ENV_NAME is an environment variable naming the conda environment to be used
if [ -z "${ENV_NAME}" ] ; then
    ENV_NAME="${CONDA_ENVIRONMENT}"
fi

# echo "Environment: $(env | sort)"

source "${CONDA_BASE_BIN}/activate" "${ENV_NAME}"

#--------------------
echo "CONDA_ENVIRONMENT=${CONDA_ENVIRONMENT}"
echo "CONDA=${CONDA}"
echo "DATABROKER_CATALOG=${DATABROKER_CATALOG}"
echo "QS_SERVER_HOST=${QS_SERVER_HOST}"
echo "QS_UPDATE_PLANS_DEVICES=${QS_UPDATE_PLANS_DEVICES}"
echo "QS_USER_GROUP_PERMISSIONS_FILE=${QS_USER_GROUP_PERMISSIONS_FILE}"
echo "QS_USER_GROUP_PERMISSIONS_RELOAD=${QS_USER_GROUP_PERMISSIONS_RELOAD}"
echo "REDIS_ADDR=${REDIS_ADDR}"
echo "SHELL_SCRIPT_NAME=${SHELL_SCRIPT_NAME}"
echo "STARTUP_DIR=${STARTUP_DIR}"
#--------------------

start-re-manager \
    --redis-addr "${REDIS_ADDR}" \
    --startup-dir "${STARTUP_DIR}" \
    --update-existing-plans-devices "${QS_UPDATE_PLANS_DEVICES}" \
    --user-group-permissions "${QS_USER_GROUP_PERMISSIONS_FILE}" \
    --user-group-permissions-reload "${QS_USER_GROUP_PERMISSIONS_RELOAD}" \
    --zmq-publish-console ON \
    --keep-re
