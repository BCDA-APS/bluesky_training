#!/bin/bash

# configure VM (ubuntu) OS for a classroom use
#
# run as root from directory:
#  bluesky_instrument_training/resources/developer ~/bluesky_instrument_training

############################################################
# Install conda environment (needed later)

echo "Installing conda environment file for Bluesky: /opt/environment.yml"
cp ../../environment.yml /opt

############################################################
# Docker & EPICS IOCs

# pre-requisite: docker already installed
# install the starter scripts for the Docker containers

url=https://raw.githubusercontent.com/prjemian/epics-docker/master/v1.1
pushd /opt
wget ${url}/n5_custom_synApps/start_xxx.sh
wget ${url}/n5_custom_synApps/remove_container.sh
wget ${url}/n6_custom_areaDetector/start_adsim.sh
chmod +x start_xxx.sh start_adsim.sh remove_container.sh

# find the remove_container.sh script
sed -i s:'remove_container.sh':'/opt/remove_container.sh':g ./start_xxx.sh
sed -i s:'remove_container.sh':'/opt/remove_container.sh':g ./start_adsim.sh

# remove unnecessary lines
sed -i s:'echo -n "removing':'# echo -n "removing':g ./remove_container.sh
sed -i s:'docker rm':'# docker rm':g ./remove_container.sh

############################################################
# MongoDB

# pre-requisite: mongod already installed

############################################################
# Miniconda Python and Bluesky environment

url=http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
wget ${url}
bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3
# source "/opt/miniconda3/etc/profile.d/conda.sh"
export PATH=${PATH}:/opt/miniconda3/bin
source /opt/miniconda3/bin/activate
# add Bluesky framework to base environment
conda env update -n base -f /opt/environment.yml
pip install dotenv
conda env list

############################################################
# instrument package and data examples

popd
cp \
    /home/jemian/course_content.tar.gz \
    /home/jemian/bluesky_instrument_training/resources/example-data/class_data_examples.zip \
    user_setup.sh \
    /home/
/bin/rm -rf /opt/class_data_examples
cd /opt && unzip /home/class_data_examples.zip
