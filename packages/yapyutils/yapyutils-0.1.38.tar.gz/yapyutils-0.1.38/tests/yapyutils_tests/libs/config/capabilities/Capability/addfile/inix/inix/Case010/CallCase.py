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

from yapydata.datatree.synini import DataTreeINI, YapyDataINIError
from yapydata.datatree.synjson import DataTreeJSON, YapyDataJSONError
from yapydata.datatree.synxml import DataTreeXML, YapyDataXMLError
from yapydata.datatree.synyaml import DataTreeYAML, YapyDataYAMLError

from yapyutils.config.capabilities import Capability


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
 #       sys.path.insert(0, mypath) 
        self.maxDiff = None

    def testCase010(self):
        _cap = Capability()
        _cap.readfile(os.path.dirname(__file__) + os.sep + 'data.inix')
        _cap.addfile(os.path.dirname(__file__) + os.sep + 'data1.inix')

        with open(os.path.dirname(__file__) + os.sep + 'resx.json') as data_file:
            _res = DataTreeJSON()
            _res.import_data(os.path.dirname(__file__) + os.sep + 'resx')
            resx = _res.data

#         print("4TEST:_cap.data = <%s>" % (str(_cap.data)))
#         print("4TEST:resx      = <%s>" % (str(resx)))

        self.assertEqual(_cap.data, resx)


if __name__ == '__main__':
    unittest.main()
