"""
Common test data
================
Common data for 'UseCases' and 'tests'. Refer to the package by PYTHONPATH.
The global variable 'testdata.pythonids.mypath' provides the pathname into 'testdata'.
"""

import os
mypath = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))

curcygdrive = 'cygdrive'


import platform
from pythonids.pythondist import dist2num
def _fetch_pydist_to_32bit():
    
    #FIXME: lacks IPython
    return dist2num[platform.python_implementation()]


