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
        self.maxDiff = None

    def testCase010(self):
        pp = pythonids.pythondist.PythonDist(
            category=123, 
            disttype=234,
            dist=345,
            distrel=456,
        )
        pp.hexrelease = 567
        res = tuple(pp.values())
        resx = (123, 234, 345, 456, 567)
        self.assertEqual(res, resx)

    def testCase020(self):
        pp = pythonids.pythondist.PythonDist(
            category=123, 
            disttype=234,
            dist=345,
            distrel=456,
            forceall=True,
        )
        pp.hexrelease = 567
        res = tuple(pp.values())
        resx = (123, 234, 345, 456, 567, '', 0, 0, '', 0)
        self.assertEqual(res, resx)


if __name__ == '__main__':
    unittest.main()
