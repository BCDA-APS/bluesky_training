import databroker
import datetime
import numpy as np
from scipy.ndimage.measurements import center_of_mass
from scipy.ndimage.measurements import maximum_position

list(databroker.catalog)
cat = databroker.catalog["class_data_examples"]


def get_run_by_scan_id(scan_id):
    # run = cat.search({"scan_id": scan_id})[-1]
    run = cat[scan_id]  # simple access
    print(f"{run.metadata['start']['scan_id'] = }")
    print(f"{run.metadata['start']['plan_name'] = }")
    return run


def get_run_by_uid(uid):
    run = cat[uid]
    print(f"{run.metadata['start']['scan_id']  = }")
    print(f"{run.metadata['start']['plan_name'] = }")
    ts = run.metadata['start']['time']
    dt = datetime.datetime.fromtimestamp(ts)
    iso = dt.isoformat(sep=" ", timespec="seconds")
    print(f"start time: {iso}")
    return run


def run_analyzer(run):
    ds = run.primary.read()
    if "adsimdet_image" in ds:
        print("image")
        np_frame = ds["adsimdet_image"][0][0].to_masked_array()
        com = center_of_mass(np_frame)
        maxp = maximum_position(np_frame)
        print(f"{com = }")
        print(f"{maxp = }")

    elif "noisy" in ds:
        print("1-D scan")
        y_arr = ds["noisy"].to_masked_array()
        x_arr = ds["m1"].to_masked_array()
        n_arr = np.arange(len(y_arr))
        com = np.interp(center_of_mass(y_arr), n_arr, x_arr)
        maxp = np.interp(maximum_position(y_arr), n_arr, x_arr)
        print(f"{com = }")
        print(f"{maxp = }")
        print(f"{len(y_arr) = }")

    elif "temperature_readback" in ds:
        print("temperatures")
        y_arr = ds["temperature_readback"]
        print(f"{y_arr.mean().values = }")
        print(f"{y_arr.std().values = }")
        print(f"{len(y_arr) = }")

    else:
        print(f"Not recognized: {ds = }")


SORT_KEY = "time"
def sorter(uid):
    return cat[uid].metadata["start"][SORT_KEY]


for uid in sorted(cat, key=sorter):
    run = get_run_by_uid(uid)
    if "stop" not in run.metadata:
        print("no stop document")
    elif run.metadata["stop"] is None:
        print("stop document empty")
    elif run.metadata["stop"]["exit_status"] != "success":
        print(f'{run.metadata["stop"]["exit_status"] = }')
    else:
        run_analyzer(run)
    print("-"*40)
