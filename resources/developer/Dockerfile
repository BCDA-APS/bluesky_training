FROM  ubuntu:latest
# FROM  prjemian/os_only-1.1
LABEL version="1.1.0" \
      maintainer="prjemian <prjemian@gmail.com>" \
      Description="source: https://github.com/prjemian/epics-docker/"
USER  root
WORKDIR /home
CMD ["/bin/bash"]

############################################################
# OS updates & additions

RUN \
    DEBIAN_FRONTEND=noninteractive apt-get update -y \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install gnupg less sudo unzip wget

############################################################
# MongoDB

RUN \
    wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add - \
    && echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
RUN \
    DEBIAN_FRONTEND=noninteractive apt-get update -y \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y mongodb-org

# not running systemd, need to do this SystemV way
ADD https://raw.githubusercontent.com/mongodb/mongo/master/debian/init.d /etc/init.d/mongod
RUN \
    chmod +x /etc/init.d/mongod \
    && service mongod start \
    && service mongod status


############################################################
# Miniconda Python

# COPY miniconda.sh /root
ADD http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh /root/miniconda.sh
RUN bash /root/miniconda.sh -b -p /opt/miniconda3
# source "/opt/miniconda3/etc/profile.d/conda.sh"
COPY environment.yml /opt
RUN \
    export PATH=${PATH}:/opt/miniconda3/bin \
    && . /opt/miniconda3/bin/activate \
    && conda env create -f /opt/environment.yml \
    && conda env list

############################################################
# generic IOC prefixes

ENV GP_IOC_PREFIX="gp:"
ENV AD_IOC_PREFIX="ad:"

############################################################
# user accounts

COPY \
    add2bash.rc \
    user_setup.sh \
    instrument.tar.gz \
    blueskyStarter.sh \
    class_data_examples.zip \
    /home/
WORKDIR /opt
RUN unzip /home/class_data_examples.zip
RUN cat /home/add2bash.rc >> /etc/skel/.bashrc
RUN \
    for u in test1 test2 test3 ; do \
        /usr/sbin/useradd -d /home/$u -m $u -p $u; \
        su -l -c /home/user_setup.sh - $u; \
    done

############################################################
# final

WORKDIR /home
RUN pwd && ls
