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
        resx = """category            = python
disttype            = 
dist                = 
distrel             = 
hexrelease          = 0x80000000
"""
#         print("4TEST: \n" + str(pp))         
#         print("4TEST: \n" + str(resx))         
        self.assertEqual(str(pp), resx)

    def testCase020(self):
        pp = pythonids.pythondist.PythonDist(
            disttype=PYE_PYTHON27,
        )         
        resx = """category            = python
disttype            = python2.7
dist                = 
distrel             = 
hexrelease          = 0xa3800000
"""
#         print("4TEST: \n" + str(pp))         
#         print("4TEST: \n" + str(resx))         
        self.assertEqual(str(pp), resx)

    def testCase030(self):
        pp = pythonids.pythondist.PythonDist(
            dist=PYE_CPYTHON
        )         
        resx = """category            = python
disttype            = 
dist                = cpython
distrel             = 
hexrelease          = 0x80040000
"""
#         print("4TEST: \n" + str(pp))         
#         print("4TEST: \n" + str(resx))         
        self.assertEqual(str(pp), resx)

    def testCase040(self):
        pp = pythonids.pythondist.PythonDist(
            distrel=pythonids.pythondist._encode_distrel_bitmask(*pythonids.decode_pysyntax_16bit_to_tuple(pythonids.PYV27))
        )         
        resx = """category            = python
disttype            = 
dist                = 
distrel             = 2.7.0
hexrelease          = 0x800021c0
"""
#         print("4TEST: \n" + str(pp))         
#         print("4TEST: \n" + str(resx))         
        self.assertEqual(str(pp), resx)



if __name__ == '__main__':
    unittest.main()
