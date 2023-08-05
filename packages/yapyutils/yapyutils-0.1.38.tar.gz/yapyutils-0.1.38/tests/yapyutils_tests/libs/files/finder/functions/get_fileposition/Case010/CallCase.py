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

    def testCase020(self):

        #(rfpname, toppath=None, spaths=None, hook=None,):
        
        imppathname, impname = get_filesysposition(
            'dir00/file1.txt', 
            os.path.dirname(__file__), 
            (os.path.dirname(__file__) + os.sep + 'dir0/dir01/dir010',),
            ) 
        self.assertEqual(impname, "file1.txt")
        self.assertTrue(imppathname.endswith("dir0/dir00"))


if __name__ == '__main__':
    unittest.main()
