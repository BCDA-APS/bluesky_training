# Bluesky Instrument Template

**Caution**:  If you will use the bluesky queueserver (QS), note that _every_
Python file in this directory will be executed when QS starts the RunEngine.
Don't add extra Python files to this directory.  Instead, put them in `user/` or
somewhere else.

Contains:

description | item(s)
--- | ---
Introduction | [`intro2bluesky.md`](intro2bluesky.md)
IPython console startup | [`console/`](console/README.md)
Bluesky queueserver support | [introduction](qserver.md), `*qs*`
Instrument configuration | `instrument/`
Conda environments | [`environments/`](./environments/README.md)
Unit tests | [`tests/`](./tests/README.md)
Documentation | [How-to, examples, tutorials, reference](https://bcda-aps.github.io/bluesky_training)
