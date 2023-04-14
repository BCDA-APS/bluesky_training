#!/usr/bin/env python

"""
Install a new instrument package for bluesky from the training template.

* see: https://github.com/BCDA-APS/bluesky_training/blob/main/resources/new_bluesky_instrument.py
* raw: https://raw.githubusercontent.com/BCDA-APS/bluesky_training/main/resources/new_bluesky_instrument.py

EXAMPLE::

    (base) user@host:~$ new_bluesky_instrument.py  /tmp/tmp_instrument/
    INFO:__main__:Installing to: '/tmp/tmp_instrument'
    INFO:__main__:Downloading 'https://github.com/BCDA-APS/bluesky_training/archive/refs/heads/main.zip'
    INFO:__main__:Extracting content from '/tmp/bluesky_training-main.zip'
    INFO:__main__:Installing to '/tmp/tmp_instrument'

USAGE::

    (base) user@host:~$ new_bluesky_instrument.py  /tmp/tmp_instrument/
    usage: new_bluesky_instrument.py [-h] [--quiet | --info | --debug] [directory]

    Install a new instrument package for bluesky from the training template.

    positional arguments:
    directory   Directory for the new instrument. If omitted, use the present working directory (/home/user). The directory will be
                created if it does not exist. If the directory exists and it is not empty, this program will stop before any action is taken.

    options:
    -h, --help  show this help message and exit
    --quiet     Reporting: only warnings and errors
    --info      Reporting: also information messages (default)
    --debug     Reporting: also debugging messages

DEPENDENCIES:

* Python 3.6 or higher
* Python Standard Libraries (already installed with Python)
* requests package: https://docs.python-requests.org/en/latest/index.html
"""

import logging
import pathlib
import shutil
import tempfile
import time
import zipfile

import requests

logger = None  # set by command_line_options()

REPO_NAME = "bluesky_training"
REPO_ORG = "https://github.com/BCDA-APS"
BRANCH = "main"

BASE_NAME = f"{REPO_NAME}-{BRANCH}"
HEADER = f"{BASE_NAME}/bluesky/"
LOCAL_ZIP_FILE = pathlib.Path("/tmp") / f"{BASE_NAME}.zip"
TRAINING_REPO = f"{REPO_ORG}/{REPO_NAME}"
DOWNLOAD_URL = f"{TRAINING_REPO}/archive/refs/heads/{BRANCH}.zip"

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR


def new_instrument_from_template(destination=None):
    """
    Install a new bluesky instrument from the online training repository.

    PARAMETERS

    destination *str* or *obj*:
        Directory for the new instrument.  Either a *str* or an
        instance of ``pathlib.Path()``.
        If ``None``, installs into a temporary directory.
    """
    destination = pathlib.Path(destination or tempfile.mkdtemp()).absolute()
    if destination.exists() and len(list(destination.iterdir())) > 0:
        # We _could_ use shutil to clear the directory but
        # the caller should sort this out.  We should not
        # delete any content without review.
        raise RuntimeError("Directory is not empty: " + str(destination))
    # fmt: off
    if (
        not LOCAL_ZIP_FILE.exists()
        or LOCAL_ZIP_FILE.stat().st_mtime < time.time() - 1 * DAY
    ):
        download_zip()
    # fmt: on

    extract_content(LOCAL_ZIP_FILE, destination)
    move_content(destination / HEADER, destination)
    revise_content(destination)

    # remove the source directory from the repository
    logger.debug("Removing directory '%s'", destination / BASE_NAME)
    shutil.rmtree(destination / BASE_NAME)

    return destination


def download_zip():
    """Download repository as ZIP file."""
    logger.info("Downloading '%s'", DOWNLOAD_URL)
    try:
        r = requests.get(DOWNLOAD_URL, stream=True)
        if not r.ok:
            raise RuntimeError(f"Problem getting zip file: {DOWNLOAD_URL}")
        with open(LOCAL_ZIP_FILE, "wb") as f:
            f.write(r.content)
    except Exception as exinfo:
        logger.warning("Problem: %s", exinfo)


