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


try:
    from rdbg.start import start_remote_debug     # load a slim bootstrap module for stage-0
    start_remote_debug()                          # check whether –rdbg option is present, if so accomplish bootstrap
except:
    pass

import unittest

import sys

import pythonids.pythondist
from pythonids.pythondist import _encode_distrel_bitmask, \
    PYE_CPYTHON, PYE_IPYTHON, PYE_JYTHON, PYE_PYPY, PYE_IRONPYTHON
from testdata.pythonids_testdata import _fetch_pydist_to_32bit


class CallUnits(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def testCase010(self):
        dist = _fetch_pydist_to_32bit()

        if dist == PYE_PYPY:

            # e.g. '2.7.13 (c925e73810367cd960a32592dd7f728f436c125c, Dec 14 2017, 12:47:11)\n[PyPy 5.8.0 with GCC 7.2.1 20170915 (Red Hat 7.2.1-2)]'
            import re

            _c = sys.version
            _cprep = re.findall(r'.*PyPy *([^ ]*) .*$', _c, re.MULTILINE)  # @UndefinedVariable
            distrel_tuple = tuple(int(x) for x in _cprep[0].split('.'))
            distrel = _encode_distrel_bitmask(*distrel_tuple)

    
            pp = pythonids.pythondist.PythonDist()
            pp.scan()         

            self.assertEqual(
                pp.distrel,
                distrel
            )

        elif dist in (PYE_CPYTHON, PYE_IRONPYTHON, ):
            pp = pythonids.pythondist.PythonDist()
            pp.scan()         

            self.assertEqual(
                pp.distrel,
                _encode_distrel_bitmask(*sys.version_info[:3])
            )

        elif dist in (PYE_IPYTHON, ):
            distrel = _encode_distrel_bitmask(int(x) for x in sys.modules['IPython'].__version__.split('.'))
            
            pp = pythonids.pythondist.PythonDist()
            pp.scan()         

            self.assertEqual(
                pp.distrel,
                distrel
            )
            
        elif dist in (PYE_JYTHON, ):
            import platform
            
            distrel = _encode_distrel_bitmask(*(int(x) for x in platform.python_version_tuple()[0:3]))
            
            pp = pythonids.pythondist.PythonDist()
            pp.scan()         

            self.assertEqual(
                pp.distrel,
                distrel
            )

        else:
            self.assertTrue(
                False,
                "Platform not supported"
                )


if __name__ == '__main__':
    unittest.main()
