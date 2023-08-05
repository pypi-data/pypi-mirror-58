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

import pythonids.pythondist


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase010(self):
        res = pythonids.pythondist._encode_distrel_bitmask(
            2, 7, 15,
            )
        resx = 0x21cf
        self.assertEqual(res, resx)
        
    def testCase020(self):
        res = pythonids.pythondist._encode_distrel_bitmask(
            3, 5, 3,
            )
        resx = 0x3143
        self.assertEqual(res, resx)

    def testCase030(self):
        res = pythonids.pythondist._encode_distrel_bitmask(
            3, 6, 5,
            )
        resx = 0x3185
        self.assertEqual(res, resx)

    def testCase040(self):
        res = pythonids.pythondist._encode_distrel_bitmask(
            3, 7, 1,
            )
        resx = 0x31c1
        self.assertEqual(res, resx)

    def testCase050(self):
        res = pythonids.pythondist._encode_distrel_bitmask(
            3, 7, 2,
            )
        resx = 0x31c2
        self.assertEqual(res, resx)

if __name__ == '__main__':
    unittest.main()
