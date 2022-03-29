"""
configure matplotlib for console or notebook session
MUST be run BEFORE other initializations
"""


def isnotebook():
    """
    see: https://stackoverflow.com/a/39662359/1046449
    """
    try:
        from IPython import get_ipython

        _ipython = get_ipython()
        if _ipython is not None:
            shell = _ipython.__class__.__name__
            return shell == "ZMQInteractiveShell"
        return False
        #    return True   # Jupyter notebook or qtconsole
        # elif shell == 'TerminalInteractiveShell':
        #    return False  # Terminal running IPython
        # else:
        #    return False  # Other type (?)
    except NameError:
        return False  # Probably standard Python interpreter


if isnotebook():
    from .notebook import *
else:
    from .console import *
