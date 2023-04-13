# Python `__init__.py` files

In Python, a file directory becomes a Python
[*package*](https://realpython.com/python-modules-packages/) by the presence of
a `__init__.py` file.  Even if this file is empty, the directory (which must
adhere to Python naming rules) can be used with the `import` statement if the
package is on the [search
path](https://realpython.com/python-modules-packages/#the-module-search-path).

The `instrument` package relies on these `__init__.py` files to control the
import of Python objects (variables and functions) for command-line use in
interactive Bluesky sessions.  These files *expose* various content (while
hiding unnecessary content) for the command-line user.  Within any python file,
you may find a declaration of `__all__`, a list of the Python object names to be
exposed from that Python file.

The order of loading files is controlled by the lines in the `__init__.py` file.
In some cases, the sequence of loading is important.

## `instrument/collection.py`

This file is used to start the `instrument` package for interactive use with
data collection.  It can be used with both IPython console sessions and Jupyter
Notebook & JupyterLab sessions.

```py
from instrument.collection import *
```

## `instrument/queueserver.py`

This file is used to start the `instrument` package for background server use with
remote data collection.  It is used by a bluesky-queueserver process.

```py
from instrument.queueserver import *
```
