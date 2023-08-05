# -*- coding: utf-8 -*-
"""*yapyutils.modules.loader* provides module location and load as file.
"""
import sys
import os
import re

from yapyutils.modules import YapyUtilsModulesError
from pythonids import PYVxyz, PYV27X, PYV3X, PYV35Plus, decode_pysyntax_16bit_to_str


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"


class YapyUtilsLoaderError(YapyUtilsModulesError):
    """Module load error."""
    pass


_debug = 0
_verbose = 0


def get_modulelocation(mname, mbase=None, mpaths=None, **kargs):
    """"A very basic function for the detection of the absolute path and
    the relative module search-path-name for a given path of a module.
    The values are the same as would be present in *sys.modules*.
    Supports source modules as input only. 
    
    The *platformids* is a low-level library within the software stack. 
    The generic functions for the allocation of module sources and binaries
    are provided by *sourceinfo* [sourceinfo]_, which itself depends on
    the *platformids*. Thus *sourceinfo* could not be used in order to avoid
    circular dependencies. So implemented this function to keep *platformids*
    on lowest possible software-stack level only.
    
    Args:
        mname:
            The relative path of the module in dotted *Python* notation,
            without file suffix. ::
    
                mname := (
                     <dotted-module-name-str>
                   | <dotted-module-name-path-name-str>
                )

        mbase:
            Base for module search paths, filepath name with a trailing
            separator. :: 

                default := os.path.normpath(os.path.curdir + os.sep + '..' ) + os.sep

            The base path is used within the post-processing of the eventually matched
            path, thus has to be appropriate for all items in *mpaths*. 

       mpaths:
            List of module search paths relative to *mbase*:: 

                default := [
                   '',
                ]

            resulting in::

                default := [
                   mbase,
                ]

       kargs:
            permitrel: 
                Permit the return of relative module names within *mpath*.
                If *False* absolute only, which is actually relative to an existing
                search path entry in *sys.path*. ::

                    permitrel := (
                        True,       # returns a relative module name if within subtree
                        False       # returns in any case a module name relative to sys.path
                    )

                Sets relavive base to the default::

                    rbase = os.path.normpath(os.path.dirname(__file__) + os.sep + '..' + re.sub(r'[.]', os.sep, mname)) + os.sep

    Returns:
        Returns in case of a match the resulting entry within *sys.modules*::

            match -> (<relative-module-name>, <module-file-path-name>,)

        The default when no match occured is to rely on the more versatile
        search mechanism of the import implementation of the concrete 
        *Python* implementation for another final trial by the caller::

            default -> (<mname>, None,)

    Raises:
        PlatformIDsError
            'mbase' does not match 'mpaths'

        PlatformIDsPresentError
            missing 'mbase'

        pass-through

    """
    if mpaths == None:
        mpaths = ('',)

#     if mbase == None:
#         mbase = os.path.normpath(
#             os.path.abspath(os.path.curdir) + os.sep + '..' ) + os.sep

    assert(isinstance(mpaths, (list, tuple)))

    _permitrel = kargs.get('permitrel', False)
    rbase = kargs.get('rbase')

    _res = re.split(r'[.]', mname, maxsplit=1)
    if len(_res) == 1:
        _package = _relpath = ''
        _relname = _module = _res[0]
    else:
        _package = _res[0]
        _relname = _res[1]
        _relpath = re.sub(r'[.]', os.sep, _relname)
        _relpath, _module = os.path.split(_relpath)
        
    if mbase == None:
        for s in sys.path:
            if os.path.exists(s + os.sep + _package):
                mbase = s + os.sep + _package
                break
        else:
            raise YapyUtilsLoaderError(
                "Cannot find package dir: '" + str(_package) + "'")

    mbase = os.path.normpath(mbase) + os.sep

    if _permitrel and rbase == None:
        rbase = mbase + _relpath
    
    if mpaths == None:
        # default
        _mpaths = [
            mbase,
        ]

    elif mpaths and mpaths[0]:
        _mpaths = list(mpaths[:])
        
        # permit relative to mbase only
        for mi in range(len(_mpaths)):
            if os.path.isabs(_mpaths[mi]):
                continue
            _mpaths[mi] = os.path.normpath(mbase + os.sep + _mpaths[mi]) + os.sep

    elif not mpaths:
        raise YapyUtilsLoaderError("missing 'mpaths'")
    
    else:
        _mpaths = mpaths


    if _mpaths and not _mpaths[0].startswith(mbase):
        raise YapyUtilsLoaderError(
            "'mbase' does not match 'mpaths'\nmbase = %s\nmpaths[0] = %s" %(
                mbase, _mpaths[0]
                )
            )

    modfpath = ''
    for _p in _mpaths:
        modfpath = os.path.join(_p, _package, _relpath, _module) + '.py'
        if os.path.exists(modfpath):
            if _permitrel and modfpath.startswith(rbase):
                modname = re.sub(r'[/\\\\]', r'.', os.path.normpath(modfpath[len(rbase):]))[:-3]
                break
            
            _largest_match = ''
            for spx in sys.path:
                if os.path.normpath(mbase).startswith(os.path.normpath(spx)):
                    if len(_largest_match) < len(spx):
                        _largest_match = os.path.normpath(spx)

            if os.path.normpath(mbase) == _largest_match:
                modname = re.sub(r'[/\\\\]', r'.', modfpath[len(mbase):])[:-3]

            elif os.path.normpath(os.path.dirname(mbase)) == _largest_match:
                modname = re.sub(r'[/\\\\]', r'.', modfpath[len(os.path.dirname(mbase)) + 1:])[:-3]

            elif os.path.normpath(os.path.dirname(mbase[:-1])) == _largest_match:
                modname = re.sub(r'[/\\\\]', r'.', modfpath[len(os.path.dirname(mbase[:-1])) + 1:])[:-3]

            else:
                modname = re.sub(r'[/\\\\]', r'.', os.path.normpath(modfpath[len(_largest_match) + 1:]))[:-3]

            break        

    else:
        return(mname, None)

    return (modname, modfpath)



