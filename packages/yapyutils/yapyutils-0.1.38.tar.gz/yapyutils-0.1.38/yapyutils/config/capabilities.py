# -*- coding: utf-8 -*-
"""*yapyutils.config.capabilities* provides simple hierarchical configuration
file utils based on in-memory JSON representation. This includes nested and
chained configuration data branches.

The provided features are designed to provide some powerful features of structured
configuration based on basic standard libraries, thus providing advanced setup
support utilities for components of the lower software stack.

The higher layer software components should prefer more versatile and powerful
libraries such as **multiconf**.

The package *multiconf* provides tools for the conversion of various data formats
into *JSON*. This could be used to apply e.g. data type definitions supporting
inline comments - which JSON lacks.

"""

import os

from yapyutils.config import YapyUtilsConfigError
import yapydata.datatree.synjson



__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "60cac28d-efe6-4a8d-802f-fa4fc94fa741"

__docformat__ = "restructuredtext en"


#: default alternate search path locations for configuration files
_SPATH = (
    os.curdir,
    os.path.dirname(__file__) + os.sep + 'builder' + os.sep,
)


#: known suffixes
SUFFIXES = (
    'yaml',        # standard yaml 
    'json',        # standard json
    'xml',         # xml.etree
    'inix',        # configparser + custom
    'ini',         # configparser + custom
    'cfg',         # configparser + custom
    'conf',        # configparser + custom
    'properties',  # configparser + custom
)

class YapyUtilsCapabilityError(YapyUtilsConfigError):
    """Common access error. 
    """
    pass


class YapyUtilsCapabilityOidError(YapyUtilsCapabilityError):
    """Requested object name is not present.
    """
    pass


_debug = 0
_verbose = 0


# helper for multi-break
class _FileFound(Exception):
    pass
        

class Capability(object):
    """Provides JSON based read-only configuration of capabilities.
    This in particular comprises the priority based readout
    of values and defaults. The structure hereby includes
    specialization by subcomponents, where the missing value 
    will be tried from the more general enclosing super
    component.
    
    The access to structured data trees offers various method to
    access paths of nested node attributes. This comprises the
    creation as well as the readout.
    
    The following equivalent creation methods are supported, where
    'treenode' could be either the root node, or any subordinated
    branch::

        treenode['subnode0']['subnode1']['subnode7'] = value  # dynamic items
        
        value = treenode(
                    'subnode0', 'subnode1', 'subnode7',
                    create=True,
                )  # dynamic items by '__call__'

        value = treenode.subnode0.subnode1.subnode7           # static attribute addressing style

    The following equivalent readout methods are supported, where
    'treenode' could be either the root node, or any subordinated
    branch::

        value = treenode['subnode0']['subnode1']['subnode7']  # dynamic items
        value = treenode('subnode0', 'subnode1', 'subnode7')  # dynamic items by '__call__'
        value = treenode.subnode0.subnode1.subnode7           # static attribute addressing style

    """

    M_FIRST = 1   # use first matching node
    M_LAST = 2    # use last matching node
    M_ALL = 3     # use all - iterate all matches

    match_map = {
        M_FIRST: 1,
        M_LAST: 2,
        M_ALL: 3,
        'first': 1,
        'last': 2,
        'all': 3,
    }    

    def __init__(self, data={}):
        """
        Args:
            data:
                Configuration data::

                    data := (
                        <dict>             # in-memory JSON structure
                        <file-path-name>   # persistent JSON data
                    )

        Returns:
            None / initialized object

        Raises:
            YapyUtilsCapabilityError

            pass-through

        """
        self.data = data

        if not isinstance(self.data, (dict,)):
            raise YapyUtilsCapabilityError(
                "top 'node' must be a 'dict' == JSON object, got: "
                + str(self.data)
                ) 

    def __getitem__(self, key):
        """Gets the value of the path within the data.
        
        Args:
            key:
                The value of the node within *data*::

                    key := (
                          <single-key>
                        | <list-of-keys>
                        | <tuple-of-keys>
                    )

        Returns:
            The value of the addressed node/value.

        Raises:
            pass-through

        """
        if type(key) in (list, tuple):
            res = self.data
            for k in key:
                res = res[k]
            return res
        return self.data[key]

    def __setitem__(self, key, val):
        """Sets the value of the path within the data.
        
        Args:
            key:
                The value of the node within *data*::

                    key := (
                          <single-key>
                        | <list-of-keys>
                        | <tuple-of-keys>
                    )

            val:
                The node/value to be set at the addressed path.
                Non present values are created, present are
                replaced.

                REMARK: 
                    In case of lists the value of the key for
                    a non-present value has to be the increment of
                    the highest present key. Sparse lists are not
                    supported. 

        Returns:
            The value of the addressed node/value.

        Raises:
            pass-through

        """
        if isinstance(key, (list, tuple)):
            res = self.data
            last = 0
            for k in key:
                if isinstance(res, (list, tuple)):  # treat tuple equal until it raises
                    if k < len(res):
                        res = res[k]
                    elif k == len(res):
                        if last == 1:
                            res[-1] = type()
                        
                        res.append(None)
                        
                        last = 1
            res[key[-1]] = val
            return

        self.data[key] = val

    def __setattr__(self, name, value):
        """Validates types of own data attributes.

        Args:
            name:
                Name of the attribute. Following are reserved and
                treated special:
                
                * type: str - 'data'
                  The value is treated as the replacement of the internal
                  data attribute. Replaces or creates the complete data
                  of teh current instance.

            value:
                The value of the attribute. This by default superposes
                present values by replacement. Non-present are created.

        Returns:

        Raises:
            YapyUtilsCapabilityError

        """
        if name == 'data':
            #
            # replacement of current managed data
            #
            if not isinstance(value, dict):
                raise YapyUtilsCapabilityError(
                    "value must be a 'dict' == JSON object, got: "
                    + str(type(value))
                    ) 
            self.__dict__[name] = value

        else:
            #
            # any standard attribute with standard behavior
            #
            return object.__setattr__(self, name, value)

    def __getattr__(self, name):
        """
        Args:

        Returns:

        Raises:

        """
        if name == 'data':
            return self.__dict__[name]
        elif isinstance(name, tuple):
            
            return self.__getattr__(name)
            
        else:
