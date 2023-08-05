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
from pythonids.pythondist import PythonDist, \
    _encode_disttype_str_bitmask, \
    _encode_distrel_str_bitmask, \
    PYE_CPYTHON_NAME, PYE_CPYTHON, PYE_PYTHON


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)        
        self.maxDiff = None

    def testCase010(self):
        pp = PythonDist(
            "python",
            _encode_disttype_str_bitmask("2.7"),
            "cpython",
            _encode_distrel_str_bitmask("2.7"),
        )         
        self.assertEqual(pp.category, PYE_PYTHON)

    def testCase020(self):
        pp = PythonDist(
            "python",
            _encode_disttype_str_bitmask("2.7"),
            "cpython",
            _encode_distrel_str_bitmask("2.7"),
        )         
        self.assertEqual(pp.dist, PYE_CPYTHON)

if __name__ == '__main__':
    unittest.main()
