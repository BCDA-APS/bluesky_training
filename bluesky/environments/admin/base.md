# Base environment

Install the base conda environment so that it is read-only to an account with
standard privileges so that normal users cannot install or modify the base
environment by accident.  One way is to install it with elevated privileges.

This steps are for those who will administer the base conda environment.

## Install Miniconda base environment

With _elevated privileges_, install
Miniconda as base conda environment.  Note these instructions for
[silent
installation](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html#install-linux-silent).

```bash
# download the latest installer
wget https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-Linux-x86_64.sh

# pick the installation location for your system
# export INSTALL_DIR=/opt/miniconda
export INSTALL_DIR=/APSshare/miniconda/x86_64

# run the silent installer
bash Miniconda3-py310_23.1.0-1-Linux-x86_64.sh -b -p "${INSTALL_DIR}"

# set some defaults (can override in local settings)
export CONFIG_FILE="${INSTALL_DIR}/condarc"
echo "channels:" > "${CONFIG_FILE}"
echo "  - defaults" >> "${CONFIG_FILE}"
echo "  - conda-forge" >> "${CONFIG_FILE}"
echo "  - apsu" >> "${CONFIG_FILE}"
echo "  - aps-anl-tag" >> "${CONFIG_FILE}"
echo "channel_priority: flexible" >> "${CONFIG_FILE}"
echo "solver: libmamba" >> "${CONFIG_FILE}"

# install libmamba, mamba, & micromamba
source "${INSTALL_DIR}/bin/activate"
conda install -y -n base conda-libmamba-solver mamba micromamba
```
