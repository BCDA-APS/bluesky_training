import pathlib
import sys

ROOT_PATH = (pathlib.Path(__file__).parent.parent).absolute()
sys.path.append(str(ROOT_PATH))


def test_startup(capsys):
    from instrument.collection import iconfig

    out, err = capsys.readouterr()

    match_list = [
        # "_iconfig.py",
    ]
    for item in match_list:
        assert item in str(out), item

    match_list = [
        "collection.py",
        "scaler.py",
        "logging started",
        "logging level = 10",
        "#### Startup is complete. ####",
    ]
    for item in match_list:
        assert item in str(err), item

    assert "/queueserver" not in str(out)
    assert "/queueserver" not in str(err)
