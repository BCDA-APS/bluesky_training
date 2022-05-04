import pathlib
import sys

ROOT_PATH = (pathlib.Path(__file__).parent.parent).absolute()
sys.path.append(str(ROOT_PATH))


def test_startup(capsys):
    from qstarter import iconfig

    out, err = capsys.readouterr()

    match_list = [
        "queueserver.py",
        "queueserver_framework.py",
        "RunEngine metadata:",
        "List of Plans:",
        "Table of Devices and signals:",
        "Instrument configuration (iconfig):",
        "databroker_catalog",
    ]
    for item in match_list:
        assert item in str(out), item

    match_list = []
    for item in match_list:
        assert item in str(err), item

    assert "/framework" not in str(out)
    assert "/framework" not in str(err)
