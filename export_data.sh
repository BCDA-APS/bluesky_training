#!/bin/bash

# Export all data collected during Bluesky Case Studies course

CATALOG=training
OUTPUT_DIR=./${CATALOG}
OPTIONS=
OPTIONS+=" --all"
OPTIONS+=" --copy-external"

LOG_FILE=./${CATALOG}.log

databroker-pack ${OPTIONS} ${CATALOG} ${OUTPUT_DIR} 2>&1 | tee ${LOG_FILE}

# TODO: make it a .zip file instead, match the *unpack* notebook example
tar czf ./${CATALOG}.tar.gz ./${CATALOG}
/bin/rm -rf ./${CATALOG}
