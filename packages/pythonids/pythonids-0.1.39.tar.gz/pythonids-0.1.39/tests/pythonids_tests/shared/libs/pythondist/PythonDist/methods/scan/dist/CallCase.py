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
from pythonids.pythondist import _encode_disttype_bitmask, PYE_PYTHON, \
    PYE_CPYTHON, PYE_CYTHON, PYE_IPYTHON, PYE_JYTHON, PYE_PYPY, \
    PYE_IRONPYTHON
from testdata.pythonids_testdata import _fetch_pydist_to_32bit


class CallUnits(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

        self.assertTrue(
            _fetch_pydist_to_32bit() in (PYE_CPYTHON, PYE_IPYTHON, PYE_IRONPYTHON, PYE_JYTHON, PYE_PYPY),
            "Platform not supported"
            )

    def testCase010(self):
        if _fetch_pydist_to_32bit() != PYE_CPYTHON:
            self.skipTest('other platform') 
        pp = pythonids.pythondist.PythonDist()
        pp.scan()         
        self.assertEqual(pp.dist, PYE_CPYTHON)
        
    def testCase030(self):
        if _fetch_pydist_to_32bit() != PYE_IPYTHON:
            self.skipTest('other platform') 
        pp = pythonids.pythondist.PythonDist()         
        pp.scan()         
        self.assertEqual(pp.dist, PYE_IPYTHON)

    def testCase040(self):
        if _fetch_pydist_to_32bit() != PYE_IRONPYTHON:
            self.skipTest('other platform') 
        pp = pythonids.pythondist.PythonDist()         
        pp.scan()         
        self.assertEqual(pp.dist, PYE_IRONPYTHON)

    def testCase050(self):
        if _fetch_pydist_to_32bit() != PYE_JYTHON:
            self.skipTest('other platform') 
        pp = pythonids.pythondist.PythonDist()         
        pp.scan()         
        self.assertEqual(pp.dist, PYE_JYTHON)

    def testCase060(self):
        if _fetch_pydist_to_32bit() != PYE_PYPY:
            self.skipTest('other platform') 
        pp = pythonids.pythondist.PythonDist()         
        pp.scan()         
        self.assertEqual(pp.dist, PYE_PYPY)


if __name__ == '__main__':
    unittest.main()
