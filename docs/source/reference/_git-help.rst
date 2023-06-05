Using git for version control
=============================

While version control is optional, it is _highly recommended [#]_ [#]_
that you place your bluesky instrument directory under some form of
software version control. [#]_
At minimum, this can provide some form of backup protection. It also
helps others to collaborate with similar bluesky instruments by sharing
your instrument’s implementations.

There are many `guides available online <#guides>`__ to learn about
``git`` and GitHub or GitLab. This document will not attempt to cover
that material. Rather, this document will describe the steps to place
the ``bluesky`` directory and its contents under ``git`` version control
and push to a GitHub repository.

.. [#] Why use version control?
   https://www.git-tower.com/learn/git/ebook/en/desktop-gui/basics/why-use-version-control

.. [#] Why use version control?
   https://about.gitlab.com/topics/version-control/#why-use-version-control

.. [#] software version control guide
   https://www.software.com/devops-guides/version-control-guide

.. FIXME: more editing needed here after pandoc conversion from markdown

Overview
--------

1. Identify the web host for the repository

   1. Possible web hosts include:

      1. `GitHub <#github>`__
      2. `APS GitLab <#aps-gitlab>`__
      3. others not described here

   2. Use or create an `organization for the beamline <#beamline-github-organizations>`__.
   3. Create a new repository for the ``bluesky`` directory

2. Make the ``bluesky/`` directory into a ``git`` repository - either

   -  clone the repository from the web host
   -  Use ```git init`` <https://github.com/git-guides/git-init>`__ in
      the ``bluesky/`` directory

3. Create a ```.gitignore``
   file <https://git-scm.com/docs/gitignore>`__, such as this
   `example <https://github.com/APS-USAXS/usaxs-bluesky/blob/master/.gitignore>`__
4. `Add <https://git-scm.com/docs/git-add>`__ content and
   `commit <https://git-scm.com/docs/git-commit>`__ with `a meaningful
   commit
   message <https://www.freecodecamp.org/news/git-best-practices-commits-and-code-reviews/>`__
   (see these
   `hints <https://github.com/bluesky/databroker/blob/main/.github/CONTRIBUTING.md#writing-the-commit-message>`__
   for relevant prefixes)
5. `Push <https://git-scm.com/docs/git-push>`__ content to web host

GitHub
~~~~~~

Most beamlines will use `GitHub <https://github.com>`__ to host their
``bluesky`` repositories. These are publicly-accessible (read-only) so
do not place any content there that should not be publicly-accessible.

See this document to learn more about:

-  GitHub
   `organizations <https://support.github.com/features/organizations>`__
-  GitHub
   `repositories <https://support.github.com/features/repositories>`__

GitHub organizes repositories using this pattern:
``https://github.com/ORGANIZATION/REPOSITORY``

In ``ORGANIZATION`` is either a single user’s account or a named
orgnization (created by some GitHub user).

Note that GitHub now uses multi-factor authentication
(`MFA <https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication>`__).

Beamline GitHub organizations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use GitHub organizations to provide version control for various software
projects used by a beamline. This naming convention is recommended for
the beamline organization:

-  create a GitHub *organization* with a name like this :
   ``APS-SSS-GGG``
-  ``SSS`` : sector, beamline, and station (such as ``32IDC``)
-  ``GGG`` : operating group (such as ``MIC`` for the XSD/Microscopy
   group)
-  Within each organization, create a *repository* :
   ``bluesky-INSTRUMENT``
-  ``INSTRUMENT`` : the name of the sintrument, such as ``USAXS``

APS GitLab
~~~~~~~~~~

When there is content that requires access restrictions (thus, not
publicly-accessible), the `APS GitLab <https://git.aps.anl.gov/>`__
server, managed by the APS IT group, is available to host that content.
The server provides `online help <https://git.aps.anl.gov/help>`__
comparable to that provided by GitHub.

GitLab organizes repositories using this pattern:
``https://git.aps.anl.gov/ORGANIZATION/SUBGROUP/REPOSITORY``

The ``SUBGROUP`` level is optional.

Create a GitHub repository
--------------------------

We took notes when creating a repository for the APS 6-ID-D `HEDM
bluesky
instrument <https://github.com/aps-ht-hedm/bluesky_instrument.git>`__.
Once you have a GitHub organization, follow the notes
`here <./create_github_repo.md>`__.

Guides
------

This is a sampling of How-To guides explaining git and GitHub
repositories.

-  https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github
-  https://dzone.com/articles/ten-easy-steps-to-start-using-git-and-github
-  https://www.freecodecamp.org/news/introduction-to-git-and-github/
-  https://www.digitalocean.com/community/tutorials/how-to-push-an-existing-project-to-github
-  https://www.geeksforgeeks.org/how-to-push-folders-from-local-pc-to-github-using-git-commands/
