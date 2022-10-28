# session_log patch

Look through all python source code files.

```py
import pathlib

def examine_file(file_object):
    if not file_object.exists():
        raise RuntimeError(f"Does not exist: {file_object}")

    # do not edit these files
    if file_object.name in ("collection.py", "qstarter.py"):
        return

    out = []
    found = False
    buf = open(file_object, "r").read()
    for line in buf.split("\n"):
        if ("session_logs" in line) and ("import" in line):
            found = True
            print(f"{file_object} -- '{line}'")
            line = "\n".join(
                [
                    "import logging",
                    "",
                    "logger = logging.getLogger(__name__)",
                ]
            )
        out.append(line)
    print(f"{file_object=}: {found=}")
    if found:
        with open(file_object, "w") as fp:
            fp.write("\n".join(out))
            print(f"updated: {file_object}")

def examine_dir(path=None):
    if path is None:
        path = pathlib.Path()
    for item in path.iterdir():
        if item.is_dir():
            examine_dir(item)
        elif item.is_file() and item.name.endswith(".py"):
            examine_file(item)
```

- replace lines that match: `git grep session_logs | grep import`
- with: `import logging; logger = logging.getLogger(__name__)`

Matching examples below:

```bash
(bluesky_2022_3) prjemian@zap:~/bluesky$ git grep session_logs | grep import
instrument/collection.py:from .session_logs import logger
instrument/collection.py:from .session_logs import logger
instrument/devices/aps_source.py:from ..session_logs import logger
instrument/devices/aps_undulator.py:from ..session_logs import logger
instrument/devices/area_detector.py:from ..session_logs import logger
instrument/devices/calculation_records.py:from ..session_logs import logger
instrument/devices/ioc_stats.py:from ..session_logs import logger
instrument/devices/kohzu_monochromator.py:from ..session_logs import logger
instrument/devices/motors.py:from ..session_logs import logger
instrument/devices/noisy_detector.py:from ..session_logs import logger
instrument/devices/scaler.py:from ..session_logs import logger
instrument/devices/shutter_simulator.py:from ..session_logs import logger
instrument/devices/temperature_signal.py:from ..session_logs import logger
instrument/framework/check_bluesky.py:from ..session_logs import logger
instrument/framework/check_python.py:from ..session_logs import logger
instrument/framework/initialize.py:from ..session_logs import logger
instrument/framework/metadata.py:from ..session_logs import logger
instrument/mpl/console.py:from ..session_logs import *
instrument/mpl/notebook.py:from ..session_logs import *
instrument/plans/peak_finder_example.py:from ..session_logs import logger
instrument/utils/image_analysis.py:from ..session_logs import logger
(bluesky_2022_3) prjemian@zap:~/bluesky$ git grep __file__ | grep logger
instrument/_iconfig.py:logger.info(__file__)
instrument/callbacks/spec_data_file_writer.py:logger.info(__file__)
instrument/collection.py:logger.info(__file__)
instrument/devices/aps_source.py:logger.info(__file__)
instrument/devices/aps_undulator.py:logger.info(__file__)
instrument/devices/area_detector.py:logger.info(__file__)
instrument/devices/calculation_records.py:logger.info(__file__)
instrument/devices/ioc_stats.py:logger.info(__file__)
instrument/devices/kohzu_monochromator.py:logger.info(__file__)
instrument/devices/motors.py:logger.info(__file__)
instrument/devices/noisy_detector.py:logger.info(__file__)
instrument/devices/scaler.py:logger.info(__file__)
instrument/devices/shutter_simulator.py:logger.info(__file__)
instrument/devices/temperature_signal.py:logger.info(__file__)
instrument/epics_signal_config.py:logger.info(__file__)
instrument/framework/check_bluesky.py:logger.info(__file__)
instrument/framework/check_python.py:logger.info(__file__)
instrument/framework/initialize.py:logger.info(__file__)
instrument/framework/metadata.py:logger.info(__file__)
instrument/mpl/console.py:logger.info(__file__)
instrument/mpl/notebook.py:logger.info(__file__)
instrument/plans/peak_finder_example.py:logger.info(__file__)
instrument/queueserver.py:logger.info(__file__)
instrument/queueserver_framework.py:logger.info(__file__)
instrument/utils/image_analysis.py:logger.info(__file__)
```
