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
from pythonids import PYV3, PYV35

PYV3 =    24576  # encode_pysyntax_to_16bit(3,)
PYV32 =   25088  # encode_pysyntax_to_16bit(3, 2)
PYV33 =   25344  # encode_pysyntax_to_16bit(3, 3)
PYV34 =   25600  # encode_pysyntax_to_16bit(3, 4)
PYV35 =   25856  # encode_pysyntax_to_16bit(3, 5)
PYV36 =   26112  # encode_pysyntax_to_16bit(3, 6)
PYV362 =  26114  # encode_pysyntax_to_16bit(3, 6, 2)
PYV365 =  26117  # encode_pysyntax_to_16bit(3, 6, 5)
PYV366 =  26118  # encode_pysyntax_to_16bit(3, 6, 6)
PYV367 =  26119  # encode_pysyntax_to_16bit(3, 6, 7)
PYV368 =  26120  # encode_pysyntax_to_16bit(3, 6, 8)
PYV369 =  26121  # encode_pysyntax_to_16bit(3, 6, 9)
PYV37 =   26368  # encode_pysyntax_to_16bit(3, 7, 0)
PYV371 =  26369  # encode_pysyntax_to_16bit(3, 7, 1)
PYV372 =  26370  # encode_pysyntax_to_16bit(3, 7, 2)
PYV373 =  26371  # encode_pysyntax_to_16bit(3, 7, 3)
PYV374 =  26372  # encode_pysyntax_to_16bit(3, 7, 4)
PYV375 =  26373  # encode_pysyntax_to_16bit(3, 7, 5)
PYV376 =  26374  # encode_pysyntax_to_16bit(3, 7, 6)
PYV38 =   26624  # encode_pysyntax_to_16bit(3, 8, 0)


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None

    def testCase010(self):
        self.assertEqual(PYV3, 24576)

    def testCase020(self):
        self.assertEqual(PYV32, 25088)

    def testCase030(self):
        self.assertEqual(PYV33, 25344)

    def testCase040(self):
        self.assertEqual(PYV34, 25600  )

    def testCase050(self):
        self.assertEqual(PYV35, 25856)

    def testCase060(self):
        self.assertEqual(PYV36, 26112)
    
    def testCase070(self):
        self.assertEqual(PYV362, 26114)
    
    def testCase080(self):
        self.assertEqual(PYV365, 26117)
    
    def testCase090(self):
        self.assertEqual(PYV366, 26118)
    
    def testCase100(self):
        self.assertEqual(PYV367, 26119)
    
    def testCase110(self):
        self.assertEqual(PYV368, 26120)
    
    def testCase120(self):
        self.assertEqual(PYV369, 26121)

    def testCase130(self):
        self.assertEqual(PYV37, 26368)

    def testCase140(self):
        self.assertEqual(PYV371, 26369)

    def testCase150(self):
        self.assertEqual(PYV372, 26370)

    def testCase160(self):
        self.assertEqual(PYV373, 26371)

    def testCase170(self):
        self.assertEqual(PYV374,  26372 )

    def testCase180(self):
        self.assertEqual(PYV375, 26373)

    def testCase190(self):
        self.assertEqual(PYV376, 26374)


    def testCase3000(self):
        self.assertEqual(PYV38, 26624)


if __name__ == '__main__':
    unittest.main()
