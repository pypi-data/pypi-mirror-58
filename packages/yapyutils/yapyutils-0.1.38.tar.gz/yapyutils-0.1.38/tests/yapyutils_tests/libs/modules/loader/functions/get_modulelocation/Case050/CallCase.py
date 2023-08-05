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

from testdata.yapyutils_testdata import mypath
from yapyutils.modules.loader import get_modulelocation, load_module 



class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        sys.path.insert(0, mypath) 
        self.maxDiff = None

    def testCase010(self):
        impname, imppathname = get_modulelocation(
            '.subpackage300.submodule1', mypath, ('testpackage/subpackage3/subpackage30',))
        
        self.assertEqual(impname, "testpackage.subpackage3.subpackage30.subpackage300.submodule1")
        self.assertTrue(imppathname.endswith(
            os.path.join("testpackage","subpackage3","subpackage30","subpackage300","submodule1.py")))
        


if __name__ == '__main__':
    unittest.main()
