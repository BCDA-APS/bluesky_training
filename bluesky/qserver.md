# Introduction to the Bluesky Queueserver

work-in-progress: *very* basic notes for now

- [Introduction to the Bluesky Queueserver](#introduction-to-the-bluesky-queueserver)
  - [Run the queuserver](#run-the-queuserver)
    - [operations](#operations)
    - [diagnostics and testing](#diagnostics-and-testing)
  - [graphical user interface](#graphical-user-interface)

**IMPORTANT**:  When the queueserver starts, it **must** find only one `.py` file in this directory and it must find `instrument/` in the same directory.  Attempts to place the qserver files in a sub directory result in `'instrument/' directory not found` as queueserver starts.

## Run the queuserver

### operations

Run in a background screen session.

`./qserver.sh start`

Stop this with

`./qserver.sh stop`

### diagnostics and testing

`./qserver.sh run`

## graphical user interface

`queue-monitor &`

- connect to the server
- open the environment
- add tasks to the queue
- run the queue
- 
