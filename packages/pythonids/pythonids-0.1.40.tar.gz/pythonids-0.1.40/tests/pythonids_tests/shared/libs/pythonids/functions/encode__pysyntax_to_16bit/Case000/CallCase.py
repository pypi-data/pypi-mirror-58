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

import pythonids


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase010(self):
        res = pythonids.encode_pysyntax_to_16bit(3, 6, 5)
        resx = pythonids.PYV365
        self.assertEqual(res, resx)
        
    def testCase020(self):
        res = pythonids.encode_pysyntax_to_16bit(3, 5,)
        resx = pythonids.PYV35
        self.assertEqual(res, resx)

    def testCase030(self):
        res = pythonids.encode_pysyntax_to_16bit(2, 7,)
        resx = pythonids.PYV27
        self.assertEqual(res, resx)

    def testCase040(self):
        res = pythonids.encode_pysyntax_to_16bit(3, 7, 2,)
        resx = pythonids.PYV372
        self.assertEqual(res, resx)

if __name__ == '__main__':
    unittest.main()
