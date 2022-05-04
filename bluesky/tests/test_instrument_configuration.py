import pathlib
import sys
import yaml


ROOT_PATH = (pathlib.Path(__file__).parent.parent).absolute()
ICONFIG_YAML_FILE = ROOT_PATH / "instrument" / "iconfig.yml"


def test_existential():
    assert ROOT_PATH.exists()
    assert ICONFIG_YAML_FILE.exists()


def test_contents():
    iconfig = yaml.load(open(ICONFIG_YAML_FILE, "r").read(), yaml.Loader)

    assert iconfig is not None
    assert isinstance(iconfig, dict)
    assert len(iconfig) > 5

    key_list = """
    DATABROKER_CATALOG
    MINIMUM_BLUESKY_VERSION
    MINIMUM_DATABROKER_VERSION
    MINIMUM_OPHYD_VERSION
    MINIMUM_PYTHON_VERSION
    PV_CONNECTION_TIMEOUT
    PV_TIMEOUT
    PV_WRITE_TIMEOUT
    RUNENGINE_METADATA
    """.strip().split()
    for key in key_list:
        assert key in iconfig


def test_import():
    sys.path.append(str(ROOT_PATH))
    from instrument import iconfig

    assert isinstance(iconfig, dict)
