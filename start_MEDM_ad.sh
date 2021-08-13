#!/bin/bash

# file: start_MEDM_ad.sh

export EPICS_DISPLAY_PATH=/tmp/docker_ioc/custom-synapps-6.2-ad-3.10/screens/adl/

medm -x -macro "P=ad:, R=cam1:" simDetector.adl &
