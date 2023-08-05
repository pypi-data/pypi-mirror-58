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
import sys

from pythonids.pythondist import PYE_PYTHON,  PYE_CATEGORY, \
    PYE_CPYTHON, PYDIST_DATA, PYDIST, \
    encode_pydist_segments_to_32bit, _encode_distrel_bitmask, \
    PYE_PYPY, PYE_IRONPYTHON, PYE_IPYTHON, PYE_JYTHON
from testdata.pythonids_testdata import _fetch_pydist_to_32bit


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)        
        self.maxDiff = None
        
        self.impl = platform.python_implementation()

        self.implnum = _fetch_pydist_to_32bit()
        
    def testCase020(self):
        if self.impl != 'IronPython':  # CPython and IPython
            self.skipTest("not IronPython")

        self.assertEqual(self.implnum, PYE_IRONPYTHON)
        self.assertEqual(self.implnum, PYDIST_DATA.dist)
        
    def testCase030(self):
        if self.implnum != PYE_IRONPYTHON:
            self.skipTest("not IronPython")

        hx = encode_pydist_segments_to_32bit(
            category='python',
            dist='ironpython',
            distrel=(sys.version_info[0], sys.version_info[1], sys.version_info[2], ),
            disttype=(sys.version_info[0], sys.version_info[1]),
            )
        self.assertEqual(
            PYDIST_DATA.hexrelease,
            hx
        )
        pass

    def testCase040(self):
        if self.implnum != PYE_IRONPYTHON:
            self.skipTest("not IronPython")

        hx = encode_pydist_segments_to_32bit(
            dist='ironpython',
            distrel=(sys.version_info[0], sys.version_info[1], sys.version_info[2], ),
            disttype=(sys.version_info[0], sys.version_info[1]),
            )
        self.assertEqual(
            PYDIST_DATA.hexrelease & (PYE_CATEGORY ^ 0xFFFFFFFF),
            hx
        )
        pass


if __name__ == '__main__':
    unittest.main()