#            return self.__dict__[name]
#            return object.__getattr__(name)
            return super(Capability, self).__getattr__(name)

    def __call__(self, *subpath, **kargs):
        """Readout the value of a node, or an attribute. The name binding
        of the path is provided as a tuple of path items. 

        Args:
            subpath:
                The list of keys constituting a branch of a data tree.
                The *subpath* is treated as a branch of one of the nodes
                of a provided *searchpath* - which is by default the top node.
                The supported values are::

                    subpath := <list-of-node-ids>
                    <list-of-node-ids> := <node-id> [',' <list-of-node-ids>]
                    node-id := (
                          str            # strings as keys - objects/dict only
                        | int            # integers as index - lists only
                        | tuple | list   # set as choice of valid literal path items
                        | <regexpr>
                    )
                    regexpr := <compiled-python-regular-expression>
                    compiled-python-regular-expression := re.compile(<regexpr>)
                    regexpr := "regular expression"

            kargs:
                searchpath:
                    Optional search path for the match of the provided 
                    address *subpath*. The provided *subpath* is applied
                    to each node of the *searchpath* in accordance to the 
                    *direction* option. This provides the search and 
                    enumeration of side branches::

                        searchpath := <path-item-list> 

                        path-item-list := <path-item> [, <path-item-list>]
                        path-item := (
                              str  # item name 
                            | int  # item index
                        ) 

                        default := <top-node>

                    The search path entries has to be actually present by default.
                    These  could be either created by loading a complete tree
                    structure, or by using the *Capabilities.create()* member.
                    See also parameter 'strict'.

                direction:
                    The search direction of the *subpath* within the 
                    *searchpath*. In case of multiple superpositioned
                    attributes the first traversed match.

                    The provided values are::

                        direction := (
                              up   | 0  | False # search from right-to-left
                            | down | 1  | True  # search from left-to-right
                        )

                        default:= up

                match:
                    Sets the match criteria for the search operation.
                    Interferes with *direction*::

                        match := (
                              M_FIRST | 'first'   # use first matching node
                            | M_LAST  | 'last'    # use last matching node
                            | M_ALL   | 'all'     # use all - iterate all matches
                        )

                        default := M_FIRST

                partial:
                    Enables the return of partial sub paths in case the requested
                    path is not completely present. ::

                        partial := (
                              True   # when not completely present, the longest 
                                     # existing part is returned, the completeness
                                     # is provided by the result attribute <partial>
                            | False  # when not completely present an exception
                                     # is raised 
                        )

                strict:
                    Controls the required consistency. This comprises:

                    1. the presence of the search path entries

                    2. the presence of the requested subpath within the set
                       of search paths 

        Returns:
            In case of a match returns the tuple::

                return := (<attr-value-path>, <attr-value>, <partial>)

                attr-value-path := (
                      "the list of keys of the top-down path"
                    | "empty list when no item exists"        # see <complete>
                )
                attr-value := "value of the targeted node/attribute"
                partial := (
                      False   # the complete requested path
                    | True    # the actually present part of the path
                )

            Else raises *YapyUtilsCapabilityOidError*.

        Raises:
            YapyUtilsCapabilityOidError

            pass-through

        """

        _srch = kargs.get('searchpath', ())
        _dir = kargs.get('direction', 0)
        _match = kargs.get('match', Capability.M_FIRST)
        
        if not isinstance(_srch, (tuple, list,)):
            raise YapyUtilsCapabilityError(
                "search path requires 'tuple' or'list', got: "
                + str(_srch)
                ) 

        #
        # match criteria
        #
        try:
            _match = self.match_map[_match]
        except IndexError:
            try:
                _match = self.match_map[str(_match).lower()] 
            except KeyError:
                raise YapyUtilsCapabilityError(
                    "valid match are (first, %d, last, %d, all, %d,), got: %s" %(
                        Capability.M_FIRST,
                        Capability.M_LAST,
                        Capability.M_ALL,
                        str(_match)
                    )
                )

        #
        # search direction
        #
        if _dir in (True, False,):
            pass
        else:
            _dir = str(_dir).lower()
            if _dir in ('up', '0',):
                _dir = False
            elif _dir in ('down', '1',):
                _dir = True
            else:
                raise YapyUtilsCapabilityError(
                    "valid directions are (up, 0, down, 1), got: "
                    + str(_dir)
                    ) 

        # collect the nodes on the searchpath
        _path_nodes = [self.data,]
        _cur = self.data
        if _srch:
            for x in _srch:
                try:
                    _cur = _cur[x]
                except (IndexError, KeyError, TypeError):
                    raise YapyUtilsCapabilityOidError(
                            "invalid search path: %s\n see: %s\n" %(
                                str(_srch),
                                str(x)
                            )
                        )

                _path_nodes.append(_cur)

        # revert for bottom-up search direction        
        if not _dir:
            # upward - up | 0 | False
            _path_nodes = reversed(_path_nodes)

        # now search the subpath for each node of the search path
        # first match wins
        for _pn in _path_nodes:
            _cur = _pn
            _idx_subpath = 0  # reset here
            for x in subpath:
                _excep = False
                try:
                    _cur = _cur[x]
                except (IndexError, KeyError, TypeError):
                    # continue with next level - only when nodes do not fit
                    _cur = None
                    _excep = True
                    break
                
            if not _excep:
                break  # has hit a regular match

        if _excep:
            # no match
            raise YapyUtilsCapabilityOidError(
                    "Missing subpath hook"
                    "\n  searchpath:   %s"
                    "\n  subpath hook: %s"
                    "\n  subpath:      %s\n" %(
                        str(_srch),
                        str(subpath[_idx_subpath - 1]),
                        str(subpath)
                    )
                )

        return _cur

