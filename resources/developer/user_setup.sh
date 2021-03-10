#!/bin/bash

# configure a new user account for the bluesky class
#
# run from root:  su -l -c /home/user_setup.sh - USERNAME

#   su -l -s /bin/bash test3

# _developer_commands = """

# # must ALWAYS start this in the container
# service mongod start
# service mongod status

# # "login" as user "test3"
# su -l -s /bin/bash test3

# # Are IOC prefixes defined?
# ! env | grep -i ioc

# import os
# os.environ.get("GP_IOC_PREFIX", "gp:")

# """

############################################################
# operating environment

. /opt/miniconda3/bin/activate class_2021_03

mkdir ~/bin

# prefixes for GP and AD IOCs
cat >> ~/.bash_aliases << EOF
#
# IOC prefixes
export GP_IOC_PREFIX="gp${USER}:"
export AD_IOC_PREFIX="ad${USER}:"

EOF
cat /home/add2bash.rc > ~/.bash_aliases

############################################################
# IPython

export IPYTHON_DIR=${HOME}/.ipython-bluesky

ipython profile create --ipython-dir=${IPYTHON_DIR} --profile=bluesky

env | sort > env.txt

cd ${IPYTHON_DIR}/profile_bluesky/startup
tar xzf /home/instrument.tar.gz

cat >> run_instrument.py << EOF
from instrument.collection import *
EOF

############################################################
# bash starter script

cp /home/blueskyStarter.sh ./
pushd ~/bin
ln -s ${IPYTHON_DIR}/profile_bluesky/startup/blueskyStarter.sh ./
popd

############################################################
# databroker configuration YAML file

mkdir -p ~/.local/share/intake
cat > ~/.local/share/intake/databroker_mongodb.yml << EOF
sources:
  class_2021_03:
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
