"""
Hello, World! demo for bluesky-queueserver testing.

EXAMPLE::

    # Load this code in IPython or Jupyter notebook:
    %run -i user/quick_hello.py

    # Run the plan with the RunEngine:
    RE(hello_world())
"""

__all__ = """
    hello_world
""".split()

import logging

logger = logging.getLogger(__name__)
logger.info(__file__)

from ophyd import Component, Device, Signal

from bluesky import plans as bp

print("Loading 'Hello, World!' example.")


class HelloDevice(Device):
    """Simple ophyd device to provide Hello, World! capability."""

    number = Component(Signal, value=0, kind="hinted")
    text = Component(Signal, value="", kind="normal")


hello_device = HelloDevice(name="hello")
hello_device.stage_sigs["number"] = 1
hello_device.stage_sigs["text"] = "Hello, World!"
hello_device.number.name = hello_device.name


def hello_world():
    """Simple bluesky plan for demonstrating Hello, World!."""
    yield from bp.count([hello_device], md=dict(title="test QS"))
