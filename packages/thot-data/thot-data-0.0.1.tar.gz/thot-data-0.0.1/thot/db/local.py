
# coding: utf-8

# # Local Database

# In[5]:


import os
import json
from datetime import datetime
from glob import glob
from functools import partial
from collections.abc import Mapping


# ## Document Objects

# In[182]:


class LocalObject( Mapping ):
    """
    Implements a local object.
    """
    
    # valid object types
    kinds = [
        'container',
        'asset'
    ]
    
    _object_file_format = '_{}.json'
    
    @classmethod
    def get_object_file( klass, path ):
        """
        :returns: Property file of path.
        :raises RuntimeError: If there is not one and only one property file.
        """
        # valid kinds
        obj_files = [ 
            klass._object_file_format.format( kind ) 
            for kind in klass.kinds 
        ] 
        
        # get property files
        contents = os.listdir( path )
        obj_file = [ 
            obj_file 
            for obj_file in obj_files 
            if ( obj_file in contents ) 
        ]
        
        # check only only one property file
        if len( obj_file ) is not 1:
            # not only one property file found
            raise RuntimeError( 
                '{} object file(s) found. Must have one and only one'.format( len( obj_file ) )
            )
            
        return obj_file[ 0 ]
        
    
    def __init__( self, path, parent = None ):
        """
        :param path: Path to the object.
        :param parent: Parent Object, or None if root. [Default: None]
        """
        self.__path = os.path.normpath( path )
        self.__parent = parent
        self.__object_file = self.get_object_file( self.path )
        
        # get properties        
        with open( os.path.join( self.path, self.__object_file ), 'r' ) as props:
            self.meta = json.load( props )
            
        # default name
        if 'name' not in self.meta:
            self.meta[ 'name' ] = os.path.basename( self.path )
        
        # get notes
        self.__notes = []
        notes_path = os.path.join( self.path, '_notes/' )
        if os.path.exists( notes_path ):
            for note in os.listdir( notes_path ):
                note_path = os.path.join( notes_path, note )
                stats = os.stat( note_path )
                created = datetime.fromtimestamp( stats.st_mtime ).isoformat( ' ' )

                with open( note_path, 'r' ) as f:
                    content = f.read()

                self.__notes.append( {
                    'title':   os.path.splitext( note )[ 0 ],
                    'created': created,
                    'content': content
                } )
        
        # get children
        self.__children = []
        for child in glob( os.path.join( self.path, '*/' ) ):
            try:
                 self.__children.append( 
                     LocalObject( child, parent = self )
                 )
                    
            except RuntimeError as err:
                # child was not an object, ignore
                continue
        
        # get scripts, if container
        if self.kind == 'container':
            scripts_path = os.path.join( 
                self.path, self._object_file_format.format( 'scripts' ) 
            )
            
            if os.path.exists( scripts_path ):
                with open( scripts_path, 'r' ) as f:
                    self.__scripts = json.load( f )
                    
            else:
                self.__scripts = []
            
        
        
    @property
    def _id( self ):
        return self.path
    
        
    @property
    def path( self ):
        return self.__path
    
    
    @property
    def kind( self ):
        """
        :returns: Kind of the object, as determined from its property file.
        """
        off   = self._object_file_format
        start = off.find( '{}' )
        end   = off.find( '.' ) - len( off )
        
        return self.__object_file[ start : end ]
    
    
    @property
    def parent( self ):
        return self.__parent
    
    
    @property
    def notes( self ):
        return self.__notes
    
    
    @property
    def scripts( self ):
        if self.kind == 'container':
            return self.__scripts
        
        raise AttributeError( "'LocalObject' object has no attribute 'scripts'" )
    
    
    @property
    def children( self ):
        return self.__children
    
    
    @property
    def is_root( self ):
        """
        :returns: If Object is root.
        """
        return ( self.parent is None )
    
    
    def __getitem__( self, item ):
        if item is '_id':
            return self.path
        
        elif item is 'notes':
            return self.notes
        
        elif item is 'children':
            return [ child.path for child in self.children ]
        
        elif item is 'parent':
            return ( 
                None 
                if ( self.parent is None ) else
                self.parent.path
            )
        
        elif ( item is 'scripts' ) and ( self.kind == 'container' ):
            return self.scripts
            
        return self.meta[ item ]
        
    
    def __iter__( self ):
        items = self.meta.copy()
        items[ '_id' ]      = self.path
        items[ 'notes' ]    = self.notes
        items[ 'children' ] = self.get( 'children' )
        items[ 'parent' ]   = self.get( 'parent' )
        
        if self.kind == 'container':
            items[ 'scripts' ]  = self.scripts
    
        yield from items
    
    
    def __len__( self ):
        # account for parent, notes, scripts, children, and meta
        extra = 4 if ( self.kind is 'container' ) else 3
        count = len( self.meta ) + extra
        
        return count


