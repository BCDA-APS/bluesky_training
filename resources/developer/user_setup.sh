#!/bin/bash

# configure a new user account for the bluesky class
#
# run from root:  su -l -c /home/user_setup.sh - USERNAME

#   su -l -s /bin/bash test3

############################################################
# operating environment

mkdir -p ~/bin

# prefixes for GP and AD IOCs
cat > ~/.bash_aliases << EOF
# user configuration of bash shell

export PATH="\${HOME}/bin:\${PATH}"
export PATH="\${PATH}:/opt/miniconda3/bin"

#
# IOC prefixes
export GP_IOC_PREFIX="gp${USER}:"
export AD_IOC_PREFIX="ad${USER}:"

# only listen to docker IOCs running on this workstation
# export DOCKER_IOC_BROADCAST_ADDRESS=172.17.255.255
export EPICS_CA_ADDR_LIST=172.17.255.255
export EPICS_CA_AUTO_ADDR_LIST=NO

EOF

source /opt/miniconda3/bin/activate
conda init

export GP_IOC_PREFIX="gp${USER}:"
export AD_IOC_PREFIX="ad${USER}:"

############################################################
# IPython

export IPYTHON_DIR=${HOME}/.ipython-bluesky

ipython profile create --ipython-dir=${IPYTHON_DIR} --profile=bluesky

env | sort > env.txt

cat > ${IPYTHON_DIR}/profile_bluesky/startup/run_instrument.py << EOF
import os
import sys
sys.path.append(os.path.join(os.environ["HOME"], "bluesky"))
from instrument.collection import *
EOF

############################################################
# create~/bluesky directory
cd ~
if [ -d "bluesky" ]; then 
    # move old dir out of the way
    TS=$(date -Iseconds | sed s+':'+''+g -)
    TAR_NAME="bluesky-${TS}.tar.gz"
    echo "archive existing 'bluesky' directory to ${TAR_NAME}"
    tar czf ${TAR_NAME} ./bluesky
    /bin/rm -rf ./bluesky
fi
mkdir ~/installer
cd ~/installer
tar xzf /home/course_content.tar.gz 
cd bluesky_instrument_training
mv ./bluesky ~/
mv *.ipynb ~/
cd ~
/bin/rm -rf ./installer
chmod +x ~/bluesky/blueskyStarter.sh

############################################################
# bash starter script

pushd ~/bin
/bin/rm -f ./blueskyStarter.sh
ln -s ~/bluesky/blueskyStarter.sh ./
popd

############################################################
# databroker configuration YAML file

mkdir -p ~/.local/share/intake
cat > ~/.local/share/intake/training.yml << EOF
sources:
  training:
    args:
      asset_registry_db: mongodb://localhost:27017/${USER}-bluesky
      metadatastore_db: mongodb://localhost:27017/${USER}-bluesky
    driver: bluesky-mongo-normalized-catalog
EOF

############################################################
# previously-collected data for analysis

cd ~
/bin/rm -f ~/.local/share/intake/databroker_unpack_class_data_examples.yml
databroker-unpack inplace "/opt/class_data_examples" class_data_examples
