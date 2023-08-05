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
from yapyutils.files.finder import get_filesysposition



class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        sys.path.insert(0, mypath) 
        self.maxDiff = None

    def testCase010(self):
        _c = os.getcwd()
        os.chdir(os.path.dirname(__file__))
        imppathname, impname = get_filesysposition(
            'dir0/dir00/file1.txt', 
            os.path.dirname(__file__),
            )
        os.chdir(os.path.dirname(_c))
        
        self.assertEqual(impname, "file1.txt")
        self.assertTrue(imppathname.endswith(os.path.normpath('/dir0/dir00')))
        pass


if __name__ == '__main__':
    unittest.main()
