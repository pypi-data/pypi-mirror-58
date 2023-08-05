# -*- coding: utf-8 -*-
"""Utility for pretty printout of pythonids.
"""
from __future__ import absolute_import
from __future__ import print_function

import sys

try:
    #
    # optional remote debug only
    #
    from rdbg import start        # load a slim bootstrap module
    start.start_remote_debug()    # check whether '--rdbg' option is present, if so accomplish bootstrap

except SystemExit:
    #
    # exit immediately after any type of help display - or any other intentional sys.exit()
    # print optional traceback
    #  1. after exit > 0
    #  2. if 3x --rdbg-self 
    #
    _s = sys.exc_info()
    import rdbg
    if rdbg.my_dbg_self >2 or _s[1] > 0:
        print()
        import traceback
        print(traceback.print_exc())
    print()
    sys.exit(_s[1])

except:
    pass

import pythonids
import pythonids.pythondist



__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"


_debug = 0
_verbose = 0


def ppretty_pythonids():
    """Prints runtime parameters of the current Python syntax and implementation.  
    """
    
    sys.stderr.write('\n')
        
    sys.stderr.write("\n#*\n#* pythonids:\n#*\n")
    sys.stderr.write(
        "%-20s= %s\n" % (
            "Python syntax",
            str(pythonids.decode_pysyntax_16bit_to_str(pythonids.PYVxyz))
        )
    )
    sys.stderr.flush()
    sys.stderr.write(str(pythonids.pythondist.PYDIST_DATA))
    sys.stderr.write('\n')
    sys.stderr.flush()

    sys.stderr.write('\n\n')
    sys.stderr.flush()

def main():
    ppretty_pythonids()
    
if __name__ in ("__main__", "pythonids.prettypyids"):
    main()

sys.exit(0)
