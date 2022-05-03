import databroker
import pathlib
import sys

ROOT_PATH = (pathlib.Path(__file__).parent.parent).absolute()
sys.path.append(str(ROOT_PATH))


def test_catalog():
    from instrument import iconfig

    if len(list(databroker.catalog)) > 0:
        assert "DATABROKER_CATALOG" in iconfig

        cat_name = iconfig["DATABROKER_CATALOG"]
        assert cat_name in list(databroker.catalog)

        cat = databroker.catalog[cat_name]
        assert isinstance(cat, databroker._drivers.mongo_normalized.BlueskyMongoCatalog)