#     def __str__(self):
#         res = ''
#         return res

    def create(self, *subpath, **kargs):
        """Creates a subpath to a given node, default is from top. 

        Args:
            subpath:
                The list of keys constituting a branch of a data tree.
                The *subpath* is treated as a branch of one of the nodes
                of a provided *searchpath* - which is by default the top node.
                The supported values are::

                    subpath := <list-of-node-ids>
                    <list-of-node-ids> := <node-id> [',' <list-of-node-ids>]
                    node-id := (
                          str            # strings as keys - objects/dict only
                        | int            # integers as index - lists only
                        | tuple | list   # set as choice of valid literal path items
                        | <regexpr>
                    )
                    regexpr := <compiled-python-regular-expression>
                    compiled-python-regular-expression := re.compile(<regexpr>)
                    regexpr := "regular expression"

            kargs:
                hook:
                    Optional node as parent of the insertion point for the new sub path.
                    The node must exist. ::

                        hook := (
                            
                        )

                    search path for the match of the provided 
                    address *subpath*. The provided *subpath* is applied
                    to each node of the *searchpath* in accordance to the 
                    *direction* option.

                    Default := <top-node>

                create:
                    Create missing entities of the requested path.
                    The provided value is the value of the final node::

                        create := <value-of-node>

                        value-of-node := <valid-json-node-type>
                        valid-json-node-type := (
                                              int | float
                                            | str                  # unicode
                                            | dict | list
                                            | None | True | False  # equivalent: null|true|false
                                            )

                        default := None

                direction:
                    The search direction of the *subpath* within the 
                    *searchpath*. In case of multiple superpositioning
                    attributes the first match of traversion. 

                    The provided values are::

                        direction := (
                              up   | 0  | False # search from right-to-left
                            | down | 1  | True  # search from left-to-right
                        )

                    Default:= up

                match:
                    Sets the match criteria for the search operation.
                    Interferes with *direction*::

                        match := (
                              M_FIRST   # use first matching node
                            | M_LAST    # use last matching node
                            | M_ALL     # use all - iterate all matches
                        )

                        default :=

        Returns:
            In case of a match returns the tuple::

                return := (<attr-value-path>, <attr-value>)

                attr-value-path := "the list of keys of the top-down path"
                attr-value := "value in accordance to the type of the attribute"

            Else raises *YapyUtilsCapabilityOidError*.

        Raises:
            YapyUtilsCapabilityOidError

            pass-through

        """

        _srch = kargs.get('searchpath', ())
        _dir = kargs.get('direction', 0)
        
        try:
            _create_value = kargs['create']
            _create = True
        except KeyError:
            _create_value = None
            _create = False

        if not isinstance(_srch, (tuple, list,)):
            raise YapyUtilsCapabilityError(
                "searchpath requires 'tuple' or'list', got: "
                + str(_srch)
                ) 

        if _dir in (True, False,):
            pass
        else:
            _dir = str(_dir).lower()
            if _dir in ('up', '0',):
                _dir = False
            elif _dir in ('down', '1',):
                _dir = True
            else:
                raise YapyUtilsCapabilityError(
                    "valid directions are (up, 0, down, 1), got: "
                    + str(_dir)
                    ) 

        # collect the nodes on the searchpath
        _path_nodes = [self.data,]
        _cur = self.data
        if _srch:
            for x in _srch:
                try:
                    _cur = _cur[x]
                except (IndexError, KeyError, TypeError):
                    raise YapyUtilsCapabilityOidError(
                            "invalid searchpath: %s\n see: %s\n" %(
                                str(_srch),
                                str(x)
                            )
                        )

                _path_nodes.append(_cur)

        # revert for bottom-up search direction        
        if not _dir:
            # upward - up | 0 | False
            _path_nodes = reversed(_path_nodes)

        # now search the subpath for each node of the search path
        # first match wins
        for _pn in _path_nodes:
            _cur = _pn
            _idx_subpath = 0  # reset here
            for x in subpath:
                _excep = False
                try:
                    _cur = _cur[x]
                except (IndexError, KeyError, TypeError):
                    # continue with next level - only when nodes do not fit
                    _cur = None
                    _excep = True
                    break
                
            if not _excep:
                break  # has hit a regular match

        if _excep:
            # no match
            raise YapyUtilsCapabilityOidError(
                    "Missing subpath hook"
                    "\n  searchpath:   %s"
                    "\n  subpath hook: %s"
                    "\n  subpath:      %s\n" %(
                        str(_srch),
                        str(subpath[_idx_subpath - 1]),
                        str(subpath)
                    )
                )

        return _cur

    def get(self, *key):
        """Gets a value from data.

        Args:

        Returns:

        Raises:

        """
        try:
            return self(*key)
        except:
            return None

    def addfile(self, fpname, key=None, node=None, **kargs):
        """Superposes a configuration file to the existing entries. Updates and
        creates granular items. The a applied traversing algorithm is::

            1. create non-existing branches and leafs
            2. replace existing leafs
            3. traverse existing leafs for new branches and existing leafs

        Args:
            fpname:
                see *readfile()*
                
            key:
                see *readfile()*
            
            node:
                see *readfile()*
            
            kargs:
                path:
                    see *readfile()*

                striproot:
                    see *readfile()*

                suffixes:
                    see *readfile()*

        Returns:
            Reference to updated data structure.

        Raises:
            YapyUtilsConfigError

            pass-through

        """
        jval = self.readfile(fpname, nodata=True, **kargs)

        _p = yapydata.datatree.synjson.DataTreeJSON(self.data)
        _p.join(jval)
        self.data = _p.data
        return self.data
    
    def readfile(self, fpname, key=None, node=None, **kargs):
        """Reads a JSON file. This is a simple basic method for the application
        on the lower layers of the software stack. It is designed for minimal
        dependencies. The used standard libraries support the syntaxes::

            INI, JSON, .properties, XML, YAML

        The data is by not validated. If this is required external higher layer
        tools such as *multiconf* could be applied.
        
        The *readfile()* simply replaces existing configuration data, for the 
        iterative update see *addfile()*.

        Args:
            fpname:
                File path name of the configuration file. Alternate relative names
                could be provided, where optionally additional parameters are used
                for search and file suffixes, see other parameters::

                    <path>/<fpname>[<suffix>]

            key:
                The key for the insertion point::

                    node[key] = <file-data>

                    default := None - replace self.data, 

                The caller is responsible for the containment of the provided
                node within the data structure represented by this object. No
                checks are performed. 

            node:
                The node for the insertion of the read data.::

                    default := <top>

            kargs:
                nodata:
                    Prohibit insertion to *self.data*, returns the data reference only. ::

                        default := False

                path:
                    Alternate list of search paths::

                        path := <list-of-search-paths> 
                        list-of-search-paths := <spath> [, <list-of-search-paths>]
                        spath := "path-prefix"
                        
                striproot:
                    A special option for *XML* files. When *True* suppresses the mandatory
                    named root node of *XML*. Thus provides a similar result as *JSON* for
                    better merge and internal processing. Other parsers simply ignore this
                    option.

                suffixes:
                    Suffixes as preferences for configuration file type::

                        suffixes := '[' <list-of-preferences> ']' 
                        list-of-preferences := <pref> [, <list-of-preferences>]
                        
                        pref := (     # the order defines the search and usage priority
                              'yaml'
                            | 'json'
                            | 'xml'
                            | 'inix'
                            | 'ini'
                            | 'cfg'
                            | 'properties'
                        )

        Returns:
            Reference to read data structure.

        Raises:
            YapyUtilsConfigError

            pass-through

        """

        _nodata = kargs.get('nodata')
        _app = kargs.get('app', '')
        _suffixes = kargs.get('suffixes', SUFFIXES)
        _spath = kargs.get('path', _SPATH)

        _parser = None
        if not os.path.isfile(fpname):
            try:
                for s in _spath:
                    for p in _suffixes:
                        if p[0] != '.':
                            p = '.' + p
                        if os.path.isabs(fpname) and os.path.exists(fpname + p):
                            datafile = os.path.abspath(fpname + p)
                            _parser = p
                            raise _FileFound

                        elif os.path.isabs(fpname) and os.path.exists(fpname + 'capabilities' + p):
                            datafile = os.path.abspath(fpname + os.sep + 'capabilities' + p)
                            _parser = p
                            raise _FileFound
        
                        elif os.path.exists(s + os.sep + fpname + p):
                            datafile = os.path.abspath(s + os.sep + fpname + p)
                            _parser = p
                            raise _FileFound

                        elif os.path.exists(s + os.sep + fpname + os.sep + 'capabilities' + p):
                            datafile = os.path.abspath(s + os.sep + fpname + os.sep + 'capabilities' + p)
                            _parser = p
                            raise _FileFound

            except _FileFound:
                pass

            else:
                raise YapyUtilsConfigError("Missing configuration file: " + str(fpname)) 

        else:
            datafile = fpname
        
        if _parser == None:
            _parser = os.path.splitext(datafile)[1]

        if _parser == '.yaml':
            from yapydata.datatree.synyaml import DataTreeYAML as Parser  # @UnusedImport
        elif _parser == '.xml':
            from yapydata.datatree.synxml import DataTreeXML as Parser  # @UnusedImport @Reimport
        elif _parser == '.json':
            from yapydata.datatree.synjson import DataTreeJSON as Parser  # @UnusedImport @Reimport
        elif _parser in ('.ini', '.inix', '.cfg', '.conf', ):
            from yapydata.datatree.synini import DataTreeINI as Parser  # @Reimport
        elif _parser in ('.properties', ):
            raise NotImplemented("not yet available")

        jval = Parser().import_data(datafile, key, node, **kargs)

        if key and node == None:
            raise YapyUtilsConfigError("Given key(%s) requires a valid node." % (str(key)))

        if key:
            node[key] = jval
        elif not _nodata:
            self.data = jval

        return jval

