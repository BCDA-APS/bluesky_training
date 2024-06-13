import datetime
import os
import pathlib
import shutil
import tempfile

import pytest
from apstools.utils import cleanupText
from spec2nexus.spec import SpecDataFile
from spec2nexus.spec import is_spec_file

from bluesky.run_engine import RunEngine
from instrument.callbacks.spec_data_file_writer import RE_finder
from instrument.callbacks.spec_data_file_writer import newSpecFile
from instrument.callbacks.spec_data_file_writer import specwriter

INITIAL_SCAN_ID = 1234
RE = RunEngine(dict(scan_id=INITIAL_SCAN_ID))
# databroker is not necessary
TEST_DATA_FILE = pathlib.Path(__file__).parent / "20230509-191819.spec_data"


@pytest.fixture
def tempdir():
    t = pathlib.Path(tempfile.mkdtemp())
    yield t
    shutil.rmtree(t)


@pytest.mark.parametrize(
    "title, scan_id",
    [
        ["title", None],  # most common use
        ["title", 1],
        ["title", 555],
        ["x+y = 12% (by weight)", None],  # title is not safe
        [None, None],  # title cannot be None, will raise a TypeError
    ],
)
def test_newSpecFile(title, scan_id, tempdir):
    assert tempdir.exists()
    os.chdir(tempdir)  # newSpecFile() works in pwd

    # make sure test case does not match initial value
    assert scan_id != INITIAL_SCAN_ID

    RE.md["scan_id"] = INITIAL_SCAN_ID
    assert RE.md["scan_id"] == INITIAL_SCAN_ID

    kwargs = dict(RE=RE)
    if scan_id is not None:
        kwargs["scan_id"] = scan_id

    if title is None:
        with pytest.raises(TypeError):
            newSpecFile(title, **kwargs)
    else:
        newSpecFile(title, **kwargs)

        assert RE.md["scan_id"] == 1 if scan_id is None else scan_id
        safe_title = cleanupText(title)
        assert safe_title in specwriter.spec_filename.name
        assert specwriter.spec_filename.name[5:] == f"_{safe_title}.dat"
        assert isinstance(specwriter.spec_filename, pathlib.Path)


@pytest.mark.parametrize("scan_id", [1, 2, 3, INITIAL_SCAN_ID - 1, INITIAL_SCAN_ID + 1])
def test_issue_271(scan_id, tempdir):
    """newSpecFile("title", scan_id=1) did not reset scan id."""
    found_RE = RE_finder()  # Won't find the one in this module's globals()
    assert found_RE is None

    RE = RunEngine()  # define for this function, so it can be found
    found_RE = RE_finder()
    assert found_RE is not None
    assert found_RE == RE

    assert isinstance(scan_id, int)
    assert tempdir.exists()
    os.chdir(tempdir)  # newSpecFile() works in pwd

    RE.md["scan_id"] = INITIAL_SCAN_ID
    assert RE.md["scan_id"] == INITIAL_SCAN_ID

    newSpecFile("title", scan_id=scan_id, RE=RE)
    assert RE.md["scan_id"] != INITIAL_SCAN_ID
    assert RE.md["scan_id"] == scan_id

    # repeat, without passing RE as parameter
    RE.md["scan_id"] = INITIAL_SCAN_ID
    assert RE.md["scan_id"] == INITIAL_SCAN_ID

    newSpecFile("title", scan_id=scan_id)
    assert RE.md["scan_id"] != INITIAL_SCAN_ID
    assert RE.md["scan_id"] == scan_id


def test_newSpecFile_with_existing(tempdir):
    assert tempdir.exists()
    os.chdir(tempdir)  # newSpecFile() works in pwd

    assert TEST_DATA_FILE.exists()
    assert is_spec_file(TEST_DATA_FILE)

    mmdd = str(datetime.datetime.now()).split()[0][5:].replace("-", "_")
    title = "testfile"
    testfile = tempdir / f"{mmdd}_{title}.dat"
    assert not testfile.exists()

    # make the file to be named by newSpecFile() below
    shutil.copy2(TEST_DATA_FILE, testfile)
    assert testfile.exists()
    assert is_spec_file(testfile)

    sdf = SpecDataFile(testfile)
    last_scan_number_in_file = int(sdf.getLastScanNumber())
    assert last_scan_number_in_file == 983

    RE.md["scan_id"] = INITIAL_SCAN_ID
    assert RE.md["scan_id"] == INITIAL_SCAN_ID

    scan_id = max(last_scan_number_in_file, INITIAL_SCAN_ID) + 10
    newSpecFile(title, RE=RE)
    assert RE.md["scan_id"] != INITIAL_SCAN_ID
    assert RE.md["scan_id"] != scan_id
    assert RE.md["scan_id"] == last_scan_number_in_file

    RE.md["scan_id"] = INITIAL_SCAN_ID  # reset it before next call
    newSpecFile(title, scan_id=scan_id, RE=RE)
    assert RE.md["scan_id"] != INITIAL_SCAN_ID
    assert RE.md["scan_id"] != scan_id
    assert RE.md["scan_id"] == last_scan_number_in_file
