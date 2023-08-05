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
import sys

from pythonids.pythondist import PYE_PYTHON,  PYE_CATEGORY, \
    PYE_CPYTHON, PYDIST_DATA, PYDIST, \
    encode_pydist_segments_to_32bit, _encode_distrel_bitmask, \
    PYE_PYPY, PYE_IRONPYTHON, PYE_JYTHON
from testdata.pythonids_testdata import _fetch_pydist_to_32bit


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)        
        self.maxDiff = None
        
        self.impl = platform.python_implementation()

        self.implnum = _fetch_pydist_to_32bit()

        if self.impl == 'PyPy':  # CPython and IPython

            # e.g. '2.7.13 (c925e73810367cd960a32592dd7f728f436c125c, Dec 14 2017, 12:47:11)\n[PyPy 5.8.0 with GCC 7.2.1 20170915 (Red Hat 7.2.1-2)]'
            import re

            _c = sys.version
            _cprep = re.findall(r'.*PyPy *([^ ]*) .*$', _c, re.MULTILINE)  # @UndefinedVariable
            self.distrel_tuple = tuple(int(x) for x in _cprep[0].split('.'))
            self.distrel = _encode_distrel_bitmask(*self.distrel_tuple)
        
    def testCase020(self):
        if self.impl != 'PyPy':  # CPython and IPython
            self.skipTest("not PyPy")

        self.assertEqual(self.implnum, PYE_PYPY)
        self.assertEqual(self.implnum, PYDIST_DATA.dist)
        
    def testCase030(self):
        if self.implnum != PYE_PYPY:
            self.skipTest("not PyPy")

        hx = encode_pydist_segments_to_32bit(
            category='python',
            dist='pypy',
            distrel=self.distrel_tuple,
            disttype=(sys.version_info[0], sys.version_info[1]),
            )
        self.assertEqual(
            PYDIST_DATA.hexrelease,
            hx
        )
        pass

    def testCase040(self):
        if self.implnum != PYE_PYPY:
            self.skipTest("not PyPy")

        hx = encode_pydist_segments_to_32bit(
            dist='pypy',
            distrel=self.distrel_tuple,
            disttype=(sys.version_info[0], sys.version_info[1]),
            )
        self.assertEqual(
            PYDIST_DATA.hexrelease & (PYE_CATEGORY ^ 0xFFFFFFFF),
            hx
        )
        pass


if __name__ == '__main__':
    unittest.main()
