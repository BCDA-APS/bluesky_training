# Steps to setup the VM for Bluesky and EPICS

- [Steps to setup the VM for Bluesky and EPICS](#steps-to-setup-the-vm-for-bluesky-and-epics)
  - [Infrastructure: `sys_setup.sh`](#infrastructure-sys_setupsh)
    - [Get the installation scripts](#get-the-installation-scripts)
    - [Install the infrastructure](#install-the-infrastructure)

## Infrastructure: `sys_setup.sh`

All infrastructure tools install into directory `/opt`.

### Get the installation scripts

```sh
cd ~
git clone https://github.com/BCDA-APS/bluesky_instrument_training
cd bluesky_instrument_training/
git checkout 4-refactor-one-folder 
```

### Install the infrastructure

Gather various resources to simplify infrastructure installation.

```sh
pushd resources/developer/
export INSTALLER_PATH=$(pwd)
make instrument >> infrastructure_setup-$(date -Idate).log
```

Installs (to `/opt`):

- docker shell scripts to start and remove EPICS containers
- the Anaconda python installation (the base environment)
- the Bluesky framework in the base environment
- the example data files
- the (bluesky) instrument package
- per-user setup scripts

```sh
sudo su
bash ./sys_setup.sh 2>&1 >> infrastructure_setup-$(date -Idate).log
exit
popd
```

---------------

Install the example data files, the (bluesky) instrument package, and
per-user setup scripts

```sh
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
```
