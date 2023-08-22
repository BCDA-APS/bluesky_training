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
    INFO:__main__:Initialized Git repository in '/tmp/tmp_instrument'

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
    --no-git    Do not create a git repository.

DEPENDENCIES:

* Python 3.6 or higher
* Python Standard Libraries (already installed with Python)
* requests package: https://docs.python-requests.org/en/latest/index.html
"""

import logging
import pathlib
import shlex
import shutil
import subprocess
import tempfile
import time
import zipfile

import requests

logger = logging.getLogger(__name__)  # set by command_line_options()

GITHUB_URL = "https://github.com"
REPO_NAME = "bluesky_training"
REPO_ORG = "BCDA-APS"
# BRANCH = "main"  # TODO: use latest release name

# BASE_NAME = f"{REPO_NAME}-{BRANCH}"
# HEADER = f"{BASE_NAME}/bluesky/"
TRAINING_REPO = f"{GITHUB_URL}/{REPO_ORG}/{REPO_NAME}"

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

EXECUTABLE_PERMISSIONS = 0o775  # rwxrwxr-x
READ_WRITE_PERMISSIONS = 0o664  # rw-rw-r--
EXECUTABLE_SUFFIXES = ".sh .py".split()

release_details_cache_ = None  # minimize calls to GitHub API


def new_instrument_from_template(destination=None, make_git_repo=False):
    """
    Install a new bluesky instrument from the online training repository.

    PARAMETERS

    destination *str* or *obj*:
        Directory for the new instrument.  Either a *str* or an
        instance of ``pathlib.Path()``.
        If ``None``, installs into a temporary directory.
    make_git_repo *bool*:
        Create a git repository by calling ``git init``.
    """
    destination = pathlib.Path(destination or tempfile.mkdtemp()).absolute()
    if destination.exists() and len(list(destination.iterdir())) > 0:
        # We _could_ use shutil to clear the directory but
        # the caller should sort this out.  We should not
        # delete any content without review.
        raise RuntimeError("Directory is not empty: " + str(destination))
    # fmt: off
    branch, base_name, header = branch_name_header(REPO_ORG, REPO_NAME)
    local_zip_file = pathlib.Path("/tmp") / f"{base_name}.zip"
    if (
        not local_zip_file.exists()
        or local_zip_file.stat().st_mtime < time.time() - 1 * DAY
    ):
        download_zip(local_zip_file, branch)
    # fmt: on

    extract_content(local_zip_file, destination)
    move_content(destination / header, destination)
    revise_content(destination)

    # remove the source directory from the repository
    logger.debug("Removing directory '%s'", destination / base_name)
    shutil.rmtree(destination / base_name)

    adjust_permissions(destination)

    if make_git_repo:
        git_init(destination)

    return destination


def adjust_permissions(target):
    if target.is_dir() or target.suffix in EXECUTABLE_SUFFIXES:
        permissions = EXECUTABLE_PERMISSIONS
    else:
        permissions = READ_WRITE_PERMISSIONS
    target.chmod(permissions)
    logger.debug("Set permissions=o%o: '%s'", permissions, target)
    if target.is_dir():
        for item in target.iterdir():
            adjust_permissions(item)


def branch_name_header(org, repo):
    branch = latest_github_release_string(REPO_ORG, REPO_NAME)
    base_name = f"{REPO_NAME}-{branch.lstrip('v')}"
    header = f"{base_name}/bluesky/"
    return branch, base_name, header


def download_zip(local_zip_file, branch):
    """Download repository as ZIP file."""
    url = f"{TRAINING_REPO}/archive/refs/tags/{branch}.zip"
    logger.info("Downloading '%s'", url)
    try:
        r = requests.get(url, stream=True)
        if not r.ok:
            raise RuntimeError(f"Problem getting zip file: {url}")
        with open(local_zip_file, "wb") as f:
            f.write(r.content)
    except Exception as exinfo:
        logger.warning("Problem: %s", exinfo)


def extract_content(archive, destination):
    """Extract the bluesky directory from the repo zip file."""
    logger.info("Extracting content from '%s'", archive)
    z = zipfile.ZipFile(archive)
    logger.info("Installing to '%s'", destination)

    branch, base_name, header = branch_name_header(REPO_ORG, REPO_NAME)

    # fmt: off
    for item in z.namelist():
        if (
            item.startswith(header)
            and
            not item.endswith(".ipynb")
        ):
            logger.debug("extracting archive item: '%s'", item)
            z.extract(item, path=destination)
        elif item == f"{base_name}/.gitignore":  # special case
            logger.debug("extracting archive item: '%s'", item)
            z.extract(item, path=destination)
        else:
            logger.debug("ignoring archive item: '%s'", item)
    # fmt: on


def git_init(destination):
    """
    Initialize a Git repository in 'destination' and make the first commit.

    User instructions should describe how to set git origin.
    """

    def shell(cmd):
        logger.debug(
            "Execute shell command \"%s\" in directory '%s'.", cmd, destination
        )
        split_command = shlex.split(cmd)
        process = subprocess.Popen(
            split_command,
            cwd=destination,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = process.communicate()
        logger.debug(
            "command output:\n  stdout=%s\n  stderr=%s",
            out.splitlines(),
            err.splitlines(),
        )

    for command in """
        git init
        git add .gitignore
        git add *
        git commit -m 'initial commit'
    """.strip().splitlines():
        shell(command.strip())
    logger.info("Initialized Git repository in '%s'", destination)
    shell("ls -lAFgh")


def latest_github_release_string(org, repo, ref="releases/latest"):
    global release_details_cache_

    if release_details_cache_ is None:
        api = "https://api.github.com/repos"
        url = f"{api}/{org}/{repo}/{ref}"
        response = requests.get(url)
        release_details_cache_ = response.json()

    return release_details_cache_["tag_name"]


def move_content(source, destination):
    """Move the content into the destination directory."""
    item = source.parent / ".gitignore"
    target = destination / item.name
    logger.debug("file: '%s'  -->  '%s'", item.name, target)
    shutil.copy2(item, destination / target)

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

    branch, base_name, header = branch_name_header(REPO_ORG, REPO_NAME)

    file = destination / "instrument" / "iconfig.yml"
    # User should edit this to assigned catalog name.
    key_catalog = "DATABROKER_CATALOG: &databroker_catalog"
    buf = []
    version_found = False
    for line in read(file):
        if key_catalog in line:
            line = f"{key_catalog} EDIT_CATALOG_NAME_HERE"
        elif line.startswith("ICONFIG_VERSION: "):
            line = f"ICONFIG_VERSION: {branch.lstrip('v')}"
            version_found = True
        buf.append(line)
    if not version_found:
        buf.append("")
        line = f"ICONFIG_VERSION: {branch.lstrip('v')}"
        buf.append(line)
        buf.append("")
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
        default=".",
        help=(
            "Directory for the new instrument."
            "  If omitted, use the present working directory"
            f" ({pathlib.Path('.').absolute()})."
            "  The directory will be created if it does not exist."
            "  If the directory exists and it is not empty, this"
            " program will stop before any action is taken."
        ),
        nargs="?",
        type=str,
    )

    logging_group = parser.add_mutually_exclusive_group(required=False)

    logging_group.add_argument(
        "--quiet",
        action="store_const",
        const=logging.WARNING,
        default=logging.INFO,
        dest="loglevel",
        help="Reporting: only warnings and errors",
    )
    logging_group.add_argument(
        "--info",
        action="store_const",
        const=logging.INFO,
        dest="loglevel",
        help="Reporting: also information messages (default)",
    )
    logging_group.add_argument(
        "--debug",
        action="store_const",
        const=logging.DEBUG,
        dest="loglevel",
        help="Reporting: also debugging messages",
    )
    logging_group.add_argument(
        "--no-git",
        action="store_false",
        dest="git_init",
        help="Do not create a git repository.",
    )

    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)
    logger = logging.getLogger(__name__)

    return args


if __name__ == "__main__":
    args = command_line_options()
    destination = pathlib.Path(args.directory)
    logger.info("Requested installation to: '%s'", destination)

    new_instrument_from_template(destination, make_git_repo=args.git_init)
