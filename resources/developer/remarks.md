# Remarks

2021-05-27: Bluesky Case Studies

Note the Bluesky Office Hours every Wednesday afternoon at 2:30 - 3:30 on MS Teams.  No set format to this, People come with a question or contribution, answers as possible.
https://tinyurl.com/BlueskyOfficeHours

https://teams.microsoft.com/l/meetup-join/19%3af9523bff12844888b25bd7d49a5fad56%40thread.skype/1616020172420?context=%7b%22Tid%22%3a%220cfca185-25f7-49e3-8ae7-704d5326e285%22%2c%22Oid%22%3a%22cd8e408e-f2c5-4590-937e-df9d934296ad%22%7d

## notebook: custom_plan

- What is pycat?
- What is "md" in the `up_down_once()` plan of the custom_plan notebook?
- How is logging handled?  How to get the logger object?
- Use `%pycat .logs/ipython_logger.log` to see the log file. It is OS-independent.
- Another suggestion: make adding log messages the 1st exercise item so all of the demos provide more feedback.
- What is bps?
- What is stage_sigs?
- Use `from inspect import signature` to document the call signature of functions.
- How is real-time plotting handled?
- How to count against a monitor instead of time?
- How is `kind` used?
- Use `%%time` at the start of slow cells to show how long the execution took to complete.
- How does the RE reset things if a scan is stopped early. How to configure reset/cleanup?

## notebook: databroker_analysis

- How are the catalogs named and why?  What is possible?
- How to export data to users?
  - tiled?
  - custom data writing callback
- 16BM & 16ID will probably need to support their own file format for export
- 16BM & 16ID : How to provide bluesky to a beam line through a VM?
  - I'm working with a VM.  It may be possible but I need to learn more how to make this available as a service to the beam line.
  - That will make our Tri-Lab guys very happy
  - Tr-Lab = LANL, LLNL and Sandia
- In notebook cells, append `;` to suppress output of the object representation
- Challenge: provide custom visualization for live or saved data
  - bokeh: https://docs.bokeh.org/en/latest/index.html
- What is `primary`?  (data streams)
- What is `plan_name` in the metadata?  How is this defined?
- How to organize using a unique scan ID?

## notebook: basic-motor-scaler-scan

- Challenge: modify tscan() to accept the same positioner args as bp.scan() AND the ct=1 kwarg
- Challenge: modify tscan() to restore the original stage_sigs before it was modified

## General

- A general question (if time allows): GUI vs CLI, which category is the BlueSky more compatible with? BS doesn't seem to provide SPEC like CLI environment (contained environment with limited number of pre-defined commands) nor have any intention to be used for existing GUI frames (e.g., MEDM or caQtDM). From user's perspective, they would not expect they should learn much of Python jargons to run their experiment at different beamlines. As a beamline scietist, what should I prepare to provide users with a consistent, robust interface for their experiment? Every single user experriment is to be customized on BluSky platform?

    - Most typical case at a beamline with users in-house is command-line session from linux terminal.  Graphical data visualization provided in separate windows.  Additional beam line GUI (caQtDM, MEDM, other) is expected.  As with any user-facing environment, you probably want to limit the "vocabulary" that users must learn.  Many instruments maintain a "cheat sheet" for their users, expressed in terms known best to their user community.  It is typical for a beamline to present the user with customized plans that package the standard plans with other actions for the instrument.  Metadata, control of X-ray wavelength, slits, mirrors, shutter, and sample position are often part of that custom plan that simplify the vocabulary for the user.  That's the part you would maintain.  The jargon of the custom plan would be under your control.  Also, you maintain the ophyd devices that interface to your control system.

- RunEngine streams: https://blueskyproject.io/bluesky/tutorial.html#other-supplemental-data
- Is there a GUI for bluesky?
- Teach us to write plans all the time.  No blocking examples.

- About data coming from an area detector. Is the area detector saving data to disk using its own save file functionality and Bluesky just saves the filepaths in the catalogue. Or, is Bluesky grabbing the 2-D data from the image PV directly and saving it in its own catalogue. Or, both ways are possible?
  - It's the first one.  Area detector is configured with a file writer (such as HDF5) to write the file.  Bluesky only records the file path and name and frame number.
  - How is the choice made between writing data outside of bluesky and passing the data into bluesky for writing?  When the data volume would delay the RunEngine significantly (still a judgement call), then write externally and inform the RunEngine about the path, name and frame number.  Bluesky will need to know how to locate & read that image (example: the HDF5 writer writes in NeXus format and bluesky has a handler for that).
- how many blueskys can run at  the same time at a beamline? 
  - There is no limitation on the number of bluesky sessions running on the same workstation, account or subnet.
- How can we make background monitoring processes?  Wants to run a sample heater process separate from standard collection process.
  - You can write all the commands necessary in a python file that executes as a background job.  Typically, this is ophyd code but it is possible to use the RunEngine in this way.  The bluesky_snapshot tool is one _example_ of such a tool.

    https://apstools.readthedocs.io/en/latest/applications/snapshot.html#bluesky-snapshot

- How can it be logged into the same experiment data base?
  - I have not tested it but believe that mongodb can handle more than one writer to the same database and collection (mongo terms) at the same time.  Every document from the RunEngine is given a uid (unique identifier) and those uids are linked back to the run's start document.  This allows a mix of simultaneous writers.
  - In such cases, interactive clients should be careful when requesting the "last run" from the catalog: `cat[-1]` as this result may be unpredictable.
