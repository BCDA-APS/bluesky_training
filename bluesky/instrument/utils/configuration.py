"""
Provide information from the configuration.yml file.

Example YAML configuration file::

    # simple key:value pairs

    ADSIM_IOC_PREFIX: "ad:"
    GP_IOC_PREFIX: "gp:"
    catalog: training
"""

__all__ = ["configuration_dict"]

from ..session_logs import logger

logger.info(__file__)

import pathlib
import yaml


PATH = pathlib.Path(__file__).absolute().parent.parent
CONFIG_FILE = PATH / "configuration.yml"

configuration_dict = yaml.load(open(CONFIG_FILE, "r").read(), yaml.Loader)
