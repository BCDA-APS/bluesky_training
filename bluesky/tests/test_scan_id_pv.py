"""
Test that a PV can be used for the RunEngine's scan_id value.
"""

import pathlib

import pytest
import yaml
from ophyd import EpicsSignal, Signal

from bluesky import plans as bp
from bluesky import run_engine


@pytest.fixture
def scan_id_pv():
    instrument_path = pathlib.Path(__file__).parent.parent / "instrument"
    assert instrument_path.exists()

    with open(instrument_path / "iconfig.yml") as f:
        iconfig = yaml.load(f.read(), Loader=yaml.Loader)
    assert len(iconfig) > 0

    scan_id_pv = iconfig.get("RUN_ENGINE_SCAN_ID_PV")
    if scan_id_pv is None:
        IOC = iconfig.get("GP_IOC_PREFIX")
        assert IOC is not None
        scan_id_pv = f"{IOC}gp:int20"

    yield scan_id_pv


def test_connection(scan_id_pv):
    scan_id = EpicsSignal(scan_id_pv, name="scan_id")
    scan_id.wait_for_connection()
    if scan_id.get() < 0:
        scan_id.put(0)
    assert scan_id.get() >= 0


def test_custom_function(scan_id_pv):
    scan_id = EpicsSignal(scan_id_pv, name="scan_id")
    scan_id.wait_for_connection()
    assert scan_id.connected

    def epics_scan_id_source(md):
        value = max(scan_id.get(), -1) + 1
        scan_id.put(value)
        return value

    v0 = scan_id.get()
    assert v0 >= 0
    epics_scan_id_source({}) == v0 + 1


def test_with_run_engine(scan_id_pv):
    scan_id = EpicsSignal(scan_id_pv, name="scan_id")
    scan_id.wait_for_connection()
    assert scan_id.connected

    def epics_scan_id_source(md):
        value = max(scan_id.get(), -1) + 1
        scan_id.put(value)
        return value

    RE = run_engine.RunEngine(scan_id_source=epics_scan_id_source)
    assert "scan_id" not in RE.md

    signal = Signal(name="signal")
    v0 = scan_id.get()
    uids = RE(bp.count([signal]))
    assert uids is not None
    assert len(uids) == 1
    assert RE.md.get("scan_id") == v0 + 1
