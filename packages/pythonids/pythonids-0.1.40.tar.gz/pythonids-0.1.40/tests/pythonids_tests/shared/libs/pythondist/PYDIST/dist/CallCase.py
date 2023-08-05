from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__ = "5624dc41-775a-4d17-ac42-14a0d5c41d1a"

__docformat__ = "restructuredtext en"

import unittest
import platform

from pythonids.pythondist import PYE_PYTHON, \
    PYE_CPYTHON, PYDIST_DATA, PYDIST, \
    PYE_PYPY, PYE_IRONPYTHON, PYE_IPYTHON, PYE_JYTHON

from testdata.pythonids_testdata import _fetch_pydist_to_32bit


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)        
        self.maxDiff = None
        
        self.impl = platform.python_implementation()


    def testCase010(self):
        if self.impl in ('CPython', 'IPython'):  # CPython and IPython
            self.assertTrue(_fetch_pydist_to_32bit() in (PYE_CPYTHON, PYE_IPYTHON,))
            self.assertTrue(PYDIST_DATA.dist in (PYE_CPYTHON, PYE_IPYTHON,))
            pass

        elif self.impl == 'PyPy':
            self.assertEqual(_fetch_pydist_to_32bit(), PYE_PYPY)
            self.assertEqual(PYDIST_DATA.dist, PYE_PYPY)
            pass

        elif self.impl == 'IronPython':
            self.assertEqual(_fetch_pydist_to_32bit(), PYE_IRONPYTHON)
            self.assertEqual(PYDIST_DATA.dist, PYE_IRONPYTHON)
            pass

        elif self.impl == 'Jython':
            self.assertEqual(_fetch_pydist_to_32bit(), PYE_JYTHON)
            self.assertEqual(PYDIST_DATA.dist, PYE_JYTHON)
            pass

        else:
            raise("Platform not supported:" + str(self.impl))
        
        

if __name__ == '__main__':
    unittest.main()
