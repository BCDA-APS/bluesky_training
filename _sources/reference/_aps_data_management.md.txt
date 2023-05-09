# APS Data Management

The [APS Data
Management](https://www.aps.anl.gov/Science/Scientific-Software/DataManagement)
software is used to process data file workflows after the data has been
collected (by Bluesky or other software).  The workflows are sets of
instructions that describe how to find the data and what should happen next with
its processing.

Add the APS data management API and test it.  If successful, this will
not print any errors to standard output.

```bash
# install
conda install -c apsu aps-dm-api(base)

# test
CMD="from dm.cat_web_service.api.catApiFactory import CatApiFactory;"
CMD+=" api = CatApiFactory.getRunCatApi()"
python -c "${CMD}"
```
