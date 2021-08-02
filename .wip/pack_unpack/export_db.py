#!/usr/bin/env python

"""
export data from one db and import to another

see: https://github.com/APS-3ID-IXN/ipython-s3blue/issues/2
"""

from databroker import Broker
import datetime, os, shutil, time
import pyRestTable
from dask.bag import text


def main():
    server = "otz"
    otz_config = {
        "description": "heavyweight shared database",
        "metadatastore": {
            "module": "databroker.headersource.mongo",
            "class": "MDS",
            "config": {
                "host": server,
                "port": 27017,
                "database": "metadatastore-production-v1",
                "timezone": "US/Central"
            }
        },
        "assets": {
            "module": "databroker.assets.mongo",
            "class": "Registry",
            "config": {
                "host": server,
                "port": 27017,
                "database": "filestore-production-v1"
            }
        }
    }
    otz_db = Broker.from_config(otz_config)

    tbl = pyRestTable.Table()
    tbl.labels = "beamline uid plan_name".split()
    headers = otz_db(since='2018-09-01', until='2018-11-06')
    for h in headers:
        row = (h.start["beamline_id"], h.start["login_id"], h.start["plan_name"])
        tbl.addRow(row)
    print(tbl)

    tbl = pyRestTable.Table()
    tbl.labels = "date/time # uid plan_name".split()
    headers = otz_db(beamline_id='3-ID')
    for h in headers:
        t_float = h.start["time"]
        dt = datetime.datetime.fromtimestamp(t_float)
        row = [dt, h.start["scan_id"], h.start["uid"], h.start["plan_name"]]
        tbl.addRow(row)
    print(tbl)

    # build a local sqlite database for testing
    test_dir = "/tmp/bluesky"
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    test_config = {
        "description": "lightweight personal database",
        "metadatastore": {
            "module": "databroker.headersource.sqlite",
            "class": "MDS",
            "config": {
                "directory": test_dir,
                "timezone": "US/Central"
            }
        },
        "assets": {
            "module": "databroker.assets.sqlite",
            "class": "Registry",
            "config": {
                "dbpath": test_dir + "/database.sql"
            }
        }
    }
    test_db = Broker.from_config(test_config)
    
    # test the export from otz using a local sqlite db
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
        os.makedirs(test_dir)
    
    for h in otz_db.stream(headers):
        tag, doc = h
        print(tag)
        if tag == "descriptor":
            print(sorted(doc.data_keys.keys()))
        elif tag == "event":
            print(doc.seq_num)
        test_db.insert(tag, doc)
        if tag == "descriptor":
            print(sorted(doc.data_keys.keys()))
        elif tag == "event":
            print(sorted(doc.data_keys.keys()))


import re
ACCEPTABLE_PATTERN = r"[A-Za-z_][\w_]*"


def make_safe(keys):
    def safe(text):
        matching_positions = [
            p 
            for m in re.finditer(ACCEPTABLE_PATTERN, text) 
            for p in range(m.start(), m.end())]
        def rewrite(p):
            return {True: text[p], False: "_"}[p in matching_positions]
        return "".join(map(rewrite, range(len(text))))
    safe_keys = list(map(safe, sorted(keys)))
    return safe_keys


def tester():
    import pyRestTable
    tbl = pyRestTable.Table()
    tbl.addLabel("old")
    tbl.addLabel("new")
    keys = ['NFS, delayed', 'NFS, total', 'NRIXS dlyd-sum', 'NRIXS tot-sum',
    'NRIXS, delayed1', 'NRIXS, delayed2', 'NRIXS, delayed3', 'Time',
    'mca_elapsed_real_time', 'mca_preset_real_time', 'mca_spectrum',
    'neat_stage_x', 'neat_stage_x_user_setpoint', 'neat_stage_y',
    'neat_stage_y_user_setpoint', 'scaler_time']
    safe_keys = make_safe(keys)
    keymap = {k:v for k, v in zip(keys, safe_keys)}
    for old_key, new_key in zip(keys, safe_keys):
        tbl.addRow((old_key, new_key))
    print(tbl)


if __name__ == "__main__":
    main()
    # tester()
