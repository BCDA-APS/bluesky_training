#!/bin/bash

# apply patches and software updates (2021-08-13)

echo "downloading latest training repo content from GitHub"
cd ~/training
git pull

echo "check that IOCs are running"
_n_ad=$(docker ps | grep "  iocad" | wc -l)
_n_gp=$(docker ps | grep "  iocgp" | wc -l)

if (( "${_n_ad}" < 1 || "${_n_gp}" < 1 )); then
    echo "starting IOCs"
    ~/bin/start_iocs.sh
else
    echo "running"
fi

echo "Fix the GUI starter scripts"
cd ~/bin
/bin/rm ./start_caQtDM_ad
ln -s /tmp/docker_ioc/iocad/iocSimDetector/start_caQtDM_adsim ./start_caQtDM_ad

/bin/rm ./start_caQtDM_gp
ln -s /tmp/docker_ioc/iocgp/xxx-R6-2/start_caQtDM_xxx ./start_caQtDM_gp

/bin/rm ./start_MEDM_gp
ln -s /tmp/docker_ioc/iocgp/xxx-R6-2/start_MEDM_xxx ./start_MEDM_gp
cd ~/
