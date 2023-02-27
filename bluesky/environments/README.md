# Environment Definitions

This directory contains the [YAML](https://yaml.org) files that define the
package requirements (and possibly the acceptable versions) for a conda
environment.

CONTENTS

- [Environment Definitions](#environment-definitions)
  - [YAML files](#yaml-files)
  - [Managing environments](#managing-environments)

## YAML files

This directory contains the master source for these YAML files.
The repository is: https://github.com/BCDA-APS/bluesky_training/tree/main/environments

version | file
--- | ---
2023-2 (developing) | [`environment_2023_2.yml`](./environment_2023_2.yml)
2023-1 (latest) | [`environment_2023_1.yml`](./environment_2023_1.yml)

_note_: Prior to the 2023-2 version, the master source for these YAML files was the
[BCDA Bluesky
configuration](https://github.com/BCDA-APS/use_bluesky/tree/main/install)
repository.

## Managing environments

Some advice is provided for [managing conda environments](./admin/README.md)
with these files, such as [creating a new Bluesky environment](./admin/bluesky.md).

First you must activate the environment you will use (if not already activated).
Such as:

```bash
(base) prjemian@zap:~$ conda activate bluesky_2023_2
(bluesky_2023_2) prjemian@zap:~$ 
```