def load_module(importname, modfpath):
    """Loads the specified module by it's name and file system path.
    Provides a common interface for all supported platforms and Python
    implementations: *CPyhton*, *IPython*, *IronPython*, *Jython*, 
    and *PyPy*. For the syntaxversions *Python2.7* and *Python3*.
    
    Args:
        importname:
            The import name of the module in dotted path notation.
            The *importname* is registered in *sys.modules*.
          
        modfpath:
            The full file system path name. The *modfpath* is
            registered in *sys.modules*.
    
    Returns:
        The module object on success, else *None*.
    
    Raises:
        PlatformIDsError
      
        pass-through
    """
    _modx = None
    
    if sys.modules.get(importname):
        # already loaded - most likely a standard module

        #TODO: hopefully no counter for less common actual reload
        
        return sys.modules[importname]  # in case of failure want to see the exception
    
    elif PYV35Plus:  # PYVxyz >= PYV35: # Python 3.5+
        import importlib.util  # @UnresolvedImport
        spec = importlib.util.spec_from_file_location(importname, modfpath)  # @UndefinedVariable
        if spec:
            _modx = importlib.util.module_from_spec(spec)  # @UndefinedVariable
            spec.loader.exec_module(_modx)

    elif PYV3X:  # PYVxyz >= PYV33:  # Python 3.3 and 3.4
        from importlib.machinery import SourceFileLoader  # @UnresolvedImport
        _modx = SourceFileLoader(importname, modfpath).load_module()

    elif PYV27X:  # Python 2 - verified and released for 2.7 only, but don't block
        import imp  # @UnresolvedImport
        try:
            _modx = imp.load_source(importname, modfpath)

        except IOError:
            raise YapyUtilsLoaderError(
                "Missing platform module: %s: %s" %(
                    str(importname),
                    str(modfpath)
                    )
                )
    else:
            raise YapyUtilsLoaderError(
                "Syntax release not supported: %s" %(
                    str(decode_pysyntax_16bit_to_str(PYVxyz))
                    )
                )
        
    if _modx:
        sys.modules[importname] = _modx
        globals()[importname] = _modx
    
    return sys.modules[importname]  # in case of failure want to see the exception


def search_modulelocation(mname, mbases=None, mpaths=None, **kargs):
    """Similar to *get_modulelocation()*, but searches multiple
    bases - *mbases* vs. *base*. Internally calls *get_modulelocation*
    for each base.

    Args:
        mname:
            see *get_modulelocation()*

        mbases:
            A list of bases for the search of relative module 
            paths. :: 

                default := sys.path + os.path.curdir

        mpaths:
            see *get_modulelocation()*
    
        kargs:
            permitrel:
                see *get_modulelocation()*
    
    Returns:
        see *get_modulelocation()*
    
    Raises:
        see *get_modulelocation()*

    """
    if mbases == None:
        mbases = sys.path

    for _mbase in mbases:
        _f = get_modulelocation(mname, _mbase, mpaths)
        if _f:
            return _f
