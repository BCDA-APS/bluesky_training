"""
Install a new instrument package for bluesky from the training template.
"""

import argparse
import logging
import pathlib
import shutil
import tempfile
import time
import zipfile

import requests

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
    print(f"Downloading {DOWNLOAD_URL}")
    r = requests.get(DOWNLOAD_URL, stream=True)
    if not r.ok:
        raise RuntimeError(f"Problem getting zip file: {DOWNLOAD_URL}")
    with open(LOCAL_ZIP_FILE, "wb") as f:
        f.write(r.content)


def extract_content(archive, destination):
    """Extract the bluesky directory from the repo zip file."""
    print(f"Extracting content from {archive}")
    z = zipfile.ZipFile(archive)
    print(f"Installing to {destination}")

    # fmt: off
    for item in z.namelist():
        if (
            item.startswith(HEADER)
            and
            not item.endswith(".ipynb")
        ):
            # print(item)
            z.extract(item, path=destination)
    # fmt: on


def move_content(source, destination):
    """Move the content into the destination directory."""
    for item in source.iterdir():
        target = destination / item.name
        if item.is_file():
            # print(f"file: {item.name}  -->  {target}")
            shutil.copy2(item, destination / target)
        elif item.is_dir():
            # print(f"dir:  {item.name}  -->  {target}")
            shutil.copytree(item, destination / target)
        else:
            print(f"ERROR: did not identify {item=}")


def revise_content(destination):
    """
    Edit the instrument package to be a new template.
    """
    # TODO: edit training configuration (IOC prefix, area detector, motors, ...)
    # instrument/iconfig.yml
    # instrument/devices/__init__.py
    # instrument/plans/__init__.py
    # session_log_patch.md
    # tests/
    # Consider adding a Sphinx docs directory


if __name__ == "__main__":
    # TODO: command-line interface
    destination = "/tmp/tmp_instrument"
    new_instrument_from_template(destination)
    # TODO: set up git repo
