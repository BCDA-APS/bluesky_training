# Setup your databroker catalog configuration

The bluesky instrument uses a YAML file which describes the connection
with some location where data is stored, typically a MongoDB collection.
This is called a catalog configuration file.

The catalog configuration file must be placed in a directory where
[`databroker`](https://blueskyproject.io/databroker/how-to/mongo-backed-catalog.html)
expects to find it.  Run this snippet to find the list of paths where it looks on your system:

```bash
(bluesky_2023_2) user@host:~/bluesky$ python -c "import databroker; print(databroker.catalog_search_path())"
('/home/user/.local/share/intake', '/home/user/.conda/envs/bluesky_2023_2/share/intake')
```

Create a YAML file in one of these directories. (The actual file name does not
matter.  Only that it ends with `.yml`.  Also, amongst all the `.yml` files
found on the search path, any catalog names defined only appear once.)  Since
you might recreate the environment, it is suggested not to install into any
environment directory (such as
`/home/user/.conda/envs/bluesky_2023_2/share/intake` listed above).

Here is an example used with the Bluesky training demonstration:

```yml
# file: training.yml
# purpose: Configuration file to connect Bluesky databroker with MongoDB
# For Bluesky Python Training at APS

# Copy to: ~/.local/share/intake/training.yml
# Create subdirectories as needed

sources:
  training:
    args:
      asset_registry_db: mongodb://localhost:27017/training-bluesky
      metadatastore_db: mongodb://localhost:27017/training-bluesky
    driver: bluesky-mongo-normalized-catalog
```

Let's assume (for example purposes) this catalog assignment:

- name: `45ida_abcd`
- MongoDB server: `mongoserver.xray.aps.anl.gov`
- MongoDB collection: `45ida_abcd-bluesky`

1. Create any missing directories as needed: `mkdir -p ~/.local/share/intake`
1. Create file `~/.local/share/intake/databroker_catalog.yml`
1. Open in an editor and copy/paste the content above.
1. Change `training:` to your catalog's name, such as `45ida_abcd:`
1. Change both lines with `mongodb://...` to
   `mongodb://mongoserver.xray.aps.anl.gov:27017/45ida_abcd-bluesky`.
1. Change the comments accordingly.

Confirm that databroker can find this catalog configuration file:

```bash
(bluesky_2023_2) user@host:~/bluesky$ python -c "import databroker; print(list(databroker.catalog))"
['45ida_abcd']
```
