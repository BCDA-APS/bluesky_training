# Translate Previous SPEC Configuration

The [`apstools`](https://bcda-aps.github.io/apstools/latest/) package has an application that will translate most
of the SPEC config file into ophyd commands.  The output is to the
console.  Use a pipe to direct the output to a new file:

```bash
export INSTRUMENT_DIR=${BLUESKY_DIR}/profile_bluesky/startup/instrument
spec2ophyd CONFIG_FILE | tee ${INSTRUMENT_DIR}/devices/spec.py
```

then make sure to import this file in
`${INSTRUMENT_DIR}/devices/__init__.py` following the pattern of other
imports there.

<details>
<summary><tt>spec2ophyd</tt> example:</summary>

```bash
(bluesky_2022_3) mintadmin@mint-vm:/tmp$ spec2ophyd /home/mintadmin/Documents/projects/BCDA-APS/apstools/apstools/migration/config
"""
ophyd commands from SPEC config file

file: /home/mintadmin/Documents/projects/BCDA-APS/apstools/apstools/migration/config

CAUTION: Review the object names below before using them!
    Some names may not be valid python identifiers
    or may be reserved (such as ``time`` or ``del``)
    or may be vulnerable to re-definition because
    they are short or common.
"""

from ophyd import EpicsMotor, EpicsSignal
from ophyd.scaler import ScalerCH

un0 = EpicsMotor('9idcLAX:m58:c0:m1', name='un0', labels=('motor',))  # unused0
mx = EpicsMotor('9idcLAX:m58:c0:m2', name='mx', labels=('motor',))
my = EpicsMotor('9idcLAX:m58:c0:m3', name='my', labels=('motor',))
waxsx = EpicsMotor('9idcLAX:m58:c0:m4', name='waxsx', labels=('motor',))  # WAXS X
ax = EpicsMotor('9idcLAX:m58:c0:m5', name='ax', labels=('motor',))
gslity = EpicsMotor('9idcLAX:m58:c0:m6', name='gslity', labels=('motor',))  # Gslit_Y
az = EpicsMotor('9idcLAX:m58:c0:m7', name='az', labels=('motor',))
un7 = EpicsMotor('9idcLAX:m58:c0:m8', name='un7', labels=('motor',))  # unused7
msx = EpicsMotor('9idcLAX:m58:c1:m1', name='msx', labels=('motor',))
msy = EpicsMotor('9idcLAX:m58:c1:m2', name='msy', labels=('motor',))
art = EpicsMotor('9idcLAX:m58:c1:m3', name='art', labels=('motor',))  # ART50-100
asy = EpicsMotor('9idcLAX:m58:c1:m4', name='asy', labels=('motor',))
gslitx = EpicsMotor('9idcLAX:m58:c1:m5', name='gslitx', labels=('motor',))  # Gslit_X
tcam = EpicsMotor('9idcLAX:m58:c1:m6', name='tcam', labels=('motor',))
camy = EpicsMotor('9idcLAX:m58:c1:m7', name='camy', labels=('motor',))  # cam_y
tens = EpicsMotor('9idcLAX:m58:c1:m8', name='tens', labels=('motor',))  # Tension
sx = EpicsMotor('9idcLAX:m58:c2:m1', name='sx', labels=('motor',))
sy = EpicsMotor('9idcLAX:m58:c2:m2', name='sy', labels=('motor',))
dx = EpicsMotor('9idcLAX:m58:c2:m3', name='dx', labels=('motor',))
un19 = EpicsMotor('9idcLAX:m58:c2:m4', name='un19', labels=('motor',))
uslvcen = EpicsMotor('9idcLAX:m58:c2:m5', name='uslvcen', labels=('motor',))  # uslitvercen
uslhcen = EpicsMotor('9idcLAX:m58:c2:m6', name='uslhcen', labels=('motor',))  # uslithorcen
uslvap = EpicsMotor('9idcLAX:m58:c2:m7', name='uslvap', labels=('motor',))  # uslitverap
uslhap = EpicsMotor('9idcLAX:m58:c2:m8', name='uslhap', labels=('motor',))  # uslithorap
pin_x = EpicsMotor('9idcLAX:mxv:c0:m1', name='pin_x', labels=('motor',))
pin_z = EpicsMotor('9idcLAX:mxv:c0:m2', name='pin_z', labels=('motor',))
gslout = EpicsMotor('9idcLAX:mxv:c0:m3', name='gslout', labels=('motor',))  # GSlit_outb # read_mode=7
gslinb = EpicsMotor('9idcLAX:mxv:c0:m4', name='gslinb', labels=('motor',))  # GSlit_inb # read_mode=7
gsltop = EpicsMotor('9idcLAX:mxv:c0:m5', name='gsltop', labels=('motor',))  # GSlit_top # read_mode=7
gslbot = EpicsMotor('9idcLAX:mxv:c0:m6', name='gslbot', labels=('motor',))  # GSlit_bot # read_mode=7
un30 = EpicsMotor('9idcLAX:mxv:c0:m7', name='un30', labels=('motor',))  # unused30
pin_y = EpicsMotor('9idcLAX:mxv:c0:m8', name='pin_y', labels=('motor',))
a2rp = EpicsMotor('9idcLAX:pi:c0:m1', name='a2rp', labels=('motor',))  # USAXS.a2rp
m2rp = EpicsMotor('9idcLAX:pi:c0:m2', name='m2rp', labels=('motor',))  # USAXS.m2rp
msrp = EpicsMotor('9idcLAX:pi:c0:m3', name='msrp', labels=('motor',))  # USAXS.msrp
asrp = EpicsMotor('9idcLAX:pi:c0:m4', name='asrp', labels=('motor',))  # USAXS.asrp
un36 = EpicsMotor('9idcLAX:xps:c0:m1', name='un36', labels=('motor',))  # unused36
un37 = EpicsMotor('9idcLAX:xps:c0:m2', name='un37', labels=('motor',))  # unused37
mst = EpicsMotor('9idcLAX:xps:c0:m3', name='mst', labels=('motor',))
ast = EpicsMotor('9idcLAX:xps:c0:m4', name='ast', labels=('motor',))
msr = EpicsMotor('9idcLAX:xps:c0:m5', name='msr', labels=('motor',))
asr = EpicsMotor('9idcLAX:xps:c0:m6', name='asr', labels=('motor',))
un42 = EpicsMotor('9idcLAX:xps:c0:m7', name='un42', labels=('motor',))  # unused42
un43 = EpicsMotor('9idcLAX:xps:c0:m8', name='un43', labels=('motor',))  # unused43
ar = EpicsMotor('9idcLAX:aero:c0:m1', name='ar', labels=('motor',))
un45 = EpicsMotor('9idcLAX:mxv:c1:m1', name='un45', labels=('motor',))
un46 = EpicsMotor('9idcLAX:mxv:c1:m2', name='un46', labels=('motor',))
un47 = EpicsMotor('9idcLAX:mxv:c1:m3', name='un47', labels=('motor',))
un48 = EpicsMotor('9idcLAX:mxv:c1:m4', name='un48', labels=('motor',))
un49 = EpicsMotor('9idcLAX:mxv:c1:m5', name='un49', labels=('motor',))
un50 = EpicsMotor('9idcLAX:mxv:c1:m6', name='un50', labels=('motor',))
un51 = EpicsMotor('9idcLAX:mxv:c1:m7', name='un51', labels=('motor',))
un52 = EpicsMotor('9idcLAX:mxv:c1:m8', name='un52', labels=('motor',))
ay = EpicsMotor('9idcLAX:aero:c1:m1', name='ay', labels=('motor',))
dy = EpicsMotor('9idcLAX:aero:c2:m1', name='dy', labels=('motor',))
# Macro Motor: SpecMotor(mne='en', config_line='55', macro_prefix='kohzuE') # read_mode=7
InbMS = EpicsMotor('9ida:m43', name='InbMS', labels=('motor',))  # MonoSl_inb
OutMS = EpicsMotor('9ida:m44', name='OutMS', labels=('motor',))  # MonoSl_out
TopMS = EpicsMotor('9ida:m45', name='TopMS', labels=('motor',))  # MonoSl_top
BotMS = EpicsMotor('9ida:m46', name='BotMS', labels=('motor',))  # MonoSl_bot
mr = EpicsMotor('9idcLAX:aero:c3:m1', name='mr', labels=('motor',))
c0 = ScalerCH('9idcLAX:vsc:c0', name='c0', labels=('detectors',))
c0.select_channels(None)
sec = c0.channels.chan01.s
I0 = c0.channels.chan02.s
I00 = c0.channels.chan03.s
upd2 = c0.channels.chan04.s
trd = c0.channels.chan05.s
I000 = c0.channels.chan06.s
```

</details>
