from bluesky_queueserver_api import BPlan
from bluesky_queueserver_api.zmq import REManagerAPI
from bluesky_queueserver_api.comm_base import RequestFailedError
import pytest
import time


RM = REManagerAPI()


def test_env_open():
    keylist = "re_state manager_state worker_environment_state".split()
    try:
        RM.environment_close()
        RM.wait_for_idle()
    except RequestFailedError:
        pass
    RM.environment_open()
    status = RM.status()
    for key in keylist:
        assert key in status
        assert status[key] != "idle", (key, status.get(key, "no such key"))

    RM.wait_for_idle()

    status = RM.status()
    for key in keylist:
        assert key in status
        assert status[key] == "idle", (key, status.get(key, "no such key"))


@pytest.mark.parametrize(
    "plan, items",
    [
        ["findpeak_multipass", 1],
        ["repeat_findpeak", 1],
        ["two_pass_scan", 1],
    ]
)
def test_findpeak_multipass(plan, items):
    RM.queue_clear()
    RM.history_clear()
    RM.item_add(BPlan(plan))
    assert RM.status()["items_in_queue"] == 1

    RM.queue_start()
    time.sleep(2)
    assert RM.status()["re_state"] != "idle"

    RM.wait_for_idle()
    assert RM.status()["items_in_history"] == items
