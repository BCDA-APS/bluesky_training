#!/bin/bash

# Start a bluesky session in IPython console (default) or Jupyter notebook GUI.

# Get the Python environment name.
# define fallback if BLUESKY_CONDA_ENV is not found
DEFAULT_ENV=bluesky_2023_3
export ENV_NAME="${BLUESKY_CONDA_ENV:-${DEFAULT_ENV}}"
export IPYTHON_PROFILE=bluesky
export IPYTHONDIR="${HOME}/.ipython-bluesky"


pick () {  # activate ENV_NAME (using conda) from given arg

    ARG="${1}"

    if [ "${ARG}" == "" ]; then
        return 1
    fi

    if [ -d "${ARG}" ]; then
        pick "${ARG}/bin/conda"

        if [ "${cmd_base}" != "" ]; then
            return 0
        fi
        return 1
    fi

    CMD=$(which ${ARG})  # as executable command
    if [ "${CMD}" == "" ]; then
        return 1
    fi

    if [ -x "${CMD}" ]; then
        match_env_name=$( \
            ${CMD} env list \
            | grep "^[ ]*${ENV_NAME} " \
            | awk '{print $1}' \
        )
        if [ "${match_env_name}" != "" ]; then
            # found the requested environment name
            cmd_base=$(basename "${CMD}")
            case "${cmd_base}" in
                conda)
                    source "$(dirname ${CMD})/activate" base
                    "${cmd_base}" activate "${ENV_NAME}"
                    return 0
                    ;;
                *)
                    return 1
                    ;;
            esac
        fi
    fi

    return 2
}


pick_environment_executable () {  # Activate the environment
    # Pick the first "hit"
    pick "/APSshare/miniconda/x86_64" \
    || pick "${HOME}" \
    || pick "conda" \
    || pick "/opt/miniconda3" \
    || pick "${HOME}/Apps/miniconda" \
    || pick "${HOME}/Apps/anaconda"

    echo "==> CONDA_PREFIX=${CONDA_PREFIX}"

    if [ "${cmd_base}" != "" ]; then
        echo "$(which python) -- $(python --version)"
        return 0
    fi

    echo "Could not activate environment: '${ENV_NAME}'"
    return 3
}


console_session () {
    export OPTIONS=""
    export OPTIONS="${OPTIONS} --profile=${IPYTHON_PROFILE}"
    export OPTIONS="${OPTIONS} --ipython-dir=${IPYTHONDIR}"
    export OPTIONS="${OPTIONS} --IPCompleter.use_jedi=False"
    export OPTIONS="${OPTIONS} --InteractiveShellApp.hide_initial_ns=False"

    pick_environment_executable

    ipython ${OPTIONS}
}

lab_server () {
    export OPTIONS=""
    # export OPTIONS="${OPTIONS} --no-browser"
    export OPTIONS="${OPTIONS} --ip=${HOST}"

    pick_environment_executable

    python -m ipykernel install --user --name "${ENV_NAME}"
    jupyter-lab ${OPTIONS}
}

usage () {
    echo $"Usage: $0 [console | lab | help]"
}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

case $(echo "${1}" | tr '[:upper:]' '[:lower:]') in
  lab) lab_server  ;;
  "" | console) console_session  ;;
  help) usage  ;;
  *) usage; exit 1
esac