def extract_content(archive, destination):
    """Extract the bluesky directory from the repo zip file."""
    logger.info("Extracting content from '%s'", archive)
    z = zipfile.ZipFile(archive)
    logger.info("Installing to '%s'", destination)

    # fmt: off
    for item in z.namelist():
        if (
            item.startswith(HEADER)
            and
            not item.endswith(".ipynb")
        ):
            logger.debug("extracting archive item: '%s'", item)
            z.extract(item, path=destination)
        else:
            logger.debug("ignoring archive item: '%s'", item)
    # fmt: on


def move_content(source, destination):
    """Move the content into the destination directory."""
    for item in source.iterdir():
        target = destination / item.name
        if item.is_file():
            logger.debug("file: '%s'  -->  '%s'", item.name, target)
            shutil.copy2(item, destination / target)
        elif item.is_dir():
            logger.debug("dir:  '%s'  -->  '%s'", item.name, target)
            shutil.copytree(item, destination / target)
        else:
            logger.warning("PROBLEM: did not identify this content: '%s'", item)


def revise_content(destination):
    """
    Change the instrument package from training to be a new template.
    """
    destination = pathlib.Path(destination)

    def read(file):
        logger.debug("Reading '%s'", file)
        with open(file, "r") as f:
            lines = f.read().splitlines()
        return lines

    def write(file, lines):
        logger.debug("Writing '%s'", file)
        with open(file, "w") as f:
            f.write("\n".join(lines))

    file = destination / "instrument" / "iconfig.yml"
    # User should edit this to assigned catalog name.
    key = "DATABROKER_CATALOG: &databroker_catalog"
    buf = []
    for line in read(file):
        if key in line:
            line = f"{key} EDIT_CATALOG_NAME_HERE"
        buf.append(line)
    write(file, buf)

    for group in "devices plans".split():
        file = destination / "instrument" / group / "__init__.py"
        buf = []
        for line in read(file):
            if line.startswith("from ."):
                line = f"# {line}"
            buf.append(line)
        write(file, buf)

    # Consider keeping ``tests/`` as examples, but it will need
    # serious revision to be a template.
    # For now, remove it.
    subdir = destination / "tests"
    if subdir.exists():
        logger.debug("Removing directory '%s'", subdir)
        shutil.rmtree(subdir)


def command_line_options():
    import argparse
    import sys

    global logger

    parser = argparse.ArgumentParser(
        prog=pathlib.Path(sys.argv[0]).name,
        description=__doc__.strip().splitlines()[0],
    )

    parser.add_argument(
        "directory",
        type=str,
        help=(
            "Directory for the new instrument."
            "  If omitted, use the present working directory"
            f" ({pathlib.Path('.').absolute()})."
            "  The directory will be created if it does not exist."
            "  If the directory exists and it is not empty, this"
            " program will stop before any action is taken."
        ),
        default=".",
        nargs="?",
    )

    logging_group = parser.add_mutually_exclusive_group(required=False)

    logging_group.add_argument(
        "--quiet",
        help="Reporting: only warnings and errors",
        action="store_const",
        dest="loglevel",
        const=logging.WARNING,
        default=logging.INFO,
    )
    logging_group.add_argument(
        "--info",
        help="Reporting: also information messages (default)",
        action="store_const",
        dest="loglevel",
        const=logging.INFO,
    )
    logging_group.add_argument(
        "--debug",
        help="Reporting: also debugging messages",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
    )

    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)
    logger = logging.getLogger(__name__)

    return args


if __name__ == "__main__":
    args = command_line_options()
    destination = pathlib.Path(args.directory)
    logger.info("Requested installation to: '%s'", destination)

    # # TODO: Developer use only
    # destination = pathlib.Path(__file__).parent / "bluesky"
    # if destination.exists():
    #     logger.debug("Removing file '%s'", destination)
    #     shutil.rmtree(destination)

    new_instrument_from_template(destination)
    # User instructions should describe how to set up git repo: git init
