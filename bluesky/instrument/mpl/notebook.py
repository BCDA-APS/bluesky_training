"""
Configure matplotlib in interactive mode for Jupyter notebook
"""

__all__ = [
    "plt",
]

from IPython import get_ipython
import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

# %matplotlib notebook
_ipython = get_ipython()
if _ipython is not None:
    # _ipython.magic("matplotlib notebook")
    _ipython.magic("matplotlib inline")
import matplotlib.pyplot as plt

plt.ion()
