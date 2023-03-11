#!/usr/bin/env python

"""
Install a new instrument package for bluesky from the training template.
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
    destination = pathlib.Path(destination or tempfile.mkdtemp())
    if destination.exists() and len(list(destination.iterdir())) > 0:
        # We _could_ use shutil to clear the directory but
        # the caller should sort this out.  We should not
        # delete any content without review.
        raise RuntimeError(f"Directory is not empty: {destination=}")

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
    shutil.rmtree(destination / BASE_NAME)

    return destination


def download_zip():
    """Download repository as ZIP file."""
    logger.info("Downloading '%s'", DOWNLOAD_URL)
    r = requests.get(DOWNLOAD_URL, stream=True)
    if not r.ok:
        raise RuntimeError(f"Problem getting zip file: {DOWNLOAD_URL}")
    with open(LOCAL_ZIP_FILE, "wb") as f:
        f.write(r.content)


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
        with open(file, "r") as f:
            lines = f.read().splitlines()
        return lines

    def write(file, lines):
        with open(file, "w") as f:
            f.write("\n".join(lines))

    file = destination / "instrument" / "iconfig.yml"
    # TODO: Leave this for user to edit as first steps

    file = destination / "instrument" / "devices" / "__init__.py"
    buf = []
    for line in read(file):
        if line.startswith("from ."):
            line = f"# {line}"
        buf.append(line)
    write(file, buf)

    file = destination / "instrument" / "plans" / "__init__.py"
    buf = []
    for line in read(file):
        if line.startswith("from ."):
            line = f"# {line}"
        buf.append(line)
    write(file, buf)

    # fmt: off
    remove_these_files = [
        destination / "export_data.sh",
        destination / "session_log-patch.md",
    ]
    for file in remove_these_files:
        if file.exists():
            file.unlink()
    # fmt: on

    # Consider keeping ``tests/`` as examples, but it will need
    # serious revision to be a template.
    subdir = destination / "tests"
    if subdir.exists():
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
        "-d",
        "--directory",
        type=str,
        help=(
            "Directory for the new instrument."
            "  Default is the present working directory"
            f" ({pathlib.Path('.').absolute()})."
            "  The directory will be created if it does not exist."
            "  If the directory exists and it is not empty, this"
            " program will stop before any action is taken."
        ),
        default=".",
    )

    parser.add_argument(
        "--quiet",
        help="Report only warnings and errors. (default)",
        action="store_const",
        dest="loglevel",
        const=logging.WARNING,
        default=logging.WARNING,
    )
    parser.add_argument(
        "--verbose",
        help="Also report information messages.",
        action="store_const",
        dest="loglevel",
        const=logging.INFO,
    )
    parser.add_argument(
        "--debug",
        help="Also report debugging messages",
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
    DEVELOPMENT = True  # TODO: remove for production
    if DEVELOPMENT:
        destination = pathlib.Path("/tmp/tmp_instrument")  # TODO: remove for production
    logger.info("Installing to: '%s'", destination)

    if DEVELOPMENT:
        if destination.exists():  # TODO: remove for production
            shutil.rmtree(destination)

    new_instrument_from_template(destination)
    # TODO: set up git repo
