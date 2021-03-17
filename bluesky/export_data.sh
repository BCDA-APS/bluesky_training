#!/bin/bash

# Export all data collected during Bluesky Case Studies course

CATALOG=class_2021_03
OUTPUT_DIR=./data_export
OPTIONS=
OPTIONS+=" --all"
OPTIONS+=" --copy-external"

LOG_FILE=./export_data.log

databroker-pack ${OPTIONS} ${CATALOG} ${OUTPUT_DIR} 2>&1 | tee ${LOG_FILE}

tar czf ./data_export.tar.gz ./data_export
/bin/rm -rf ./data_export
