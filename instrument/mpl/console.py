"""
Configure matplotlib in interactive mode for IPython console
"""

__all__ = [
    "plt",
]

from ..session_logs import *

logger.info(__file__)

import matplotlib.pyplot as plt

plt.ion()
