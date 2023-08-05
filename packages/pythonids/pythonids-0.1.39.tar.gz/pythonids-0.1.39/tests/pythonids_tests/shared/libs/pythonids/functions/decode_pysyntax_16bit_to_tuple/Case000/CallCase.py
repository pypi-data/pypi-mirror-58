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
        self.assertEqual(pythonids.decode_pysyntax_16bit_to_tuple(pythonids.PYV32), (3, 2, 0))

    def testCase020(self):
        self.assertEqual(pythonids.decode_pysyntax_16bit_to_tuple(pythonids.PYV362), (3, 6, 2))

if __name__ == '__main__':
    unittest.main()
