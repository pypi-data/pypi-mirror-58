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

from pythonids import PYV3, PYV36, PYV362, PYV365, PYV366, PYV367, PYV368, PYV369


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase010(self):
        self.assertEqual(PYV3, 24576)

    def testCase020(self):
        self.assertEqual(PYV36, 26112)

    def testCase030(self):
        self.assertEqual(PYV362, 26114)

    def testCase040(self):
        self.assertEqual(PYV365, 26117)

    def testCase050(self):
        self.assertEqual(PYV366, 26118)

    def testCase060(self):
        self.assertEqual(PYV367, 26119)

    def testCase070(self):
        self.assertEqual(PYV368, 26120)

    def testCase080(self):
        self.assertEqual(PYV369, 26121)


if __name__ == '__main__':
    unittest.main()
