# Environment Definitions

This directory contains the [YAML](https://yaml.org) files that define the
package requirements (and possibly the acceptable versions) for a conda
environment.

## YAML files

This directory contains the master source for these YAML files.
The repository is: https://github.com/BCDA-APS/bluesky_training/

version | file
--- | ---
2023-3 (latest) | [`environment_2023_3.yml`](./environment_2023_3.yml)
2023-2 | [`environment_2023_2.yml`](./environment_2023_2.yml)
2023-1 | [`environment_2023_1.yml`](./archive/environment_2023_1.yml)
2022_3 | [`environment_2022_3.yml`](./archive/environment_2022_3.yml)
2022_2 | [`environment_2022_2.yml`](./archive/environment_2022_2.yml)
2022_1 | [`environment_2022_1.yml`](./archive/environment_2022_1.yml)
2021_2 | [`environment_2021_2.yml`](./archive/environment_2021_2.yml)
2021_1 | [`environment_2021_1.yml`](./archive/environment_2021_1.yml)

_note_: Prior to the 2023-2 version, the master source for these YAML files was the
[BCDA Bluesky
configuration](https://github.com/BCDA-APS/use_bluesky/tree/main/install)
repository.

## Managing environments

First you must activate the conda
[environment](https://bcda-aps.github.io/bluesky_training/reference/_conda_environment.html)
you will use (if not already activated). Such as:

```bash
(base) prjemian@zap:~$ conda activate bluesky_2023_3
(bluesky_2023_3) prjemian@zap:~$ 
```
