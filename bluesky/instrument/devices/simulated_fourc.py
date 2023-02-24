"""
Simulated 4-circle diffractometer.
"""

__all__ = """
    sim4c
""".split()

import logging

logger = logging.getLogger(__name__)
logger.info(__file__)

import hkl

sim4c = hkl.SimulatedE4CV("", name="sim4c")
