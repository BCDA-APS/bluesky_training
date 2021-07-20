from collections import defaultdict
from dataclasses import dataclass
import apstools.utils
import databroker
import databroker.queries
import datetime
import numpy as np
import pandas as pd
import pyRestTable


def getCatalog(ref=None):
    if isinstance(ref, str):  # and ref in databroker.catalog:
        return databroker.catalog[ref]
    if ref is not None and hasattr(ref, "v2"):
        return ref.v2
    cat = getDefaultCatalog()
    if cat is None:
        raise ValueError(f"Cannot identify default databroker catalog.")
    return cat


def findCatalogsInNamespace():
    g = {}
    g.update(getDefaultNamespace())
    ns_cats = {}
    for k, v in g.items():
        if not k.startswith("_") and hasattr(v, "__class__"):
            try:
                if (hasattr(v.v2, "container") and hasattr(v.v2, "metadata")):
                    ns_cats[k] = v
            except (AttributeError, TypeError):
                continue
    return ns_cats


def getDefaultCatalog():
    from intake.catalog import Catalog

    cats = findCatalogsInNamespace()
    if len(cats) == 1:
        return cats[list(cats.keys())[0]]
    if len(cats) > 1:
        choices = '   '.join([
            f"{k} ({v.name})"
            for k, v in cats.items()
        ])
        raise ValueError(
            "No catalog defined.  "
            "Multiple catalog objects available."
            "  Specify one of these:"
            f" {choices}"
        )

    cats = list(databroker.catalog)
    if len(cats) == 1:
        return databroker.catalog[cats[0]]
    if len(cats) > 1:
        choices = '   '.join([f'databroker.catalog[\"{k}\"]' for k in cats])
        raise ValueError(
            "No catalog defined.  "
            "Multiple catalog configurations available."
            "  Create specific catalog object from one of these commands:"
            f" {choices}"
        )

    raise ValueError("No catalogs available.")


def getDefaultNamespace():
    """
    get the IPython shell's namespace dictionary (or globals() if not found)
    """
    try:
        from IPython import get_ipython

        ns = get_ipython().user_ns
    except AttributeError:
        ns = globals()
    return ns


@dataclass
class ListRuns:
    """
    List the runs from the given catalog according to some options.

    EXAMPLE::

        ListRuns(cat).to_dataframe()

    """

    cat: object = None
    # FIXME: ValueError: mutable default <class 'dict'> for field db_search_terms is not allowed: use default_factory
    # TODO: can we pick up db_search_terms as all the optional kwargs?
    db_search_terms: dict = None
    keys: str = None
    missing: str = ""
    num: int = 20
    reverse: bool = True
    since: str = None
    sortby: str = "time"
    timefmt: str = "%Y-%m-%d %H:%M:%S"
    until: str = None

    def get_by_key(self, md, key):
        """
        Get run's metadata value by key.

        Look in ``start`` document first.
        If not found, look in ``stop`` document.
        If not found, report using ``self.missing``.

        If ``key`` is found but value is None, report as ``self.missing``.

        The ``time`` key will be formatted by the ``self.timefmt`` value.
        See https://strftime.org/ for examples.  The special ``timefmt="raw"``
        is used to report time as the raw value (floating point time as used in
        python's ``time.time()``).
        """
        if key == "time":
            v = md["start"][key]
            if self.timefmt != "raw":
                ts = datetime.datetime.fromtimestamp(v)
                v = ts.strftime(self.timefmt)
        elif key in md["start"]:
            v = md["start"].get(key, self.missing)
        elif md["stop"] and key in md["stop"]:
            v = md["stop"].get(key, self.missing)
        else:
            v = self.missing
        return v

    def _check_cat(self):
        if self.cat is None:
            self.cat = getCatalog()

    def _apply_search_filters(self):
        since = self.since or "1995-01-01"
        until = self.until or "2100-12-31"
        self._check_cat()
        cat = self.cat.v2.search(
            databroker.queries.TimeRange(since=since, until=until)
        ).search(self.db_search_terms or {})
        return cat

    def parse_runs(self):
        """Parse the runs for the given metadata keys.  Return a dict."""
        cat = self._apply_search_filters()
        num_runs_requested = min(abs(self.num), len(cat))
        dd = {
            key: [
                self.get_by_key(run.metadata, key)
                for _, run in sorted(
                    cat.items(), key=self.sorter, reverse=self.reverse
                )[:num_runs_requested]
            ]
            for key in self.keys
        }
        return dd

    def sorter(self, args):
        """Sort runs in desired order based on metadata key."""
        # args : (uid, run)
        md = args[1].metadata
        for doc in "start stop".split():
            if md[doc] and self.sortby in md[doc]:
                return md[doc][self.sortby] or self.missing
        return self.missing

    def _check_keys(self):
        """Check that self.keys is a list of strings."""
        # other _known_ keys: uid exit_status motors num_points
        self.keys = self.keys or "scan_id time plan_name detectors"
        if isinstance(self.keys, str) and self.keys.find(" ") >= 0:
            # convert a space-delimited string of names
            self.keys = self.keys.split()

    def to_dataframe(self):
        """Output as pandas DataFrame object"""
        self._check_keys()
        dd = self.parse_runs()
        return pd.DataFrame(dd, columns=self.keys)

    def to_table(self, fmt=None):
        """Output as pyRestTable object.  (backwards compatible)"""
        self._check_keys()
        dd = self.parse_runs()

        table = pyRestTable.Table()
        rows = []
        for label, values in dd.items():
            table.addLabel(label)
            rows.append(values)
        table.rows = list(zip(*rows))

        return table.reST(fmt=fmt or "simple")


def listruns2(
    cat=None,
    keys=None,
    missing="",
    num=20,
    printing="smart",
    reverse=True,
    since=None,
    sortby="time",
    timefmt="%Y-%m-%d %H:%M:%S",
    until=None,
    tablefmt="dataframe"
):
    """List runs from catalog."""

    lr = ListRuns(
        cat=cat,
        keys=keys,
        missing=missing,
        num=num,
        reverse=reverse,
        since=since,
        sortby=sortby,
        timefmt=timefmt,
        until=until,
    )

    table_format_function = dict(
        dataframe=lr.to_dataframe,
        table=lr.to_table,
    ).get(tablefmt or "dataframe", lr.to_table)
    obj = table_format_function()

    do_print = False
    if printing:
        if lr.cat is not None:
            print(f"catalog: {lr.cat.name}")
        if printing == "smart":
            try:
                get_ipython()  # console or notebook will handle
            except NameError:
                do_print = True  # we print it here
        else:
            do_print = True
    if do_print:
        print(obj)
        return
    return obj


def listruns(db=None, tablefmt="table", printing=True, **kwargs):
    """List runs from catalog (legacy support: see listruns2())"""
    lr = listruns2(cat=db, tablefmt=tablefmt, printing=False, **kwargs)
    if printing:
        print(lr)
    else:
        return lr
