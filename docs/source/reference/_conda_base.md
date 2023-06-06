# Conda Base Environment

Review [Python Virtual Environments](../reference/_conda_environment.md) before continuing here.

Install the conda [base
environment](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-environments)
so that it is read-only to an account with standard privileges so that normal
users cannot install or modify the base environment by accident.  One way is to
install it with *elevated privileges* (with permissions to read & write in
directories which are read-only with regular permissions).

These steps are for those who will administer the base conda environment.

## Install Miniconda base environment

With _elevated privileges_, install
[Miniconda](https://docs.conda.io/en/latest/miniconda.html) as base conda
environment.  Note these instructions for [silent
installation](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html#install-linux-silent).

```bash
# pick the installer script
INSTALLER=Miniconda3-latest-Linux-x86_64.sh
# INSTALLER=Miniconda3-py310_23.3.1-0-Linux-x86_64.sh

# pick the installation location for your system
# INSTALL_DIR=/opt/miniconda3
INSTALL_DIR=/APSshare/miniconda/x86_64

# download the installer script
wget "https://repo.anaconda.com/miniconda/${INSTALLER}"

# install Miniconda
bash ${INSTALLER} -b -p "${INSTALL_DIR}"

# install libmamba, mamba, & micromamba
source "${INSTALL_DIR}/bin/activate"
conda update -y -n base conda
conda install -y -n base conda-libmamba-solver
# conda install -y -n base -c conda-forge mamba --solver=libmamba
conda install -y -n base -c conda-forge micromamba --solver=libmamba

# set some defaults (can override in local settings)
CONFIG_FILE="${INSTALL_DIR}/condarc"
echo "channels:" > "${CONFIG_FILE}"
echo "  - defaults" >> "${CONFIG_FILE}"
echo "  - conda-forge" >> "${CONFIG_FILE}"
echo "  - apsu" >> "${CONFIG_FILE}"
echo "  - aps-anl-tag" >> "${CONFIG_FILE}"
echo "channel_priority: flexible" >> "${CONFIG_FILE}"
echo "solver: libmamba" >> "${CONFIG_FILE}"
```
