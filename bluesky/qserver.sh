#!/bin/bash

# manage the bluesky queueserver process in a screen session

#--------------------
# change the program defaults here
DATABROKER_CATALOG=training
DEFAULT_SESSION_NAME="bluesky_queueserver-${DATABROKER_CATALOG}"
#--------------------

SHELL_SCRIPT_NAME=${BASH_SOURCE:-${0}}
if [ -z "$STARTUP_DIR" ] ; then
    # If no startup dir is specified, use the directory with this script
    STARTUP_DIR=$(dirname "${SHELL_SCRIPT_NAME}")
fi

SELECTION=${1:-usage}
SESSION_NAME=${2:-"${DEFAULT_SESSION_NAME}"}

PROCESS=run_qstarter_py.sh
STARTUP_COMMAND="${STARTUP_DIR}/${PROCESS}"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# echo "SESSION_NAME = ${SESSION_NAME}"
# echo "SHELL_SCRIPT_NAME = ${SHELL_SCRIPT_NAME}"
# echo "STARTUP_COMMAND = ${STARTUP_COMMAND}"
# echo "STARTUP_DIR = ${STARTUP_DIR}"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

function checkpid() {
    MY_UID=$(id -u)
    # # The '\$' is needed in the pgrep pattern to select vm7, but not vm7.sh
    MY_PID=$(pgrep "${PROCESS}"\$ -u "${MY_UID}")
    # #!echo "MY_PID=${MY_PID}"

    if [ "${MY_PID}" != "" ] ; then
        # Assume the process is down until proven otherwise
        PROCESS_DOWN=1
        SCREEN_PID=""

        # At least one instance of the process is running;
        # Find the binary that is associated with this process
        for pid in ${MY_PID}; do
            # compare directories
            BIN_CWD=$(readlink "/proc/${pid}/cwd")
            START_CWD=$(readlink -f "${STARTUP_DIR}")

            if [ "$BIN_CWD" = "$START_CWD" ] ; then
                # The process is running with PID=$pid from $STARTUP_DIR
                P_PID=$(ps -p "${pid}" -o ppid=)
                # strip leading (and trailing) whitespace
                arr=($P_PID)
                P_PID=${arr[0]}
                SCREEN_SESSION="${P_PID}.${SESSION_NAME}"
                SCREEN_MATCH=$(screen -ls "${SCREEN_SESSION}" | grep "${SESSION_NAME}")
                if [ "${SCREEN_MATCH}" != "" ] ; then
                    # process is running in screen
                    PROCESS_DOWN=0
                    MY_PID=${pid}
                    SCREEN_PID=${P_PID}
                    break
                fi
            fi
        done
    else
        # process is not running
        PROCESS_DOWN=1
    fi

    return ${PROCESS_DOWN}
}

function checkup () {
    if ! checkpid; then
        restart
    fi
}

function console () {
    if checkpid; then
        echo "Connecting to ${SCREEN_SESSION}'s screen session"
        # The -r flag will only connect if no one is attached to the session
        #!screen -r "${SESSION_NAME}"
        # The -x flag will connect even if someone is attached to the session
        screen -x "${SCREEN_SESSION}"
    else
        echo "${SCREEN_NAME} is not running"
    fi
}

function exit_if_running() {
    # ensure that multiple, simultaneous processes are not started by this user ID
    MY_UID=$(id -u)
    MY_PID=$(pgrep "${SESSION_NAME}"\$ -u "${MY_UID}")

    if [ "" != "${MY_PID}" ] ; then
        echo "${SESSION_NAME} is already running (PID=${MY_PID}), won't start a new one"
        exit 1
    fi
}

function restart() {
    stop
    start
}

function run_process() {
    # only use this for diagnostic purposes
    exit_if_running
    ${STARTUP_COMMAND}
}

function screenpid() {
    if [ -z "${SCREEN_PID}" ] ; then
        echo
    else
        echo " in a screen session (pid=${SCREEN_PID})"
    fi
}

function start() {
    if checkpid; then
        echo -n "${SCREEN_SESSION} is already running (pid=${MY_PID})"
        screenpid
    else
        echo "Starting ${SESSION_NAME}"
        cd "${STARTUP_DIR}"
        # Run SESSION_NAME inside a screen session
        CMD="screen -dm -S ${SESSION_NAME} -h 5000 ${STARTUP_COMMAND}"
        ${CMD}
    fi
}

function status() {
    if checkpid; then
        echo -n "${SCREEN_SESSION} is running (pid=${MY_PID})"
        screenpid
    else
        echo "${SESSION_NAME} is not running"
    fi
}

function stop() {
    if checkpid; then
        echo "Stopping ${SCREEN_SESSION} (pid=${MY_PID})"
        kill "${MY_PID}"
    else
        echo "${SESSION_NAME} is not running"
    fi
}

function usage() {
    echo "Usage: $(basename "${SHELL_SCRIPT_NAME}") {start|stop|restart|status|checkup|console|run} [NAME]"
    echo ""
    echo "    COMMANDS"
    echo "        console   attach to process console if process is running in screen"
    echo "        checkup   check that process is running, restart if not"
    echo "        restart   restart process"
    echo "        run       run process in console (not screen)"
    echo "        start     start process"
    echo "        status    report if process is running"
    echo "        stop      stop process"
    echo ""
    echo "    OPTIONAL TERMS"
    echo "        NAME      name of process (default: ${DEFAULT_SESSION_NAME})"
}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

case ${SELECTION} in
    start) start ;;
    stop | kill) stop ;;
    restart) restart ;;
    status) status ;;
    checkup) checkup ;;
    console) console ;;
    run) run_process ;;
    *) usage ;;
esac

# -----------------------------------------------------------------------------
# :author:    Pete R. Jemian
# :email:     jemian@anl.gov
# :copyright: (c) 2017-2022, UChicago Argonne, LLC
#
# Distributed under the terms of the Creative Commons Attribution 4.0 International Public License.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------
