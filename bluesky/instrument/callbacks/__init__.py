# this file makes the .py files here importable

from .. import iconfig

if iconfig.get("WRITE_SPEC_DATA_FILES", False):
    from .spec_data_file_writer import *

del iconfig
