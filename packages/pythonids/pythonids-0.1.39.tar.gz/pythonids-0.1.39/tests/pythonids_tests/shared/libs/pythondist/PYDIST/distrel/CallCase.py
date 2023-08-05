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

from pythonids.pythondist import PYE_PYTHON, \
    PYE_CPYTHON, PYDIST_DATA, PYDIST, \
    PYE_PYPY, PYE_IRONPYTHON, PYE_IPYTHON, PYE_JYTHON

from pythonids.pythondist import _encode_distrel_bitmask

class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)        
        self.maxDiff = None
        
    def testCase010(self):
        if PYDIST_DATA.dist == PYE_CPYTHON:
            self.assertEqual(
                PYDIST_DATA.distrel,
                _encode_distrel_bitmask(*sys.version_info[:3])
            )
        
        elif PYDIST_DATA.dist == PYE_IPYTHON:
            # provided by the core module __version__
            distrel = _encode_distrel_bitmask(int(x) for x in sys.modules['IPython'].__version__.split('.'))
            self.assertEqual(
                PYDIST_DATA.distrel,
                distrel
            )
        
        elif PYDIST_DATA.dist == PYE_PYPY:
            # e.g. '2.7.13 (c925e73810367cd960a32592dd7f728f436c125c, Dec 14 2017, 12:47:11)\n[PyPy 5.8.0 with GCC 7.2.1 20170915 (Red Hat 7.2.1-2)]'
            import re

            _c = sys.version
            _cprep = re.findall(r'.*PyPy *([^ ]*) .*$', _c, re.MULTILINE)  # @UndefinedVariable
            distrel = _encode_distrel_bitmask(*(int(x) for x in _cprep[0].split('.')))

            self.assertEqual(
                PYDIST_DATA.distrel,
                distrel
            )

        elif PYDIST_DATA.dist == PYE_IRONPYTHON:
            #
            # The sys.version seems to be compatible to the python-syntax, but
            # in sync only with major and minor version.
            # The micro version seems to be independent from Python-Syntax/CPython.
            #
            self.assertEqual(
                PYDIST_DATA.distrel,
                _encode_distrel_bitmask(*sys.version_info[:3])
            )
            pass
        
        elif PYDIST_DATA.dist == PYE_JYTHON:
            # the distrel seems to be the same as sys.version
            # and platform.python_version_tuple / platform.python_version 
            #
            distrel = _encode_distrel_bitmask(*(int(x) for x in platform.python_version_tuple()[0:3]))
            
            self.assertEqual(
                PYDIST_DATA.distrel,
                distrel
            )

        else:
            raise("Platform not supported:" + str(PYDIST_DATA.dist))
        

if __name__ == '__main__':
    unittest.main()


