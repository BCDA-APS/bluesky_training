.. _git-help:

Using Git for version control
=============================

.. _beamline-github-organizations:

Beamline GitHub organizations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Most beamlines will use `GitHub <https://github.com>`__ to host their
``bluesky`` repositories. These are publicly-accessible (read-only) so
do not place any content there that should not be publicly-accessible.

GitHub organizes repositories using this pattern:
``https://github.com/ORGANIZATION/REPOSITORY``

``ORGANIZATION`` is either a single user’s account or a named
`organizations <https://support.github.com/features/organizations>`__ 
(created by some GitHub user).

This naming convention is recommended for the beamline organization:

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


Guides
------

This is a sampling of How-To guides explaining Git and GitHub
repositories.

- Why use version control?
   https://www.git-tower.com/learn/git/ebook/en/desktop-gui/basics/why-use-version-control
- Why use version control?
   https://about.gitlab.com/topics/version-control/#why-use-version-control
- Software version control guide
   https://www.software.com/devops-guides/version-control-guide
-  https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github
-  https://dzone.com/articles/ten-easy-steps-to-start-using-git-and-github
-  https://www.freecodecamp.org/news/introduction-to-git-and-github/
-  https://www.digitalocean.com/community/tutorials/how-to-push-an-existing-project-to-github
-  https://www.geeksforgeeks.org/how-to-push-folders-from-local-pc-to-github-using-git-commands/
