#!/bin/bash

# Start the bluesky queueserver.

#--------------------
# change the program defaults here
# CONDA: pre-defined in GitHub Actions workflow
export CONDA=${CONDA:-/APSshare/miniconda/x86_64}
export CONDA_ENVIRONMENT="${BLUESKY_CONDA_ENV:-training_2022}"
export DATABROKER_CATALOG=${DATABROKER_CATALOG:-training}
export QS_SERVER_HOST=$(hostname)  # or host (that passes $(hostname) test below)
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

# activate conda command, if needed
if [ ! -f "${CONDA_EXE}" ]; then
    CONDA_ROOTS="${CONDA}"  # In GitHub Actions workflow: (miniconda)
    CONDA_ROOTS+=" /APSshare/miniconda/x86_64"
    CONDA_ROOTS+=" /opt/miniconda3"
    for root in ${CONDA_ROOTS}; do
        if [ -d "${root}" ] && [ -f "${root}/etc/profile.d/conda.sh" ]; then
            # Found a match!
            source "${root}/etc/profile.d/conda.sh"
            break
        fi
    done
fi

# In GitHub Actions workflow,
# $ENV_NAME is an environment variable naming the conda environment to be used
if [ -z "${ENV_NAME}" ] ; then
    ENV_NAME="${CONDA_ENVIRONMENT}"
fi

# echo "conda env list = $(conda env list)"

conda activate "${ENV_NAME}"

# #--------------------
# echo "Environment: $(env | sort)"
# echo "------"
# echo "CONDA_ENVIRONMENT=${CONDA_ENVIRONMENT}"
# echo "CONDA=${CONDA}"
# echo "DATABROKER_CATALOG=${DATABROKER_CATALOG}"
# echo "QS_SERVER_HOST=${QS_SERVER_HOST}"
# echo "QS_UPDATE_PLANS_DEVICES=${QS_UPDATE_PLANS_DEVICES}"
# echo "QS_USER_GROUP_PERMISSIONS_FILE=${QS_USER_GROUP_PERMISSIONS_FILE}"
# echo "QS_USER_GROUP_PERMISSIONS_RELOAD=${QS_USER_GROUP_PERMISSIONS_RELOAD}"
# echo "REDIS_ADDR=${REDIS_ADDR}"
# echo "SHELL_SCRIPT_NAME=${SHELL_SCRIPT_NAME}"
# echo "STARTUP_DIR=${STARTUP_DIR}"
# #--------------------

# Start the bluesky queueserver (QS)
start-re-manager \
    --redis-addr "${REDIS_ADDR}" \
    --startup-dir "${STARTUP_DIR}" \
    --update-existing-plans-devices "${QS_UPDATE_PLANS_DEVICES}" \
    --user-group-permissions "${QS_USER_GROUP_PERMISSIONS_FILE}" \
    --user-group-permissions-reload "${QS_USER_GROUP_PERMISSIONS_RELOAD}" \
    --zmq-publish-console ON \
    --keep-re
