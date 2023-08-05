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
import pythonids.pythondist
from pythonids.pythondist import PYE_PYTHON, PYE_CPYTHON_NAME, PYE_PYTHON27, PYE_CPYTHON


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)        
        self.maxDiff = None

    def testCase010(self):
        pp = pythonids.pythondist.PythonDist(
            category=PYE_PYTHON
        )         
        self.assertEqual(pp.category, PYE_PYTHON)

    def testCase020(self):
        pp = pythonids.pythondist.PythonDist(
            disttype=PYE_PYTHON27,
        )         
        self.assertEqual(pp.disttype, PYE_PYTHON27)

    def testCase030(self):
        pp = pythonids.pythondist.PythonDist(
            dist=PYE_CPYTHON
        )         
        self.assertEqual(pp.dist, PYE_CPYTHON)

    def testCase040(self):
        pp = pythonids.pythondist.PythonDist(
            distrel=PYE_PYTHON27
        )         
        self.assertEqual(pp.distrel, PYE_PYTHON27)


if __name__ == '__main__':
    unittest.main()
