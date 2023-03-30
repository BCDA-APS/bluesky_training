"""
2D slits, 4 individual motorized blades.

.. note:: The motor assignments should already be set in the IOC
    as part of the 2slit.db database.

Coordinates of ``Optics2Slit2D_HV`` (viewing from detector towards source)::

        v.xp
    h.xn    h.xp
        v.xn

* https://github.com/epics-modules/optics/blob/master/opticsApp/Db/2slit.db
* https://bcda-aps.github.io/apstools/latest/api/synApps/_db_2slit.html#apstools.synApps.db_2slit.Optics2Slit2D_InbOutBotTop
* https://github.com/prjemian/epics-docker/tree/main/v1.1/n5_custom_synApps#motor-assignments

=====   ==========  ==================
motor	position    assignment
=====   ==========  ==================
m41	    v.xp        Slit1V:mXp
m42	    v.xn        Slit1V:mXn
m43	    h.xp        Slit1H:mXp
m44	    h.xn        Slit1H:mXn
=====   ==========  ==================

.. warning:  The training IOC is misconfigured (in docker)
   to use m5 & m6 instead of m43 & m44.
"""

__all__ = """
    slit1
""".split()

import logging

from apstools.synApps import Optics2Slit2D_HV
from apstools.synApps import Optics2Slit2D_InbOutBotTop

from .. import iconfig

logger = logging.getLogger(__name__)
logger.info(__file__)

IOC = iconfig.get("GP_IOC_PREFIX", "gp:")

# Choose between alternate interfaces to the same controls:

# Optics2Slit2D_HV() has a hierarchical structure
# slit1
#     h
#         xp, xn, size, center
#     v
#         xp, xn, size, center

# Optics2Slit2D_InbOutBotTop() has a flat structure
# slit1
#     top
#     bot
#     out
#     inb
#     hsize
#     hcenter
#     vsize
#     vcenter

slit1 = Optics2Slit2D_HV(f"{IOC}Slit1", name="slit1")
