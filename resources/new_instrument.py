"""
Install a new instrument for bluesky.
"""

import io
import pathlib
import shutil
import tempfile
import zipfile

import requests

# TODO: import logging

REPO_NAME = "bluesky_training"
BRANCH = "main"
BASE_NAME = f"{REPO_NAME}-{BRANCH}"
LOCAL_ZIP_FILE = pathlib.Path("/tmp") / f"{BASE_NAME}.zip"
TRAINING_REPO = f"https://github.com/BCDA-APS/{REPO_NAME}"
TRAINING_REPO_URL = f"{TRAINING_REPO}/archive/refs/heads/{BRANCH}.zip"


def new_instrument_from_template(destination=None):
    """
    Install a new bluesky instrument from the online training repository.

    destination obj:
        Instance of pathlib.Path(), directory for the new instrument.
    """
    destination = pathlib.Path(destination or tempfile.mkdtemp())
    if destination.exists() and len(list(destination.iterdir())) > 0:
        # We _could_ use shutil to clear the directory but
        # the caller should sort this out.  We should not
        # delete any content without review.
        raise RuntimeError(f"Directory is not empty: {destination=}")

    # download or use from local copy
    if LOCAL_ZIP_FILE.exists():
        print(f"Using {LOCAL_ZIP_FILE}")
        stream = LOCAL_ZIP_FILE
    else:
        print(f"Downloading {TRAINING_REPO_URL}")
        r = requests.get(TRAINING_REPO_URL, stream=True)
        if not r.ok:
            raise RuntimeError(f"Problem getting zip file: {TRAINING_REPO_URL}")
        stream = io.BytesIO(r.content)
    z = zipfile.ZipFile(stream)
    print(f"Installing to {destination}")

    # extract the bluesky directory from the repo zip file
    header = f"{BASE_NAME}/bluesky/"
    # fmt: off
    for item in z.namelist():
        if (
            item.startswith(header)
            and
            not item.endswith(".ipynb")
        ):
            # print(item)
            z.extract(item, path=destination)
    # fmt: on

    # move the content into the destination directory
    for item in (destination / header).iterdir():
        target = destination / item.name
        if item.is_file():
            # print(f"file: {item.name}  -->  {target}")
            shutil.copy2(item, destination / target)
        elif item.is_dir():
            # print(f"dir:  {item.name}  -->  {target}")
            shutil.copytree(item, destination / target)
        else:
            print(f"ERROR: did not identify {item=}")

    # remove the source directory from the repository
    shutil.rmtree(destination / BASE_NAME)


if __name__ == "__main__":
    # TODO: command-line interface
    destination = "/tmp/tmp_instrument"
    new_instrument_from_template(destination)
    # TODO: set up git repo
