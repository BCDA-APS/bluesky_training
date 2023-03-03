# user directory

- [user directory](#user-directory)
  - [About files in `user` directory](#about-files-in-user-directory)
  - [`%run` - Load \& Run a file](#run---load--run-a-file)
  - [Access symbols in the IPython session namespace](#access-symbols-in-the-ipython-session-namespace)

## About files in `user` directory

Each file should be written like a standard Python module, including all the imports necessary to support the code.

To use symbols from the user command shell (a.k.a., the *IPython session namespace*):
you'll need to add them.  Look at the section below for these instructions.

Usually, your code should take any necessary symbols as arguments (args) or
optional keyword arguments (kwargs).

## `%run` - Load & Run a file

To load a Python module (filename without the traling `.py` extension) from this
directory into ipython use a command such as this example:

```bash
In [1]: %run -im user.quick_hello
Hello!
```

**Tip**: The `%run` IPython magic command is comparable to SPEC's `qdo` command.

**Caution**:
    If you add or modify symbols in the user's command shell (IPython namespace) and those symbols are used in your file (`user/quick_hello.py` as the example shows), you must repeat the `%run` command (above) to load those changes.

Alternatively, this equivalent command loads and runs `quick_hello.py` file:

```bash
In [2]: %run -i user/quick_hello.py
Hello!
```

## Access symbols in the IPython session namespace

Add this code block at the top of the file, before anything else:

```py
# get all the symbols from the IPython shell
import IPython
globals().update(IPython.get_ipython().user_ns)
logger.info(__file__)
```
