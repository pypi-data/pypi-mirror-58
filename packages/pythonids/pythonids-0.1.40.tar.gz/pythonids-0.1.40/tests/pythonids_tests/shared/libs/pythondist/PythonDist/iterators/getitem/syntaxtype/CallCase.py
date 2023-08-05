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
        if PYDIST & pythonids.pythondist.PYE_SYNTAXTYPE != pythonids.pythondist.PYE_PYTHON27:
            self.skipTest("other dist")
        
        pp = pythonids.pythondist.PythonDist(
            dist=pythonids.pythondist.PYE_PYTHON27
            )
        pp.scan()
        self.assertEqual(
            pp['disttype'],
            pythonids.pythondist.PYDIST_DATA.disttype
        )

    def testCase020(self):
        if PYDIST & pythonids.pythondist.PYE_SYNTAXTYPE != pythonids.pythondist.PYE_PYTHON35:
            self.skipTest("other dist")
        
        pp = pythonids.pythondist.PythonDist(
            dist=pythonids.pythondist.PYE_PYTHON35
            )
        pp.scan()
        self.assertEqual(
            pp['disttype'],
            pythonids.pythondist.PYDIST_DATA.disttype
        )

    def testCase030(self):
        if PYDIST & pythonids.pythondist.PYE_SYNTAXTYPE != pythonids.pythondist.PYE_PYTHON36:
            self.skipTest("other dist")
        
        pp = pythonids.pythondist.PythonDist(
            dist=pythonids.pythondist.PYE_PYTHON36
            )
        pp.scan()
        self.assertEqual(
            pp['disttype'],
            pythonids.pythondist.PYDIST_DATA.disttype
        )

    def testCase040(self):
        if PYDIST & pythonids.pythondist.PYE_SYNTAXTYPE != pythonids.pythondist.PYE_PYTHON37:
            self.skipTest("other dist")
        
        pp = pythonids.pythondist.PythonDist(
            dist=pythonids.pythondist.PYE_PYTHON37
            )
        pp.scan()
        self.assertEqual(
            pp['disttype'],
            pythonids.pythondist.PYDIST_DATA.disttype
        )


if __name__ == '__main__':
    unittest.main()
