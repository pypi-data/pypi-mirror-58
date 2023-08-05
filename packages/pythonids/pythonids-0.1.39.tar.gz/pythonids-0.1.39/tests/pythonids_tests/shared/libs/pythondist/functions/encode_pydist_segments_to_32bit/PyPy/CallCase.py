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

    def testCase011(self):
        res = pythonids.pythondist.encode_pydist_segments_to_32bit(
            category='python',
            dist='pypy',
            distrel=(5, 8, 0),
            disttype=(2, 7),
            )
        resx = pythonids.pythondist.PYE_PYDIST_PYPY580
        self.assertEqual(res, resx)
        
    def testCase020(self):
        res = pythonids.pythondist.encode_pydist_segments_to_32bit(
            category='python',
            dist='pypy',
            distrel=(6, 0, 0),
            disttype=(2, 7),
            )
        resx = pythonids.pythondist.PYE_PYDIST_PYPY60027
        self.assertEqual(res, resx)

    def testCase025(self):
        res = pythonids.pythondist.encode_pydist_segments_to_32bit(
            category='python',
            dist='pypy',
            distrel=(6, 0, 0),
            disttype=(3, 5),
            )
        resx = pythonids.pythondist.PYE_PYDIST_PYPY60035
        self.assertEqual(res, resx)

    def testCase030(self):
        res = pythonids.pythondist.encode_pydist_segments_to_32bit(
            category='python',
            dist='pypy',
            distrel=(7, 0, 0),
            disttype=(3, 6),
            )
        resx = pythonids.pythondist.PYE_PYDIST_PYPY70036
        self.assertEqual(res, resx)


if __name__ == '__main__':
    unittest.main()
