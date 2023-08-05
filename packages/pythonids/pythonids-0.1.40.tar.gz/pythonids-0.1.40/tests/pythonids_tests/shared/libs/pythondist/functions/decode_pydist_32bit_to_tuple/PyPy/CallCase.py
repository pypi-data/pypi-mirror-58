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
        res = pythonids.pythondist.decode_pydist_32bit_to_tuple(
            0xa3a05200
            )
        resx = (
            pythonids.pythondist.PYE_PYTHON,
            pythonids.pythondist.PYE_PYTHON27,
            pythonids.pythondist.PYE_PYPY,
            pythonids.pythondist._encode_distrel_bitmask(5, 8, 0,),
        )
#         print("4TEST:" + str(res))
#         print("4TEST:" + str(resx))
        self.assertEqual(res, resx)
        pass
        
    def testCase020(self):
        res = pythonids.pythondist.decode_pydist_32bit_to_tuple(
            0xa3a06000
            )
        resx = (
            pythonids.pythondist.PYE_PYTHON,
            pythonids.pythondist.PYE_PYTHON27,
            pythonids.pythondist.PYE_PYPY,
            pythonids.pythondist._encode_distrel_bitmask(6, 0, 0,),
        )
#         print("4TEST:" + str(res))
#         print("4TEST:" + str(resx))
        self.assertEqual(res, resx)
        pass

    def testCase030(self):
        res = pythonids.pythondist.decode_pydist_32bit_to_tuple(
            0xb2a06000
            )
        resx = (
            pythonids.pythondist.PYE_PYTHON,
            pythonids.pythondist.PYE_PYTHON35,
            pythonids.pythondist.PYE_PYPY,
            pythonids.pythondist._encode_distrel_bitmask(6, 0, 0,),
        )
#         print("4TEST:" + str(res))
#         print("4TEST:" + str(resx))
        self.assertEqual(res, resx)
        pass


if __name__ == '__main__':
    unittest.main()

