#!/bin/bash

export CONDA_BIN=$(dirname "${CONDA_EXE}")
if [[ "${CONDA_BIN}" = "." ]]; then
  export CONDA_BIN=/APSshare/miniconda/x86_64/bin
fi
export CONDA_ACTIVATE="${CONDA_BIN}/activate"
# export CONDA_ENVIRONMENT=bluesky_2021_1
export CONDA_ENVIRONMENT=class_2021_03

export IPYTHON_PROFILE=bluesky
export IPYTHONDIR="${HOME}/.ipython-bluesky"

console_session () {
    export OPTIONS=""
    export OPTIONS="${OPTIONS} --profile=${IPYTHON_PROFILE}"
    export OPTIONS="${OPTIONS} --ipython-dir=${IPYTHONDIR}"
    export OPTIONS="${OPTIONS} --IPCompleter.use_jedi=False"
    export OPTIONS="${OPTIONS} --InteractiveShellApp.hide_initial_ns=False"

    source ${CONDA_ACTIVATE} ${CONDA_ENVIRONMENT}
    ipython ${OPTIONS}
}

lab_server () {
    export OPTIONS=""
    # export OPTIONS="${OPTIONS} --no-browser"
    export OPTIONS="${OPTIONS} --ip=${HOST}"

    source ${CONDA_ACTIVATE} ${CONDA_ENVIRONMENT}

    python -m ipykernel install --user --name "${CONDA_ENVIRONMENT}"
    jupyter-lab ${OPTIONS}
}

# start_iocs () {
#     # FIXME: needs path/to/script (if not in ~/bin)
#     iocStarter.sh
# }

usage () {
    echo $"Usage: $0 [lab | help]"
}

case $(echo "${1}" | tr '[:upper:]' '[:lower:]') in
  gui | jupyter | lab | notebook | server)  lab_server  ;;
  "" | console | ipython)  console_session  ;;
  # docker | ioc)  start_iocs  ;;
  help | usage)  usage  ;;
  *)
    usage
    exit 1
esac
