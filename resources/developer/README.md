# Steps to setup the VM for Bluesky and EPICS

- [Steps to setup the VM for Bluesky and EPICS](#steps-to-setup-the-vm-for-bluesky-and-epics)
  - [Infrastructure: `sys_setup.sh`](#infrastructure-sys_setupsh)
    - [Get the installation scripts](#get-the-installation-scripts)
    - [Install the infrastructure](#install-the-infrastructure)
    - [update the `conda` tool](#update-the-conda-tool)
    - [Get the EPICS docker images](#get-the-epics-docker-images)
  - [Configure each user account](#configure-each-user-account)

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
export INSTALLER_PATH=${HOME}/bluesky_instrument_training/resources/developer
cd ~
tar czf ~/course_content.tar.gz ./bluesky_instrument_training
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

### update the `conda` tool

Sometimes, the Miniconda installer provides an older `conda` tool.  If
suggested, update `conda`:

```sh
sudo su
source /opt/miniconda3/bin/activate
conda update conda
exit
```

### Get the EPICS docker images

For the first time, download the docker images for the two types of
EPICS IOC we'll need (we need one of each for every user).  It takes
some time to download the images for the first time, so do that now.

```sh
# confirm which containers are running
docker ps

# start a general purpose EPICS IOC with prefix gp
/opt/start_xxx.sh gp

# start a simulated area detector EPICS IOC with prefix ad
/opt/start_adsim.sh ad

# confirm which containers are running
docker ps

# stop the containers
/opt/remove_container.sh iocgp
/opt/remove_container.sh iocad

# confirm which containers are running
docker ps
```

## Configure each user account

Provision each user account with notebooks and access to the Python software
stack.  Create an IOC starter shell script for each account and add it to the
script to (re)start IOCs for all configured accounts.

Must be done from root account.

```sh
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
# USERS+=" dutc"
# USERS+=" jade"
# USERS+=" jemian"
# USERS+=" arun"
# USERS+=" cypark"
# USERS+=" hrubiak"
# USERS+=" jssmith"
# USERS+=" kenesei"
# USERS+=" kmpeters"
# USERS+=" lrebuffi"
# USERS+=" makarov"
# USERS+=" strempfer"
# USERS+=" wenqianxu"
# USERS+=" audit0"
# USERS+=" audit1"
# USERS+=" audit2"
# USERS+=" audit3"
# USERS+=" audit4"
# USERS+=" audit5"
# USERS+=" audit6"
# USERS+=" audit7"
# USERS+=" audit8"
# USERS+=" audit9"
# USERS+=" prep0"
# USERS+=" prep1"
# USERS+=" prep2"
# USERS+=" prep3"
# USERS+=" prep4"
# USERS+=" prep5"
# USERS+=" prep6"
# USERS+=" prep7"
# USERS+=" prep8"
# USERS+=" prep9"
# USERS+=" student0"
# USERS+=" student1"
# USERS+=" student2"
# USERS+=" student3"
# USERS+=" student4"
# USERS+=" student5"
# USERS+=" student6"
# USERS+=" student7"
# USERS+=" student8"
# USERS+=" student9"
USERS+=" test0"
USERS+=" test1"
USERS+=" test2"
USERS+=" test3"
# USERS+=" test4"
# USERS+=" test5"
# USERS+=" test6"
# USERS+=" test7"
# USERS+=" test8"
# USERS+=" test9"

for u in ${USERS} ; do
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
