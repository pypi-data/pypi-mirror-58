# -*- coding: utf-8 -*-
"""*yapyutils.files.finder* provides file locations.
"""
import sys
import os
import re
import fnmatch

from yapyutils.files import YapyUtilsFilesError


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"


class YapyUtilsFinderError(YapyUtilsFilesError):
    pass


_debug = 0
_verbose = 0


def splitfile(fpname):
    """Splits filename from it's pathname.
    
    Args:
        fpname:
            The file path name to be split.
            
    Returns:
        The splitted file path name::

            ret := (<pathname>, <filename>)

        In case of directory input::

            ret := (<pathname>, '')
        
    Raises:
        YapyUtilsFinderError
        
        pass-through
        
    """
    if not os.path.exists(fpname):
        raise YapyUtilsFinderError('requires existing node: ' + str(fpname))
    if os.path.isfile(fpname):
        return os.path.split(fpname)
    return (fpname, '')


def get_filelocation(fname, spaths=None):
    """A very basic function for the detection of the absolute path and
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
        fname:
            The relative path of the module in dotted *Python* notation, without
            file suffix.
    
             .. parsed-literal::
    
                mname := (
                     <dotted-module-name-str>
                   | <dotted-module-name-path-name-str>
                )
    
        spaths:
            List of search paths, 
    
             .. parsed-literal::
    
                default := sys.path + os.environ['PATH'].split(os.pathsep) 
    
    
    Returns:
        Returns in case of a match the resulting entry within *sys.modules*:
    
          .. parsed-literal::
    
             match -> (<abs-file-path>, <file-name>,)
       
        The default when no match occured is to rely on the more versatile
        search mechanism of the import implementation of the concrete 
        *Python* implementation for another final trial by the caller:
       
          .. parsed-literal::
    
             default -> ('', <fime-name>,)
    
    Raises:
        PlatformIDsError
            'mbase' does not match 'mpaths'
       
        PlatformIDsPresentError
            missing 'mbase'
       
        pass-through
    """
    if os.path.isabs(fname):
        if os.path.exists(fname):
            return os.path.split(fname)
        return ('', '')
    
    elif spaths == None:
        #  switch to (syspath + PATH) by default
        for s in ( os.getcwd(),) + sys.path + os.environ['PATH'].split(os.pathsep):
            if os.path.exists(s + os.sep + fname):
                return os.path.split(s + os.sep + fname)
        else:
            raise YapyUtilsFinderError("Cannot find file: '" + str(fname) + "'")

    else:
        #  switch to (syspath + PATH) by default
        for s in spaths:
            if os.path.exists(s + os.sep + fname):
                return os.path.split(s + os.sep + fname)
        else:
            raise YapyUtilsFinderError("Cannot find file: '" + str(fname) + "'")


def get_filesysposition(rfpname, toppath=None, spaths=None,):
    """Loads the specified module by it's name and file system path.
    Provides a common interface for all supported platforms and Python
    implementations: *CPyhton*, *IPython*, *IronPython*, *Jython*, 
    and *PyPy*. For the syntaxversions *Python2.7* and *Python3*.
    
    Args:
        rfpname:
            File path name of file to be searched, which is either 
            absolute, or relative. An absolute file path is vallidated 
            only, while a relative is searched within the set of *spaths*,
            which are resolved iterative from longest upward.
            The limiting top node is *toppath* as the highest valid hook
            for 'rfpname' as subpath.

        toppath:
            The constraint of the top level for the search operation.
            
        spaths:
            The list of search paths as insertion points of the subpath
            'rfpname'::
            
                default := [ os.getcwd(),] \\ 
                    + sys.path \\
                    + os.environ['PATH'].split(os.pathsep)

    Returns:
        The module object on success::

            res := (<path-name>, <filename>) 
        
        else::

            res := ('', '') 
    
    
    Raises:
        PlatformIDsError
      
        pass-through

    """
    rfpname = os.path.normpath(rfpname)
    toppath = os.path.normpath(toppath)
    
    if os.path.isabs(rfpname):
        if toppath and not rfpname.startswith(toppath):
            raise YapyUtilsFinderError(
                "toppath is not in path:\n  %s\n  %s'" % (str(rfpname), str(toppath),)
                )
        if os.path.exists(rfpname):
            return splitfile(rfpname)
        return ('', '')
    
    elif spaths == None:
        #  switch to (syspath + PATH) by default
        for s in [ os.getcwd(),] + sys.path + os.environ['PATH'].split(os.pathsep):
            if toppath and not (s + os.sep + rfpname).startswith(toppath + os.sep):
                continue

            if os.path.exists(s + os.sep + rfpname):
                return splitfile(s + os.sep + rfpname)
            else:
                _s = s
                _f = _s.split(os.sep)
                for sx in range(len(_f)):
                    if os.path.exists(_s):
                        return splitfile(_s)
                    _s = re.sub(r'[\\\\/]*[^\\\\/]$', '', _s)
        else:
            raise YapyUtilsFinderError("Cannot find file: '" + str(rfpname) + "'")


    else:
        for s in spaths:
            if toppath and not s.startswith(toppath):
                continue

            if os.path.exists(s + os.sep + rfpname):
                return splitfile(s + os.sep + rfpname)
            else:
                _s = s
                _f = re.split(os.sep, s)
                for sx in range(len(_f)):
                    if os.path.exists(_s + os.sep + rfpname):
                        return splitfile(_s + os.sep + rfpname)
                    _s = re.sub(r'[\\\\/]*?[^\\\\/]*$', '', _s)
        else:
            raise YapyUtilsFinderError("Cannot find file: '" + str(rfpname) + "'")


def find_files(srcdir, *wildcards, **kargs):
    """Assembles a list of package files for package_files.

    Args:
        srcdir: 
            Source root.
        
        \*wildcards: 
            List of globs.
        
        kargs:
            single_level:
                Flat only.
            
            subpath:
                Cut topmost path elemenr from listelements,
                special for dictionaries.
            
            nopostfix:
                Drop filename postfix.
            
            packages:
                List packages only, else files.
            
            yield_folders:
                List folders only.

    Returns:
        Results in an list.

    Raises:
        pass-through
        
    """
    ret=[]
    single_level = kargs.get('single_level', False)
    subpath = kargs.get('subpath', False)
    nopostfix = kargs.get('nopostfix', False)
    packages = kargs.get('packages', False)
    yield_folders = kargs.get('yield_folders', True)
    blacklist = kargs.get('blacklist', ('.gitignore', '.git', '.svn'))

    for path, subdirs, files in os.walk(srcdir):
        if yield_folders:
            files.extend(subdirs)

        if subpath:
            path=re.sub(r'^[^'+os.sep+']*'+os.sep, '',path)

        for name in sorted(files):

            if name in blacklist:
                continue

            for pattern in wildcards:
                if fnmatch.fnmatch(name, pattern):
                    if packages:
                        if not name == '__init__.py':
                            continue
                        ret.append(path)
                        continue
                    if nopostfix:
                        name=os.path.splitext(name)[0]

                    ret.append(os.path.join(path, name))

        if single_level:
            break
    return ret


