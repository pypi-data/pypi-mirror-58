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

from pythonids import PYV3, PYV37, PYV371, PYV372, PYV373, PYV374, PYV375, PYV376 


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase010(self):
        self.assertEqual(PYV3, 24576)

    def testCase020(self):
        self.assertEqual(PYV37, 26368)

    def testCase030(self):
        self.assertEqual(PYV371, 26369)

    def testCase040(self):
        self.assertEqual(PYV372, 26370)

    def testCase050(self):
        self.assertEqual(PYV373, 26371)

    def testCase060(self):
        self.assertEqual(PYV374, 26372)

    def testCase070(self):
        self.assertEqual(PYV375, 26373)

    def testCase080(self):
        self.assertEqual(PYV376, 26374)


if __name__ == '__main__':
    unittest.main()
