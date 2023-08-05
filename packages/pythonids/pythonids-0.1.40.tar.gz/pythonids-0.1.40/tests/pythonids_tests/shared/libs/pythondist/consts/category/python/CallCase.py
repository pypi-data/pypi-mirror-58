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

from pythonids.pythondist import PYE_PYTHON, PYE_PYTHON_PRETTY, PYE_PYTHON_NAME


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None

    def testCase010(self):
        self.assertEqual(PYE_PYTHON, 0x80000000)

    def testCase020(self):
        self.assertEqual(PYE_PYTHON_PRETTY, 'Python')

    def testCase030(self):
        self.assertEqual(PYE_PYTHON_NAME, 'python')



if __name__ == '__main__':
    unittest.main()
