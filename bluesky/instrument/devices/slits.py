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
m5 	    h.xp        Slit1H:mXp
m6 	    h.xn        Slit1H:mXn
=====   ==========  ==================

.. warning:  Some motor assignments in the training IOC are misconfigured.
   The misconfiguration happens in the IOC configuration in the
   ``prjemian/custom-synapps-6.2`` docker image.
   (https://hub.docker.com/r/prjemian/custom-synapps-6.2)

   ==========   ==========  ============
   in docker    should be   assignment
   ==========   ==========  ============
   m5           m43         Slit1H:mXp
   m6           m44         Slit1H:mXn
   ==========   ==========  ============

   These assignments will be corrected in the next version of the
   docker image: ``prjemian/synapps``.

There are two representations of the same ``2slit.db`` database.
Choose between a hierarchical or flat representation:

* ``Optics2Slit2D_HV()`` has a hierarchical structure::

   slit1
       h
           xp, xn, size, center
       v
           xp, xn, size, center

* ``Optics2Slit2D_InbOutBotTop()`` has a flat structure::

   slit1
       top
       bot
       out
       inb
       hsize
       hcenter
       vsize
       vcenter

"""

__all__ = """
    slit1
""".split()

import logging

# Choose between alternate interfaces to the same controls:
from apstools.synApps import Optics2Slit2D_HV
# from apstools.synApps import Optics2Slit2D_InbOutBotTop

from .. import iconfig

logger = logging.getLogger(__name__)
logger.info(__file__)

IOC = iconfig.get("GP_IOC_PREFIX", "gp:")


slit1 = Optics2Slit2D_HV(f"{IOC}Slit1", name="slit1")
