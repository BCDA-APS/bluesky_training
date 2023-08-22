"""
EPICS area_detector ADSimDetector
"""

__all__ = """
    adsimdet
    change_ad_simulated_image_parameters
    dither_ad_peak_position
    dither_ad_off
    dither_ad_on
""".split()

import logging

logger = logging.getLogger(__name__)

logger.info(__file__)

from .. import iconfig
from .calculation_records import calcs
from apstools.devices import AD_plugin_primed
from apstools.devices import AD_prime_plugin2
from apstools.devices import CamMixin_V34
from apstools.devices import SingleTrigger_V34
from ophyd import ADComponent
from ophyd import DetectorBase
from ophyd import SimDetectorCam
from ophyd.areadetector.filestore_mixins import FileStoreHDF5IterativeWrite
from ophyd.areadetector.plugins import HDF5Plugin_V34
from ophyd.areadetector.plugins import ImagePlugin_V34
from ophyd.areadetector.plugins import PvaPlugin_V34
from ophyd.ophydobj import Kind
import numpy as np
import pathlib


IOC = iconfig.get("ADSIM_IOC_PREFIX", "ad:")

IMAGE_DIR = iconfig["AD_IMAGE_DIR"]
AD_IOC_MOUNT_PATH = pathlib.Path(iconfig["AD_MOUNT_PATH"])
BLUESKY_MOUNT_PATH = pathlib.Path(iconfig["BLUESKY_MOUNT_PATH"])

# MUST end with a `/`, pathlib will NOT provide it
WRITE_PATH_TEMPLATE = f"{AD_IOC_MOUNT_PATH / IMAGE_DIR}/"
READ_PATH_TEMPLATE = f"{BLUESKY_MOUNT_PATH / IMAGE_DIR}/"


class SimDetectorCam_V34(CamMixin_V34, SimDetectorCam):
    """Revise SimDetectorCam for ADCore revisions."""


class MyHDF5Plugin(FileStoreHDF5IterativeWrite, HDF5Plugin_V34):
    """
    Add data acquisition methods to HDF5Plugin.

    * ``stage()`` - prepare device PVs befor data acquisition
    * ``unstage()`` - restore device PVs after data acquisition
    * ``generate_datum()`` - coordinate image storage metadata
    """

    def stage(self):
        self.stage_sigs.move_to_end("capture", last=True)
        super().stage()


class SimDetector_V34(SingleTrigger_V34, DetectorBase):
    """
    ADSimDetector

    SingleTrigger:

    * stop any current acquisition
    * sets image_mode to 'Multiple'
    """

    cam = ADComponent(SimDetectorCam_V34, "cam1:")
    hdf1 = ADComponent(
        MyHDF5Plugin,
        "HDF1:",
        write_path_template=WRITE_PATH_TEMPLATE,
        read_path_template=READ_PATH_TEMPLATE,
    )
    image = ADComponent(ImagePlugin_V34, "image1:")
    pva = ADComponent(PvaPlugin_V34, "Pva1:")


def change_ad_simulated_image_parameters():
    """
    Make the image be a "peak" (simulate a diffraction spot).

    Randomly-placed, random max, random noise

    Not a bluesky plan (uses blocking calls).
    """
    cam = adsimdet.cam
    cam.reset.put(1)
    cam.sim_mode.put(1)  # Peaks
    cam.gain.put(100 + 100 * np.random.random())
    cam.offset.put(10 * np.random.random())
    cam.noise.put(20 * np.random.random())
    cam.peak_start.peak_start_x.put(200 + 500 * np.random.random())
    cam.peak_start.peak_start_y.put(200 + 500 * np.random.random())
    cam.peak_width.peak_width_x.put(10 + 100 * np.random.random())
    cam.peak_width.peak_width_y.put(10 + 100 * np.random.random())
    cam.peak_variation.put(0.5 + 20 * np.random.random())


def dither_ad_off():
    # select: 0 = off (Passive)
    calcs.calc9.scanning_rate.put(0)
    calcs.calc10.scanning_rate.put(0)


def dither_ad_on(select=6):
    # select: 6 = 1 Hz (1 second), 9 = 10 Hz (.1 second)
    calcs.calc9.scanning_rate.put(select)
    calcs.calc10.scanning_rate.put(select)


def dither_ad_peak_position(magnitude=40):
    """
    Dither the peak position using swait records.
    """
    peak = adsimdet.cam.peak_start
    formula = f"min(B,max(C,A+{magnitude}*(RNDM-0.5)))"
    x = calcs.calc9
    x.description.put("adsimdet peak X dither")
    x.calculation.put(formula)
    x.channels.A.input_pv.put(peak.peak_start_x.pvname)
    x.channels.B.input_value.put(900)  # upper limit
    x.channels.C.input_value.put(100)  # lower limit
    x.output_link_pv.put(peak.peak_start_x.setpoint_pvname)
    y = calcs.calc10
    y.description.put("adsimdet peak Y dither")
    y.calculation.put(formula)
    y.channels.A.input_pv.put(peak.peak_start_y.pvname)
    y.channels.B.input_value.put(900)  # upper limit
    y.channels.C.input_value.put(100)  # lower limit
    y.output_link_pv.put(peak.peak_start_y.setpoint_pvname)
    dither_ad_on()


try:
    adsimdet = SimDetector_V34(IOC, name="adsimdet", labels=("area_detector",))
    adsimdet.wait_for_connection(timeout=15)
except TimeoutError:
    logger.warning("Did not connect to area detector IOC '%s'", IOC)
    adsimdet = None
else:
    # override default settings from ophyd
    adsimdet.hdf1.create_directory.put(-5)
    adsimdet.hdf1.kind = Kind.config | Kind.normal  # Ensure plugin's read is called.

    # The plugins do not block, the cam must wait for the plugins to finish.
    for det in (adsimdet, ):
        for nm in det.component_names:
            obj = getattr(det, nm)
            if "blocking_callbacks" in dir(obj):  # is it a plugin?
                obj.stage_sigs["blocking_callbacks"] = "No"
        det.cam.stage_sigs["wait_for_plugins"] = "Yes"
        det.hdf1.stage_sigs["compression"] = "zlib"
        det.hdf1.stage_sigs.move_to_end("capture", last=True)

    if iconfig.get("ALLOW_AREA_DETECTOR_WARMUP", False):
        # Even with `lazy_open=1`, ophyd checks if the area
        # detector HDF5 plugin has been primed.  We might
        # need to prime it.  Here's ophyd's test:
        # if np.array(adsimdet.hdf1.array_size.get()).sum() == 0:
        #     logger.info(f"Priming {adsimdet.hdf1.name} ...")
        #     adsimdet.hdf1.warmup()
        #     logger.info(f"Enabling {adsimdet.image.name} plugin ...")
        #     adsimdet.image.enable.put("Enable")
        # Ophyd's test is not sufficient.
        # WORKAROUND (involving a few more tests)
        if not AD_plugin_primed(adsimdet.hdf1):
            AD_prime_plugin2(adsimdet.hdf1)

    change_ad_simulated_image_parameters()  # new peak parameters
    dither_ad_peak_position()  # EPICS will dither the peak position
