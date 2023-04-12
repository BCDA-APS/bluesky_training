# Prepare Linux Workstation for Python Notebooks with Bluesky

revision: 2021-12-13

Without much explanation, these are the steps to prepare (install the various
components) a Linux workstation for these *Python Notebooks with Bluesky*.

These notebooks rely on docker containers providing 2 EPICS IOCs.

- [Prepare Linux Workstation for Python Notebooks with Bluesky](#prepare-linux-workstation-for-python-notebooks-with-bluesky)
  - [Docker VMs](#docker-vms)
    - [IOC `ad:` (Area Detector) simulates (2-D) area detector](#ioc-ad-area-detector-simulates-2-d-area-detector)
    - [IOC `gp:` (General Purpose) simulates motors, 1-D detectors, other tools](#ioc-gp-general-purpose-simulates-motors-1-d-detectors-other-tools)
  - [MongoDB server](#mongodb-server)
  - [Python (includes Bluesky tools)](#python-includes-bluesky-tools)
    - [Miniconda](#miniconda)
    - [Bluesky](#bluesky)
  - [IPython directory and profile](#ipython-directory-and-profile)
  - [Instrument Package](#instrument-package)
  - [Test](#test)
  - [Now, start to use Bluesky](#now-start-to-use-bluesky)

## Docker VMs

The EPICS VMs are managed from bash shell scripts.  Make a local directory for
starter scripts.  

    mkdir ~/bin
    # put in the PATH for this session
    export PATH=~/bin:${PATH}
    # put it in the PATH for new sessions
    echo "export PATH=~/bin:\${PATH}" >> ~/.bash_aliases

### IOC `ad:` (Area Detector) simulates (2-D) area detector

The docker image will download on first use.  Install the script to manage the area detector VM:

    cd ~/bin
    wget https://raw.githubusercontent.com/prjemian/epics-docker/main/resources/iocmgr.sh
    chmod +x iocmgr.sh

Start the `ad:` EPICS VM (_IOC_ in the EPICS-speaking world):

    iocmgr.sh start ADSIM ad

    # put in the PATH for this session
    export PATH=~/bin:${PATH}

Test that docker container `iocad` is running and provides its EPICS
IOC.  Use EPICS command (`caget`) within the container:

    user@localhost:~ $ docker exec iocad caget ad:cam1:Acquire
    ad:cam1:Acquire             Done

### IOC `gp:` (General Purpose) simulates motors, 1-D detectors, other tools

The docker image will download on first use.  Install the script to manage the area detector VM:

    cd ~/bin
    wget https://raw.githubusercontent.com/prjemian/epics-docker/main/resources/iocmgr.sh
    chmod +x iocmgr.sh

Start the `gp:` EPICS VM (_IOC_ in the EPICS-speaking world):

    iocmgr.sh start GP gp

Test that docker container `iocgp` is running and provides its EPICS
IOC.  Use EPICS command (`caget`) within the container:

    user@localhost:~ $ docker exec iocgp caget gp:UPTIME
    gp:UPTIME                     00:00:15

## MongoDB server

Install MongoDB Community Edition:
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

No additional configuration needed for this step.

## Python (includes Bluesky tools)

### Miniconda

see: https://github.com/BCDA-APS/use_bluesky/blob/main/install/miniconda.md#install-miniconda

    mkdir ~/Apps
    cd /tmp
    wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    bash miniconda.sh -b -p $HOME/Apps/miniconda
    # source "$HOME/miniconda/etc/profile.d/conda.sh"

### Bluesky

Install Bluesky into a custom conda environment using a YAML file (creates custom conda environment ``).
Start with a conda base environment activated:

    source $HOME/Apps/miniconda/bin/activate
    cd /tmp
    wget https://raw.githubusercontent.com/BCDA-APS/bluesky_instrument_training/main/environment.yml
    conda env create -f environment.yml
    conda activate class_2021_03

## IPython directory and profile

    ipython profile create --profile-dir=${HOME}/.ipython-bluesky bluesky

## Instrument Package

In the training workstation, clone the instrument package (for this training) from GitHub:

    cd ~/.ipython/profile_bluesky/startup
    git clone https://github.com/BCDA-APS/bluesky_instrument_training .

Make a shortcut to the bash shell script starter for bluesky sessions:

    cd ~/bin
    ln -s ~/.ipython/profile_bluesky/startup/blueskyStarter.sh ./blueskyClass.sh

Make a shortcut to the bash shell script starter for the IOC VMs:

    cd ~/bin
    ln -s ~/.ipython/profile_bluesky/startup/iocStarter.sh ./iocClass.sh

Install the databroker configuration for MongoDB:

    mkdir -p ~/.local/share/intake
    cp ~/.ipython/profile_bluesky/startup/bluesky_class.yml ~/.local/share/intake

## Test

Test that this works.  First, start the EPICS IOCs:

    cd /tmp
    iocClass.sh

<details>
<summary>Typical command output when starting IOCs:</summary>

Output from this command will be similar (not identical, long ID numbers will be
different, also, your session may show the images being download from docker
hub) to:

    stopping container iocgp ... iocgp
    removing container iocgp ... iocgp
    starting container iocgp ... d18df6acdd60d62a0a245d45ee346b885ae131449ead8b3be5b83c73680a9262
    changing xxx: to gp: in iocgp
    starting IOC iocgp ... docker exec iocgp iocxxx/softioc/xxx.sh start
    Starting xxx
    copy IOC iocgp to /tmp/docker_ioc/iocgp
    stopping container iocad ... iocad
    removing container iocad ... iocad
    starting container iocad ... c65c3994a0e1d5f1d81704a577ee8f72fe95d7125705928c3576992192c252d9
    starting IOC iocad ... docker exec iocad iocSimDetector/simDetector.sh start
    Starting simDetector
    copy IOC iocad to /tmp/docker_ioc/iocad
    changing 13SIM1: to ad: in iocad

</details>

Start Bluesky:

    cd /tmp
    blueskyClass.sh

That should start an IPython console session. With no errors.  

<details>
<summary>Typical output during startup</summary>

```
(base) prjemian@zap:/tmp$ blueskyClass.sh 
Python 3.8.5 (default, Sep  4 2020, 07:30:14) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.20.0 -- An enhanced Interactive Python. Type '?' for help.

IPython profile: bluesky
Activating auto-logging. Current session state plus future input saved.
Filename       : /tmp/.logs/ipython_console.log
Mode           : rotate
Output logging : True
Raw input log  : False
Timestamping   : True
State          : active
I Mon-14:49:34 - ############################################################ startup
I Mon-14:49:34 - logging started
I Mon-14:49:34 - logging level = 10
I Mon-14:49:34 - /home/prjemian/.ipython-bluesky/profile_bluesky/startup/instrument/collection.py
I Mon-14:49:34 - /home/prjemian/.ipython-bluesky/profile_bluesky/startup/instrument/mpl/console.py
I Mon-14:49:35 - bluesky framework
I Mon-14:49:35 - /home/prjemian/.ipython-bluesky/profile_bluesky/startup/instrument/framework/check_python.py
I Mon-14:49:35 - /home/prjemian/.ipython-bluesky/profile_bluesky/startup/instrument/framework/check_bluesky.py
I Mon-14:49:35 - /home/prjemian/.ipython-bluesky/profile_bluesky/startup/instrument/framework/initialize.py
I Mon-14:49:36 - /home/prjemian/.ipython-bluesky/profile_bluesky/startup/instrument/framework/metadata.py
I Mon-14:49:36 - /home/prjemian/.ipython-bluesky/profile_bluesky/startup/instrument/framework/callbacks.py
I Mon-14:49:36 - writing to SPEC file: /tmp/20210222-144936.dat
I Mon-14:49:36 -    >>>>   Using default SPEC file name   <<<<
I Mon-14:49:36 -    file will be created when bluesky ends its next scan
I Mon-14:49:36 -    to change SPEC file, use command:   newSpecFile('title')
I Mon-14:49:36 - /home/prjemian/.ipython-bluesky/profile_bluesky/startup/instrument/devices/area_detector.py
I Mon-14:49:36 - /home/prjemian/.ipython-bluesky/profile_bluesky/startup/instrument/devices/calculation_records.py
I Mon-14:49:38 - /home/prjemian/.ipython-bluesky/profile_bluesky/startup/instrument/devices/ioc_stats.py
I Mon-14:49:38 - /home/prjemian/.ipython-bluesky/profile_bluesky/startup/instrument/devices/motors.py
I Mon-14:49:38 - /home/prjemian/.ipython-bluesky/profile_bluesky/startup/instrument/devices/noisy.py
I Mon-14:49:38 - /home/prjemian/.ipython-bluesky/profile_bluesky/startup/instrument/devices/scaler.py
I Mon-14:49:39 - /home/prjemian/.ipython-bluesky/profile_bluesky/startup/instrument/devices/shutter.py
I Mon-14:49:39 - /home/prjemian/.ipython-bluesky/profile_bluesky/startup/instrument/plans/peak_finder_example.py
```

</details>

<details>
<summary>Show what objects are defined</summary>

```python
In [1]: listobjects()
Out[1]: 
=========== ================================ ============== ===================
name        class                            PV (or prefix) label(s)           
=========== ================================ ============== ===================
I0          EpicsSignalRO                    gp:scaler1.S2  counter channel    
I00         EpicsSignalRO                    gp:scaler1.S6  counter channel    
I000        EpicsSignalRO                    gp:scaler1.S5  counter channel    
adsimdet    SimDetector_V34                  ad:            area_detector      
calcouts    UserCalcoutDevice                gp:                               
calcs       UserCalcsDevice                  gp:                               
dcm         MyKohzu                          gp:                               
diode       EpicsSignalRO                    gp:scaler1.S4  counter channel    
fourc       FourCircle                       gp:                               
gp_stats    IocInfoDevice                    gp:                               
m1          MyEpicsMotor                     gp:m1          motor              
m10         MyEpicsMotor                     gp:m10         motor              
m11         MyEpicsMotor                     gp:m11         motor              
m12         MyEpicsMotor                     gp:m12         motor              
m13         MyEpicsMotor                     gp:m13         motor              
m14         MyEpicsMotor                     gp:m14         motor              
m15         MyEpicsMotor                     gp:m15         motor              
m16         MyEpicsMotor                     gp:m16         motor              
m2          MyEpicsMotor                     gp:m2          motor              
m3          MyEpicsMotor                     gp:m3          motor              
m4          MyEpicsMotor                     gp:m4          motor              
m7          MyEpicsMotor                     gp:m7          motor              
m8          MyEpicsMotor                     gp:m8          motor              
m9          MyEpicsMotor                     gp:m9          motor              
noisy       EpicsSignalRO                    gp:userCalc1   detectors simulator
scaler1     ScalerCH                         gp:scaler1     detectors scalers  
scint       EpicsSignalRO                    gp:scaler1.S3  counter channel    
shutter     SimulatedApsPssShutterWithStatus                shutters           
sim4c       SimulatedE4CV                                                      
simk4c      SimulatedK4CV                                                      
simk6c      SimulatedK6C                                                       
sixc        SixCircle                        gp:                               
slit1       Optics2Slit2D_HV                 gp:Slit1                          
temperature MyPvPositioner                   gp:userCalc8                      
timebase    EpicsSignalRO                    gp:scaler1.S1  counter channel    
=========== ================================ ============== ===================
```

</details>

<details>
<summary><tt>%wa</tt>: Show all motor positions (and other info, too)</summary>

```python
In [2]: %wa
area_detector
  Local variable name                    Ophyd name (to be recorded as metadata)
  adsimdet                               adsimdet                              

motor
  Positioner                     Value       Low Limit   High Limit  Offset     
  m1                             0.0         -32000.0    32000.0     0.0        
  m10                            0.0         -32000.0    32000.0     0.0        
  m11                            0.0         -32000.0    32000.0     0.0        
  m12                            0.0         -32000.0    32000.0     0.0        
  m13                            0.0         -32000.0    32000.0     0.0        
  m14                            0.0         -32000.0    32000.0     0.0        
  m15                            0.0         -32000.0    32000.0     0.0        
  m16                            0.0         -32000.0    32000.0     0.0        
  m2                             0.0         -32000.0    32000.0     0.0        
  m3                             0.0         -32000.0    32000.0     0.0        
  m4                             0.0         -32000.0    32000.0     0.0        
  m7                             0.0         -32000.0    32000.0     0.0        
  m8                             0.0         -32000.0    32000.0     0.0        
  m9                             0.0         -32000.0    32000.0     0.0        

  Local variable name                    Ophyd name (to be recorded as metadata)
  m1                                     m1                                    
  m10                                    m10                                   
  m11                                    m11                                   
  m12                                    m12                                   
  m13                                    m13                                   
  m14                                    m14                                   
  m15                                    m15                                   
  m16                                    m16                                   
  m2                                     m2                                    
  m3                                     m3                                    
  m4                                     m4                                    
  m7                                     m7                                    
  m8                                     m8                                    
  m9                                     m9                                    

detectors
  Local variable name                    Ophyd name (to be recorded as metadata)
  noisy                                  noisy                                 
  scaler1                                scaler1                               

scalers
  Local variable name                    Ophyd name (to be recorded as metadata)
  scaler1                                scaler1                               

counter
  Local variable name                    Ophyd name (to be recorded as metadata)
  I0                                     I0                                    
  diode                                  diode                                 
  scaler1.channels.chan01.s              timebase                              
  scaler1.channels.chan02.s              I0                                    
  scaler1.channels.chan03.s              scint                                 
  scaler1.channels.chan04.s              diode                                 
  scint                                  scint                                 
  timebase                               timebase                              

channel
  Local variable name                    Ophyd name (to be recorded as metadata)
  I0                                     I0                                    
  diode                                  diode                                 
  scaler1.channels.chan01.s              timebase                              
  scaler1.channels.chan02.s              I0                                    
  scaler1.channels.chan03.s              scint                                 
  scaler1.channels.chan04.s              diode                                 
  scint                                  scint                                 
  timebase                               timebase                              

shutters
  Local variable name                    Ophyd name (to be recorded as metadata)
  shutter                                shutter                               

```

</details>

Start a Jupyter lab session:

    cd /tmp
    blueskyClass.sh lab

This will take about a minute to start a Jupyter server, start a web browser,
and then the Jupyter lab session.  Open the
[`describe_instrument.ipynb`](describe_instrument.ipynb) notebook and run it to
see output similar to the console session (example shown below).

## Now, start to use Bluesky

See the quick-reference [Guide: First Steps with
Bluesky](https://github.com/BCDA-APS/use_bluesky/blob/main/first_steps_guide.md)
for the first commands to use.
