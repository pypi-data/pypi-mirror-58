from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__ = "5624dc41-775a-4d17-ac42-14a0d5c41d1a"

__docformat__ = "restructuredtext en"


try:
    from rdbg.start import start_remote_debug    # load a slim bootstrap module
    start_remote_debug()                         # check whether '--rdbg' option is present, if so accomplish bootstrap
except:
    pass

import unittest

import pythonids.pythondist


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase010(self):
        res = pythonids.pythondist._encode_disttype_bitmask(
            2, 7,
            )
        self.assertEqual(res, pythonids.pythondist.PYE_PYTHON27)
        
    def testCase020(self):
        res = pythonids.pythondist._encode_disttype_bitmask(
            3, 7,
            )
        self.assertEqual(res, pythonids.pythondist.PYE_PYTHON37)


if __name__ == '__main__':
    unittest.main()
