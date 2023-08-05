# -*- coding: utf-8 -*-
"""*yapyutils.files.utilities* provides file helpers.
"""
import sys
import os
import re
import shutil
import tempfile

from yapyutils.files import YapyUtilsFilesError


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"


class YapyUtilsHelperError(YapyUtilsFilesError):
    pass


_debug = 0
_verbose = 0


def sed(filename, pattern, repl, flags=0):
    """Emulate *sed* for inplace replacements.
 
    Args:
        filename:
            Name of file for replacement.
         
        pattern:
            Regular expression for *re* to be replaced.
         
        repl:
            Replacement string.
             
        flags:
            Flags for *re*.
     
    Returns:
        None.
         
    Raises:
        pass-through
         
    """
    pattern_compiled = re.compile(pattern,flags)
    fname = os.path.normpath(filename)
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as ftmp:
        with open(fname) as src_file:
            for line in src_file:
                ftmp.write(pattern_compiled.sub(repl, line))
 
    shutil.copystat(fname, ftmp.name)
    shutil.move(ftmp.name, fname)

