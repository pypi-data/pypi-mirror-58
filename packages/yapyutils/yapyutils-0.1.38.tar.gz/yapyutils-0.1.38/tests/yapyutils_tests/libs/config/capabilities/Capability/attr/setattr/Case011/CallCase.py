from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"

import unittest
import os
import sys

#from testdata.yapyutils_testdata import mypath
from yapyutils.config.capabilities import Capability, YapyUtilsCapabilityError



class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
 #       sys.path.insert(0, mypath) 
        self.maxDiff = None

    def testCase010(self):
        _cap = Capability({'a': 1})
        self.assertRaises(YapyUtilsCapabilityError, _cap.__setattr__, 'data', [2])

    def testCase011(self):
        _cap = Capability({'a': 1})
        try:
            _cap.data = [2]
        except YapyUtilsCapabilityError as e:
            pass
        else:
            raise Exception("Should raise exception 'YapyUtilsCapabilityError'")


if __name__ == '__main__':
    unittest.main()
