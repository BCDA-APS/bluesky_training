"""
Configure matplotlib in interactive mode for IPython console
"""

__all__ = [
    "plt",
]

import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

import matplotlib.pyplot as plt

plt.ion()
