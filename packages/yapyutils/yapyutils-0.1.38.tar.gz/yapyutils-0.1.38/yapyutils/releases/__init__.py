# -*- coding: utf-8 -*-
"""*yapyutils.releases* provides various low-level *Python* utilities for version and release numbering.
"""

from yapyutils import YapyUtilsError

import re


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"


_debug = 0
_verbose = 0


class YapyUtilsReleasesError(YapyUtilsError):
    """Subsystem *Releases*.
    """
    pass


def get_version_complete(version):
    """Checks and completes a version to the format. ::

        <major>.<minor>.<micro>

    Args:
        version:
            Arbitrary but valid version. ::

                version := [[[<major>].<minor>].<micro>]
                 
                major :=[.][0-1]+
                minor := [.][0-1]+
                micro := [.][0-1]+
                     
                default := *__main__*

    Returns:
        Displays the complete version.

    Raises:
        YapyUtilsReleasesError

        pass-through

    """
    try:
        _p, _v0, _v1, _v2, _err, _pp = re.split(
            r'^([0-9]+)[.]{0,1}([0-9]+){0,1}[.]{0,1}([0-9]+){0,1}([^0-9]*)$',
            str(version))
    except ValueError as e:
        e.args = (
            e.args[0] 
            + "\nErroneous version, requires 1-3 digits, e.g: 11[.22[.333]] - got: '%s'" % (
                str(version)), ) + e.args[1:]
        raise e #+ SetupDocXError("Erroneous version, requires 1-3 digits, e.g: 11[.22[.333]]")
 
    if _err:
        raise YapyUtilsReleasesError('version requires numeric values: ' + str(version))
    if _v0 == None:
        _v0 = '0'
    if _v1  == None:
        _v1 = '0'
    if _v2 == None:
        _v2 = '0'
 
    return "%s.%s.%s" % (_v0, _v1, _v2)
