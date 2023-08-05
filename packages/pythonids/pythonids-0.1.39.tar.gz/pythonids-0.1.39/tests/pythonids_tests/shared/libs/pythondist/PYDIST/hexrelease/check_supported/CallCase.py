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
import platform

class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)        
        self.maxDiff = None
        
        self.impl = platform.python_implementation()


    def testCase010(self):
        self.assertTrue(self.impl in ('CPython', 'PyPy', 'Jython', 'IronPython', ), "Python distribution not supported:" + str(self.impl))
        # CPython == (CPython, IPython)
        

if __name__ == '__main__':
    unittest.main()
