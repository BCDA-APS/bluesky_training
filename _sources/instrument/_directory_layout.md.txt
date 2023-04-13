# Recommended Directory Layout

## Starter script

```text
~/bin/blueskyStarter.sh  --> ~/bluesky/blueskyStarter.sh
```

<details>
<summary>Install the Starter Script</summary>


The commands and settings to configure the local environment to begin a
Bluesky session can be arranged by a simple shell script that starts the
session.  A sample starter script has been provided:
[`blueskyStarter.sh`](../../../bluesky/blueskyStarter.sh).

To allow this starter script to be called from any directory (such
as the user's data directory), the starter script can be placed in a
directory on the user's executable path.

It is useful to create a local directory (such as `~/bin`) for custom
starter scripts and executable file links.  Use these steps to configure
your account. Add this line to `~/.bash_aliases`:

```bash
export PATH="~/bin:${PATH}"
```

and create the directory:

```bash
mkdir ~/bin
```

**TIP**: You might rename `~/bin/blueskyStarter.sh` to something appropriate for
your instrument name, such as the hypothetical example above:
`blueskyFemtoScanner.sh`

</details>

## The _bluesky_ directory

Contains the `instrument` package and other support:

```text
  bluesky/
    blueskyStarter.sh
    console/
      __start_bluesky_instrument__.py
    instrument/
```

<details>
<summary>Install the _bluesky_ directory</summary>

TODO:

</details>

## IPython profile

for console sessions

```text
  .ipython-bluesky/
    profile_bluesky/
      startup/
        __start_bluesky_instrument__.py --> ~/bluesky/console/__start_bluesky_instrument__.py
```

and [`__start_bluesky_instrument__.py`](https://github.com/BCDA-APS/bluesky_training/blob/main/bluesky/console/__start_bluesky_instrument__.py) is summarized by:

```py
import pathlib, sys
sys.path.append(str(pathlib.Path.home() / "bluesky"))
from instrument.collection import *
```

## Start Bluesky

* Change to desired working directory.
* Start Bluesky session using the starter script.

```bash
blueskyStarter.sh
```
