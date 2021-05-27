# TODO: punch list

2021-05-26

* [x] `start_xxx.sh` and `start_adsim.sh` need to find `remove_container.sh` : absolute paths needed
* [x] `remove_container.sh` does not need to remove container images after stopping since they remove themselves : two lines commented out
* [x] need the [`dotenv`](https://github.com/pedroburon/dotenv) extension (`pip install dotenv`)
* [ ] describe_instrument notebook cannot find pv_finder.py code
* [ ] locate_image_peak notebook failed to find HDF5 file


Note: The jupyterhub runs from a custom docker container

* [ ] custom scan stalls in cell 11 `RE(customScan())`

## Simpler?

If Python is installed in the docker container that runs JupyterHub, then the
Python install and config is not necessary, only the EPICS IOCs, the databroker
config, the notebooks, and the example data are needed.  Could be simpler then?
