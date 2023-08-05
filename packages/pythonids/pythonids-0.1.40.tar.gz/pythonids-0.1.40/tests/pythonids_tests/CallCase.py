from __future__ import absolute_import
"""Test PyUnit environment. This is a required call-dummy only.
"""
__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.0'
__uuid__ = "5624dc41-775a-4d17-ac42-14a0d5c41d1a"


try:
    from rdbg.start import start_remote_debug
    start_remote_debug()
except:
    pass

import unittest

if __name__ == '__main__':
    unittest.main()
