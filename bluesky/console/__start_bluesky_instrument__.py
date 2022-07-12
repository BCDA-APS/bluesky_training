"""
start bluesky in IPython console session
"""

# start a Bluesky data collection console session
import pathlib, sys

# add the "bluesky/" directory to the system path
__BLUESKY_IN_HOME_DIRECTORY__ = False
# first, identify the parent directory
if __BLUESKY_IN_HOME_DIRECTORY__:
    BLUESKY_DIRECTORY = pathlib.Path.home()
else:
    # <training repository directory>
    BLUESKY_DIRECTORY = pathlib.Path(__file__).absolute().parent.parent.parent
# next, name the "bluesky" subdirectory
BLUESKY_DIRECTORY = BLUESKY_DIRECTORY / "bluesky"
if not BLUESKY_DIRECTORY.exists():
    raise FileNotFoundError(
        f"Cannot find bluesky directory: {BLUESKY_DIRECTORY}"
    )
# put bluesky directory on the import path
sys.path.append(str(BLUESKY_DIRECTORY))

# terse error dumps (Exception tracebacks)
get_ipython().run_line_magic('xmode', 'Minimal')

from instrument.collection import *
