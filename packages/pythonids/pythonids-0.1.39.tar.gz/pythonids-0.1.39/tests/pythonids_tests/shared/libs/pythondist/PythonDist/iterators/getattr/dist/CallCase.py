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

        var4debug = pythonids.pythondist.PYDIST & pythonids.pythondist.PYE_DIST in (
                    pythonids.pythondist.PYE_CPYTHON,
                    pythonids.pythondist.PYE_IPYTHON,
                    pythonids.pythondist.PYE_IRONPYTHON,
                    pythonids.pythondist.PYE_JYTHON,
                    pythonids.pythondist.PYE_PYPY,
                )

        self.assertTrue(var4debug)

    def testCase010(self):
        if PYDIST & pythonids.pythondist.PYE_DIST != PYE_CPYTHON:
            self.skipTest("other dist")
        pp = pythonids.pythondist.PythonDist(
            dist=PYE_CPYTHON
            )
        pp.scan()
        self.assertEqual(
            pp.dist,
            pythonids.pythondist.PYDIST_DATA.dist
        )

    def testCase020(self):
        if PYDIST & pythonids.pythondist.PYE_DIST != PYE_IPYTHON:
            self.skipTest("other dist")
        pp = pythonids.pythondist.PythonDist(
            dist=PYE_IPYTHON
            )
        pp.scan()
        self.assertEqual(
            pp.dist,
            pythonids.pythondist.PYDIST_DATA.dist
        )

    def testCase030(self):
        if PYDIST & pythonids.pythondist.PYE_DIST != PYE_IRONPYTHON:
            self.skipTest("other dist")
        pp = pythonids.pythondist.PythonDist(
            dist=PYE_IRONPYTHON
            )
        pp.scan()
        self.assertEqual(
            pp.dist,
            pythonids.pythondist.PYDIST_DATA.dist
        )

    def testCase040(self):
        if PYDIST & pythonids.pythondist.PYE_DIST != PYE_JYTHON:
            self.skipTest("other dist")
        pp = pythonids.pythondist.PythonDist(
            dist=PYE_JYTHON
            )
        pp.scan()
        self.assertEqual(
            pp.dist,
            pythonids.pythondist.PYDIST_DATA.dist
        )

    def testCase050(self):
        if PYDIST & pythonids.pythondist.PYE_DIST != PYE_PYPY:
            self.skipTest("other dist")
        pp = pythonids.pythondist.PythonDist(
            dist=PYE_PYPY
            )
        pp.scan()
        self.assertEqual(
            pp.dist,
            pythonids.pythondist.PYDIST_DATA.dist
        )

if __name__ == '__main__':
    unittest.main()