# ## DB Objects

# In[183]:


class LocalCollection():
    """
    Implements a local collection.
    """
    
    def __init__( self, root, kind ):
        """
        :param root: Path to root folder.
        :param kind: The collection to represent.
        """
        self.__root = LocalObject( root )
        self.__kind = kind
        
        # collect objects
        def collect_objects( root ):
            """
            Gets object of the same kind of the collection.
            
            :param root: Root object to search.
            :returns: List of LocalObjects with matching kind.
            """
            objs = []
            if root.kind == self.kind:
                objs.append( root )
                
            for child in root.children:
                objs += collect_objects( child )
                
            return objs
        
        self.__objects = collect_objects( self.root )
        
        
    @property
    def root( self ):
        return self.__root
        
    
    @property
    def kind( self ):
        return self.__kind
    
    
    def find_one( self, search = {} ):
        """
        Gets a single object matching search critera.
        
        :param search: Dictionary of property-value pairs to filter.
            If {} returns all objects.
            Syntax as is for MongoDB.
            [Default: {}]
        :returns: LocalObject matching search criteria or None.
        """
        result = self.find( search )
        
        return (
            None 
            if ( len( result ) is 0 ) else 
            result[ 0 ]
        )
    
    
    def find( self, search = {} ):
        """
        Gets objects matching search criteria.
        
        :param search: Dictionary of property-value pairs to filter.
            If {} returns all objects.
            Syntax as is for MongoDB.
            [Default: {}]
        :returns: List of LocalObjects matching search criteria.
        """
        def filter_prop( prop, value, obj ):
                """
                Check if object matched property filter.
                
                :param prop: Name of the property to check.
                :param value: Value to match, or Dictionary to recurse.
                :param obj: LocalObject.
                :returns: True if matches, False otherwise.
                """
                # parse prop
                prop_path = prop.split( '.' )
                for part in prop_path:
                    try:
                        obj = obj[ part ]
                
                    except KeyError as err:
                        # property not contained in object
                        return False
                    
                return ( obj == value )
                
               
        
        matching = self.__objects
        for prop, value in search.items():
            obj_fltr = partial( filter_prop, prop, value )
            matching = filter( obj_fltr, matching )
            
        return list( matching )
    
    
    def insert_one( self, path, properties = {} ):
        """
        Insert a new object into the database.
        
        :param path: Path of the object.
        :param properties: Properties of the object. [Default: {}]
        """
        if not os.path.exists( path ):
            # create folder for asset
            os.mkdir( path )
        
        # check object does not already exist
        try:
            LocalObject.get_object_file( path )
            
        except RuntimeError as err:
            # object file does not exist yet
            pass
            
        else:
            # object file already exists
            raise RuntimeError( 'Object {} already exists.'.format( path ) )
            
        # create object file
        pf = LocalObject._object_file_format.format( self.kind )
        pf_path = os.path.join( path, pf )
        
        with open( pf_path, 'w' ) as f:
            json.dump( properties, f )
        
        # TODO [1]: add object to self
        

        
    def replace_one( self, path, properties = {}, upsert = False ):
        """
        Replaces an object.
        
        :param path: Path of the object.
        :param properties: Properties of the object. [Default: {}]
        :param upsert: Insert new document if it doesn't yet exist.
            [Default: False]
        """
        # check object already exists
        try:
            LocalObject.get_object_file( path )
            
        except RuntimeError as err:
            # object file does not exist yet
            if upsert:
                # allowed to create new object
                self.insert_one( path, properties )
                return
                 
            else:
                raise RuntimeError( 'Object {} does not exists.'.format( path ) )
            
        # create object property file
        pf = LocalObject._object_file_format.format( self.kind )
        pf_path = os.path.join( path, pf )
        
        with open( pf_path, 'w' ) as f:
            json.dump( properties, f )
            
        # TODO [1]: add object to self


# In[184]:


class LocalDB():
    """
    Implements a local database.
    """
    
    def __init__( self, root ):
        """
        :param root: Path to root folder.
        """
        self.__root = os.path.normpath( root )
        
        self.__containers = LocalCollection( root, 'container' )
        self.__assets     = LocalCollection( root, 'asset' )
        
    
    @property
    def root( self ):
        return self.__root
    
    
    @property
    def containers( self ):
        return self.__containers
    
    
    @property
    def assets( self ):
        return self.__assets


# # Work

# In[185]:


# root = os.path.join( os.getcwd(), '../../_tests/projects/inclined-plane' )
# db = LocalDB( root )

