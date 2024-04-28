.. _instrument.create_starter_soft_link:

Create a File System Soft Link
==============================

This optional step makes it easy for those who prefer to use a command-line
interface to start an IPython console session with Bluesky.

Assuming that your account has this directory: ``${HOME}/bin/``, create the
soft link with this command::

    ln -s ${HOME}/bluesky/blueskyStarter.sh ${HOME}/bin/

.. _instrument.start_bluesky_console_session:

Start a Bluesky Console Session
-------------------------------

With this soft link in the executable PATH, you can start an IPython console
session for Bluesky from any directory with one simple command::

    blueskyStarter.sh

The ``${HOME}/bin`` directory
---------------------------------------

The ``${HOME}/bin/`` directory (same as ``~/bin/``) is an optional addition to a
Linux account. It is often used to save (or link to) executable software and
starter scripts for various application software of interest to users of this
account.

In linux, ``~/`` is Linux shorthand for the user account home directory.

If your account does not have this directory, create it with this command::

    mkdir ~/bin

:see: https://www.baeldung.com/linux/home-bin-directory
:see: https://askubuntu.com/questions/402353/how-to-add-home-username-bin-to-path

File system links
---------------------

It is assumed that your account has this directory ``~/bin/`` and that this
directory is on the executable path (as defined by the ``PATH`` environment
variable).

Lots of information about file system links is available online.

:see: https://www.redhat.com/sysadmin/linking-linux-explained
