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
  
    def testCase020(self):
        var4debug = pythonids.pythondist.PYDIST & pythonids.pythondist.PYE_DIST in (
                    pythonids.pythondist.PYE_CIRCUITPYTHON,
                    pythonids.pythondist.PYE_CPYTHON,
                    pythonids.pythondist.PYE_CYTHON,
                    pythonids.pythondist.PYE_IPYTHON,
                    pythonids.pythondist.PYE_IRONPYTHON,
                    pythonids.pythondist.PYE_JYTHON,
                    pythonids.pythondist.PYE_MICROPYTHON,
                    pythonids.pythondist.PYE_PYPY,
                )

        self.assertTrue(var4debug)


if __name__ == '__main__':
    unittest.main()
