"""
local, custom Device definitions
"""

# from ophyd.log import config_ophyd_logging
# config_ophyd_logging(level="DEBUG")
#     # 'ophyd' — the logger to which all ophyd log records propagate
#     # 'ophyd.objects' — logs records from all devices and signals (that is, OphydObject subclasses)
#     # 'ophyd.control_layer' — logs requests issued to the underlying control layer (e.g. pyepics, caproto)
#     # 'ophyd.event_dispatcher' — issues regular summaries of the backlog of updates from the control layer that are being processed on background threads

# from .aps_source import *
# from .aps_undulator import *

from .area_detector import *
from .calculation_records import *
from .ioc_stats import *
from .kohzu_monochromator import *
from .motors import *
from .noisy_detector import *
from .scaler import *
from .shutter_simulator import *
from .temperature_signal import *
