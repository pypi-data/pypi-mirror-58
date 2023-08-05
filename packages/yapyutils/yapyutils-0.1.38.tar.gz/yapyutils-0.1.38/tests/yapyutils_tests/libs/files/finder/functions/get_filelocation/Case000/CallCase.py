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
from yapyutils.files.finder import get_filelocation 



class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        sys.path.insert(0, mypath) 
        self.maxDiff = None

    def testCase010(self):
        imppathname, impname = get_filelocation('dir0/dir00/file1.txt', (mypath + os.sep + 'files',))
        self.assertEqual(impname, "file1.txt")
        self.assertTrue(imppathname.endswith(os.path.normpath('/files/dir0/dir00')))
        
    def testCase020(self):
        imppathname, impname = get_filelocation('file1.txt', (mypath + os.sep + 'files',)) 
        self.assertEqual(impname, "file1.txt")
        self.assertTrue(imppathname.endswith("files"))


if __name__ == '__main__':
    unittest.main()
