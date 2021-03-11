import databroker
from scipy import ndimage
from apstools.utils import listruns

cat = databroker.catalog["class_data_examples"]
print(f"{len(cat) = }")
listruns(db=cat.v1)

run = cat.search({"scan_id": 44})[-1]
ds = run.primary.read()
np_arr = ds["temperature_readback"]
print(f"{np_arr.mean().values = }")
print(f"{np_arr.std().values  = }")

# TODO: repeat for scan_id = 57

run = cat.search({"scan_id": 80})[-1]
ds = run.primary.read()
np_frame = ds["adsimdet_image"][0][0].to_masked_array()
print(f"{ndimage.measurements.center_of_mass(np_frame)   = }")
print(f"{ndimage.measurements.maximum_position(np_frame) = }")
print(f"{np_frame.max() = }")
print(f"{np_frame.min() = }")
