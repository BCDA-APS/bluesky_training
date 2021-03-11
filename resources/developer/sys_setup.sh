#!/bin/bash

# configure VM (ubuntu) OS for a classroom use
#
# run as root

############################################################
# OS updates & additions

# DEBIAN_FRONTEND=noninteractive apt-get update -y
# DEBIAN_FRONTEND=noninteractive apt-get upgrade -y

# DEBIAN_FRONTEND=noninteractive apt-get -y install \
#     gnupg less sudo unzip wget

############################################################
# Docker & EPICS IOCs

# docker already installed

url=https://raw.githubusercontent.com/prjemian/epics-docker/master
cd /opt
wget ${url}/n3_synApps/start_xxx.sh
wget ${url}/n4_areaDetector/start_adsim.sh
wget ${url}/n3_synApps/remove_container.sh
chmod +x start_xxx.sh start_adsim.sh remove_container.sh

############################################################
# MongoDB

# mongod already installed

# cd ${HOME}
# server_url=https://www.mongodb.org/static/pgp/server-4.4.asc
# repo_url=https://repo.mongodb.org/apt/ubuntu
# wget -qO - ${server_url} | sudo apt-key add - \
#     && echo "deb [ arch=amd64,arm64 ] ${repo_url} focal/mongodb-org/4.4 multiverse" \
#     | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
# DEBIAN_FRONTEND=noninteractive apt-get update -y
# DEBIAN_FRONTEND=noninteractive apt-get install -y mongodb-org

# # TODO: start the service, enable it to start on reboot
# # # not running systemd, need to do this SystemV way
# # ADD https://raw.githubusercontent.com/mongodb/mongo/master/debian/init.d /etc/init.d/mongod
# # RUN \
# #     chmod +x /etc/init.d/mongod \
# #     && service mongod start \
# #     && service mongod status

# systemctl start mongod
# systemctl enable mongod
# systemctl status mongod

############################################################
# Miniconda Python and Bluesky environment

url=http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
wget ${url}
bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3
# source "/opt/miniconda3/etc/profile.d/conda.sh"
cp environment.yml /opt
export PATH=${PATH}:/opt/miniconda3/bin
source /opt/miniconda3/bin/activate
conda env create -f /opt/environment.yml
conda env list

############################################################
# generic IOC prefixes

export GP_IOC_PREFIX="gp:"
export AD_IOC_PREFIX="ad:"

############################################################
# example data

repo_url=https://github.com/BCDA-APS/bluesky_instrument_training
cd ${HOME}
/bin/rm -rf bluesky_instrument_training  # for repeat runs
git clone ${repo_url}
pushd ${HOME}/bluesky_instrument_training/resources/developer
make instrument
cp \
    add2bash.rc \
    blueskyStarter.sh \
    class_data_examples.zip \
    instrument.tar.gz \
    user_setup.sh \
    /home/
/bin/rm -rf /opt/class_data_examples
cd /opt && unzip /home/class_data_examples.zip
popd

############################################################
# user accounts

cd /opt
cat > ./start_iocs.sh << EOF
#!/bin/bash
# start all class EPICS IOCs
#
EOF
chmod +x /opt/start_iocs.sh

USERS=
USERS+=" test7"
USERS+=" test8"
USERS+=" test9"

for u in ${USERS} ; do
    # /usr/sbin/useradd -d /home/$u -m $u -p $u;

    # run the setup script as the user
    su -l -c /home/user_setup.sh - ${u};

    ioc_starter="/opt/ioc_start_${u}.sh"
    cat > ${ioc_starter} << EOF
#!/bin/bash
# file: ${ioc_starter}
# purpose: (re)start all EPICS IOCs for user: ${u}

# NOTE: no trailing colon here
/opt/start_adsim.sh ad${u}
/opt/start_xxx.sh gp${u}
EOF
    chmod +x "${ioc_starter}"
    echo "${ioc_starter}" >> /opt/start_iocs.sh

done
