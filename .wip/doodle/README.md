# Demonstration: call shell command & wait for finish

Demonstrate how to launch a shell command and wait for it to finish.

This involves setting a command and receiving two different values
(_stdout_ and _stderr_).  An `ophyd.Signal` is for setting and reading
one value.  The `ophyd.Device` can provide the multiple values needed.

A working example is provided in this directory as a Jupyter notebook.
An HTML version of the finished notebook is also provided so you can
view it right away.

In the HTML file, skip forward to section "4.-As-ophyd.Device" (link:
file::///demo_doodle.html#4.-As-ophyd.Device).  The previous sections
work through why the ophyd support has to be a Device and not a Signal.
Section 5 runs this with the bluesky `count() plan.

To simulate a linux command to be run, a shell script (doodle.sh) was
created that prints a 5 second countdown to stdout (the terminal
console).

**Files**

file | description
:--- | :---
`demo_doodle.ipynb` | Jupyter notebook
`doodle.sh` | Example Linux program (a bash shell script)
`demo_doodle.html` | HTML rendering of the Jupyter notebook
