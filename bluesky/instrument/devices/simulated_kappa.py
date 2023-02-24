"""
Simulated kappa 4- & 6-circle diffractometers.
"""

__all__ = """
    simk4c
    simk6c
""".split()

import logging

logger = logging.getLogger(__name__)
logger.info(__file__)

import hkl

simk4c = hkl.SimulatedK4CV("", name="simk4c")
simk6c = hkl.SimulatedK6C("", name="simk6c")
