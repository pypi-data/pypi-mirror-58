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
import sys

from pythonids.pythondist import PYE_PYTHON, \
    PYE_CPYTHON, PYDIST_DATA, PYDIST
    
from pythonids.pythondist import _encode_disttype_bitmask
from testdata.pythonids_testdata import _fetch_pydist_to_32bit


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)        
        self.maxDiff = None

    def testCase010(self):
            
        self.assertEqual(
            PYDIST_DATA.disttype,
            _encode_disttype_bitmask(*sys.version_info[:2])
        )
        


if __name__ == '__main__':
    unittest.main()
