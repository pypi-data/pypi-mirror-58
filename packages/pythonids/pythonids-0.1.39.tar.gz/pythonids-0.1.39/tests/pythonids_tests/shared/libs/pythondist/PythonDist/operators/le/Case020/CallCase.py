# -*- coding: utf-8 -*-
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


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase011(self):
        pp0 = pythonids.pythondist.PythonDist(
            category=pythonids.pythondist.PYE_PYTHON,
            disttype=pythonids.pythondist.PYE_PYTHON27,
            dist=pythonids.pythondist.PYE_CPYTHON,
            distrel=pythonids.pythondist._encode_distrel_bitmask(2, 7, 1),
        )
        pp1 = pythonids.pythondist.PythonDist(
            category=pythonids.pythondist.PYE_PYTHON,
            disttype=pythonids.pythondist.PYE_PYTHON27,
            dist=pythonids.pythondist.PYE_CPYTHON,
            distrel=pythonids.pythondist._encode_distrel_bitmask(2, 7, 15),
        )

        self.assertFalse(pp1 <= pp0)
        pass
        
    def testCase020(self):
        pp0 = pythonids.pythondist.PythonDist(
            category=pythonids.pythondist.PYE_PYTHON,
            disttype=pythonids.pythondist.PYE_PYTHON27,
            dist=pythonids.pythondist.PYE_CPYTHON,
            distrel=pythonids.pythondist._encode_distrel_bitmask(2, 6, 1),
        )
        pp1 = pythonids.pythondist.PythonDist(
            category=pythonids.pythondist.PYE_PYTHON,
            disttype=pythonids.pythondist.PYE_PYTHON27,
            dist=pythonids.pythondist.PYE_CPYTHON,
            distrel=pythonids.pythondist._encode_distrel_bitmask(2, 7, 1),
        )

        self.assertFalse(pp1 <= pp0)
        pass

    def testCase030(self):
        pp0 = pythonids.pythondist.PythonDist(
            category=pythonids.pythondist.PYE_PYTHON,
            disttype=pythonids.pythondist.PYE_PYTHON27,
            dist=pythonids.pythondist.PYE_CPYTHON,
            distrel=pythonids.pythondist._encode_distrel_bitmask(2, 7, 1),
        )
        pp1 = pythonids.pythondist.PythonDist(
            category=pythonids.pythondist.PYE_PYTHON,
            disttype=pythonids.pythondist.PYE_PYTHON27,
            dist=pythonids.pythondist.PYE_CPYTHON,
            distrel=pythonids.pythondist._encode_distrel_bitmask(3, 7, 1),
        )

        self.assertFalse(pp1 <= pp0)
        pass


if __name__ == '__main__':
    unittest.main()
