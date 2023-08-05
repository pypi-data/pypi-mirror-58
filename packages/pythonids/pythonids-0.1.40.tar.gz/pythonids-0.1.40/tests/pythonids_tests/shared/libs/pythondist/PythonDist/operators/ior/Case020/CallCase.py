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
            category=0,
            disttype=0,
            dist=0,
            distrel=pythonids.pythondist._encode_distrel_bitmask(2, 7, 1),
        )
        pp1 = pythonids.pythondist.PythonDist(
            distrel=pythonids.pythondist._encode_distrel_bitmask(1, 8, 2),
        )
        x = pp0.hexrelease | pp1.hexrelease
        pp0 |= pp1
        self.assertTrue(pp0 == x)
        pass
        

if __name__ == '__main__':
    unittest.main()
