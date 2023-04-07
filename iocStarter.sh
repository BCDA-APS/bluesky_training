#!/bin/bash

# file: iocStarter.sh
# purpose: start EPICS training IOCs in docker containers

iocmgr.sh start GP gp
iocmgr.sh start ADSIM ad
