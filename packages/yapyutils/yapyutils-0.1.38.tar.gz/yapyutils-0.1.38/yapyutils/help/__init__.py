# -*- coding: utf-8 -*-
"""*yapyutils.help* provides various low-level *Python* utilities for runtime help information.
"""

from yapyutils import YapyUtilsError


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"


_debug = 0
_verbose = 0


class YapyUtilsHelpError(YapyUtilsError):
    """Subsystem *Help*.
    """
    pass



def usage(name):
    """Display docstring as help.
 
    Args:
        name:
            Name for the help title.
             
            default := *__main__*
             
    Returns:
        Displays the *docsting* of the modules and exists.
         
    Raises:
        pass-through
         
    """
    if name == '__main__':
        import pydoc
        print(pydoc.help(name))
    else:
        help(str(name))
