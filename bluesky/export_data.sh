#!/bin/bash

# Export all data collected during Bluesky Case Studies course

CATALOG=class_2021_03
OUTPUT_DIR=./${CATALOG}
OPTIONS=
OPTIONS+=" --all"
OPTIONS+=" --copy-external"

LOG_FILE=./${CATALOG}.log

databroker-pack ${OPTIONS} ${CATALOG} ${OUTPUT_DIR} 2>&1 | tee ${LOG_FILE}

tar czf ./${CATALOG}.tar.gz ./${CATALOG}
/bin/rm -rf ./${CATALOG}
