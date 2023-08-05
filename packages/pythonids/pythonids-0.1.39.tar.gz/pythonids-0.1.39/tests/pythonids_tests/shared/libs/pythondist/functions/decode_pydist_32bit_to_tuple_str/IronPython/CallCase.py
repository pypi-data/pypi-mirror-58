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
        res = pythonids.pythondist.decode_pydist_32bit_to_tuple_str(
            pythonids.pythondist.PYE_PYDIST_IRONPYTHON277
            )
        resx = pythonids.pythondist.PyDistStr(
            pythonids.pythondist.PYE_PYTHON_NAME,
            pythonids.pythondist.num2name[pythonids.pythondist.PYE_PYTHON27],
            pythonids.pythondist.PYE_IRONPYTHON_NAME,
            '2.7.7',
        )
        print("4TEST:" + str(res))
        print("4TEST:" + str(resx))
        self.assertEqual(res, resx)
        pass
        
    def testCase020(self):
        res = pythonids.pythondist.decode_pydist_32bit_to_tuple_str(
            pythonids.pythondist.PYE_PYDIST_IRONPYTHON279
            )
        resx = pythonids.pythondist.PyDistStr(
            pythonids.pythondist.PYE_PYTHON_NAME,
            pythonids.pythondist.num2name[pythonids.pythondist.PYE_PYTHON27],
            pythonids.pythondist.PYE_IRONPYTHON_NAME,
            '2.7.9',
        )
#         print("4TEST:" + str(res))
#         print("4TEST:" + str(resx))
        self.assertEqual(res, resx)
        pass


if __name__ == '__main__':
    unittest.main()
