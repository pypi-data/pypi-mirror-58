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

from pythonids.pythondist import PYE_DIST, PYE_DISTREL, PYE_DISTREL_MAJOR, PYE_DISTREL_MINOR, PYE_DISTREL_MICRO


class CallUnits(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None
    def testCase020(self):
        self.assertEqual(PYE_DISTREL, 0x0003ffff)

    def testCase030(self):
        self.assertEqual(PYE_DISTREL_MAJOR, 0x0003f000)

    def testCase040(self):
        self.assertEqual(PYE_DISTREL_MINOR, 0x00000fc0)

    def testCase050(self):
        self.assertEqual(PYE_DISTREL_MICRO, 0x0000003f)


if __name__ == '__main__':
    unittest.main()
