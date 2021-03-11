# already running a bluesky session


def up_down_once(lo, hi, num, md={}):
    dets = [scaler1, temperature]
    yield from bp.scan(dets, m1, lo, hi, num, md=md)
    yield from bp.scan(dets, m1, hi, lo, num, md=md)

def up_down_twice(lo, hi, num, md={}):
    yield from up_down_once(lo, hi, num, md=md)
    yield from up_down_once(lo, hi, num, md=md)

# recommend checking plans FIRST before running with RE():
#     summarize_plan(up_down_once(0, 1, 5))
#     summarize_plan(up_down_twice(0, 1, 5))

# ---

def mv_shutter(mode):
    logger.info("setting shutter: %s", mode)
    yield from bps.mv(shutter, mode)
    logger.debug("shutter state: %s", shutter.state)


def my_scan(dets, m, sta, fin, num, md={}):
    yield from mv_shutter("open")
    yield from bp.scan(dets, m, sta, fin, num, md=md)
    yield from mv_shutter("close")


def up_down(hi=1, lo=0, iterations=2, num=11, ct_time=1, hi_dwell=5, lo_dwell=10, md={}):
    dets = [scaler1, temperature]
    channels = ["I0", "diode"]
    scaler1.select_channels(channels)

    orig_sigs = scaler1.stage_sigs
    scaler1.stage_sigs["preset_time"] = ct_time

    _md = dict(custom_plan="up_down", example=True)
    _md.update(md)

    logger.info("move to the start position")
    yield from bps.mv(m1, lo)
    for i in range(iterations):
        _md["iteration"] = i+1
        logger.info("sleep for %.2fs", lo_dwell)
        yield from bps.sleep(lo_dwell)
        _md["direction"] = "up"
        yield from my_scan(dets, m1, lo, hi, num, md=_md)

        logger.info("sleep for %.2fs", hi_dwell)
        yield from bps.sleep(hi_dwell)
        _md["direction"] = "down"
        yield from my_scan(dets, m1, hi, lo, num, md=_md)

    logger.info("scanning complete")
    scaler1.select_channels()
    scaler1.stage_sigs = orig_sigs
