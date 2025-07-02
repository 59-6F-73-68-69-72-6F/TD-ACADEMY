# STYLE ***************************************************************************
# content = assignment style
#
# date    = 2025-07-01
# email   = rudyleti@gmail.com
#************************************************************************************

import os
from inspect import currentframe

# original: logging.init.py

def findCaller(self):
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.

    On some versions of IronPython, currentframe() returns None if
    IronPython isn't run with -X:Frames.
    """
    
    f = currentframe()
    if f is not None:
        f = f.f_back
    
    rv = "(unknown file)", 0, "(unknown function)"

    while hasattr(f, "f_code"):
        co = f.f_code
        filename = os.path.normcase(co.co_filename)
        
        if filename == _srcfile:
            f = f.f_back
            continue
        
        rv = (co.co_filename, f.f_lineno, co.co_name)
        break
    return rv
