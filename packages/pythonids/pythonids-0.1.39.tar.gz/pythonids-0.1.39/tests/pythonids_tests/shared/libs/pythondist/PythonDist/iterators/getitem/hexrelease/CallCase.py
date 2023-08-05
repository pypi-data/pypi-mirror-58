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

import sys

import pythonids
import pythonids.pythondist
from pythonids.pythondist import PythonDist, PYDIST, PYE_PYTHON, \
    PYE_CPYTHON, PYE_CYTHON, PYE_IPYTHON, PYE_JYTHON, PYE_PYPY, \
    PYE_IRONPYTHON


class CallUnits(unittest.TestCase):


    def setUp(self):
        self.maxDiff = None

    def testCase010(self):
        pp = pythonids.pythondist.PythonDist()
        pp.scan()         
        hx = pp.get_hexrelease()
        self.assertEqual(
            pp['hexrelease'],
            hx
        )

    def testCase011(self):
        pp = pythonids.pythondist.PythonDist()
        pp.scan()         
        self.assertEqual(
            pp['hexrelease'],
            PYDIST
        )

if __name__ == '__main__':
    unittest.main()
