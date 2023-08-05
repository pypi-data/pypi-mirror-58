# -*- coding: utf-8 -*-
"""Distribute 'yapyutils', a collection of common required low-level utility libraries for Python.

Additional local options for this *setup.py* module:
   --no-install-requires: 
       Suppresses installation dependency checks,
       requires appropriate PYTHONPATH.

   --offline: 
       Sets online dependencies to offline, or ignores online
       dependencies.

"""
from __future__ import absolute_import
from __future__ import print_function

#
# setup extension modules -  pip install setuplib / pip install pysetuplib 
#
import os
import sys

import setuptools

if sys.version_info[:2] == (2, 7,):
    ModuleLoadError = ImportError
else:
    ModuleLoadError = ModuleNotFoundError  # @UndefinedVariable


__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__vers__ = [0, 1, 38,]
__version__ = "%02d.%02d.%03d"%(__vers__[0],__vers__[1],__vers__[2],)
__release__ = "%d.%d.%d" % (__vers__[0], __vers__[1], __vers__[2],) + '-rc0'
__status__ = 'beta'


# required for various interfaces, thus just do it
_mypath = os.path.dirname(os.path.abspath(__file__))
"""Path of this file."""
sys.path.insert(0, os.path.abspath(_mypath))


_name='yapyutils'
"""package name"""

__pkgname__ = "yapyutils"
"""package name"""

_packages = [
    'yapyutils', 
    'yapyutils/config', 
    'yapyutils/files', 
    'yapyutils/help', 
    'yapyutils/modules', 
    'yapyutils/releases', 
]

_install_requires = []
"""prerequired non-standard packages"""

__no_install_requires = False
if '--no-install-requires' in sys.argv:
    __no_install_requires = True
    sys.argv.remove('--no-install-requires')

__offline = False
if '--offline' in sys.argv:
    __offline = True
    __no_install_requires = True
    sys.argv.remove('--offline')


if __no_install_requires:
    print("#")
    print("# Changed to offline mode, ignore install dependencies completely.")
    print("# Requires appropriate PYTHONPATH.")
    print("# Ignored dependencies are:")
    print("#")
    for ir in _install_requires:
        print("#   " + str(ir))
    print("#")
    _install_requires = []


#
# see setup.py for remaining parameters
#
setuptools.setup(
    author=__author__,
    author_email=__author_email__,
    description="The 'yapyutils' package provides miscellaneous low-level Python utilities.",
    download_url="https://sourceforge.net/projects/yapyutils/files/",
    entry_points={
        'console_scripts': [
            'prettyenv = yapyutils.prettyenv:pprint_environment',
            'prettypath = yapyutils.prettypath:pprint_path',
            'prettypypath = yapyutils.prettypypath:pprint_pypath',
        ]
    },
    install_requires=_install_requires,
    license=__license__,
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    name=_name,
    packages=_packages,
    url='https://sourceforge.net/projects/yapyutils/',
    version="%d.%d.%d"%(__vers__[0],__vers__[1],__vers__[2],),
    zip_safe=False,
)

sys.exit(0)

