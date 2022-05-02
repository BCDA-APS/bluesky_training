"""
Various reports that are NOT bluesky plans
"""

__all__ = """
    print_instrument_configuration
    print_RE_metadata
""".split()


from .. import iconfig
from ..queueserver_framework import RE
import pyRestTable


def _make_table(data):
    table = pyRestTable.Table()
    table.labels = "key value".split()
    for k, v in sorted(data.items()):
        if isinstance(v, dict):
            table.addRow((k, _make_table(v)))
        else:
            table.addRow((k, v))
    return table


def print_instrument_configuration():
    if len(iconfig) > 0:
        table = _make_table(iconfig)
        print("")
        print("Instrument configuration (iconfig):")
        print(table)


def print_RE_metadata():
    """
    Print a table (to the console) with the current RunEngine metadata.
    """
    if len(RE.md) > 0:
        table = _make_table(RE.md)
        print("")
        print("RunEngine metadata:")
        print(table)
