
# coding: utf-8

# # Thot
# Library for data analysis and management.

# In[1]:


import os
import random

from .db.local import LocalObject, LocalDB
# from db.mongo import MongoDB

from .classes.thot_interface import ThotInterface
from .classes.container      import Container
from .classes.asset          import Asset
from .classes.script         import ScriptAssociation


# ## Local

# In[2]:


class LocalProject( ThotInterface ):
    
    def __init__( self, root = None ):
        """
        :param root: Root Container.
        """
        if root is None:
            root = os.environ[ 'THOT_CONTAINER_ID' ]
        
        super().__init__( root )
        self._db = LocalDB( self._root )
        
        # set environment
        os.chdir( root )
    
    
    def find_container( self, search = {} ):
        """
        Gets a single Container matching search criteria.
        
        :param search: Dictionary of search criteria.
            [Default: {}]
        :returns: Container matching search criteria or None.
        """
        result = super().find_container( search )
        
        if result is None:
            return None
        
        container = LocalProject._object_to_container( result )
        return container
    
    
    def find_containers( self, search = {} ):
        """
        Gets Containers matching search criteria.
        
        :param search: Dictionary of search criteria.
            [Default: {}]
        :returns: List of Containers matching search.
        """
        result = super().find_containers( search )
        
        containers = []
        for res in result:
            containers.append( LocalProject._object_to_container( res ) )
    
        return containers    

    
    def find_asset( self, search = {} ):
        """
        Gets a single Asset matching search criteria.
        
        :param search: Dictionary of search criteria.
            [Default: {}]
        :returns: Asset matching search criteria or None.
        """
        result = super().find_asset( search )
        
        if result is None:
            return None
        
        asset = Asset( **result )
        return asset
    
    
    def find_assets( self, search = {} ):
        """
        Gets Assets matching search criteria.
        
        :param search: Dictionary of search criteria.
            [Default: {}]
        :returns: List of Assets matching search.
        """
        result = super().find_assets( search )
    
        assets = [ Asset( **asset ) for asset in result ]
        return assets    
    
    
    def add_asset( self, properties, _id = None, overwrite = True ):
        """
        Creates a new Asset.
        
        :param properties: Dictionary of information about the Asset.
        :param _id: Id of new asset, or None to create one.
            [Default: None]
        :param overwrite: (NOT IMPLEMENTED) Allow Asset to be overwritten if it already exists.
            [Default: True]
        :returns: Path to Asset file.
        """
        # check file is defined
        if 'file' not in properties:
            _id = str( random.random() )[ 2: ]
        
        if _id is None:
            _id = str( random.random() )[ 2: ]
        
        # set properties
        properties[ 'creator_type' ] = 'script'
        properties[ 'creator' ] = os.environ[ 'THOT_SCRIPT_SCRIPT' ]
        
        path = os.path.normpath( 
            os.path.join( self.root, _id )
        )
        
        # TODO [1]: Allow overwriting
#         if overwrite:
#             self._db.assets.replace_one( path, properties, upsert = True )
            
        self._db.assets.insert_one( path, properties )
    
        return os.path.normpath( 
            os.path.join( path, properties[ 'file' ] )
        )
    
    
    @staticmethod
    def _sort_objects( objects ):
        """
        Sorts a list of LocalObjects by kind
        """
        # sort types of children
        kinds = { kind: [] for kind in LocalObject.kinds }
        for obj in objects:
            kinds[ obj.kind ].append( obj )
        
        return kinds
    
    
    @staticmethod
    def _object_to_container( obj ):
        """
        Converts a LocalObject to a Container.
        
        :param obj: LocalObject of kind container.
        :returns: Container.
        """
        container = dict( obj )
        
        # sort children
        kinds = LocalProject._sort_objects( obj.children )

        container[ 'children' ] = [ child._id  for child  in kinds[ 'container' ] ]
        container[ 'assets' ]   = [ asset._id  for asset  in kinds[ 'asset' ] ]
        container[ 'scripts' ]  = [  
            ScriptAssociation( **script )
            for script in obj.scripts 
        ]
        
        container = Container( **container )
        
        return container


# ## Hosted

# In[43]:



# from bson.objectid import ObjectId

# get root
# _root_container = db.containers.find_one( { 
#     '_id': ObjectId( _root_container_id ) 
# } )

class ThotProject( ThotInterface ):
    
    def __init__( self, root ):
        """
        :param root: Root Container.
        """
        super().__init__( root )
    
    
    def find_container( self, search = {} ):
        """
        Gets a single Container matching search criteria.
        
        :param search: Dictionary of search criteria.
            [Default: {}]
        :returns: Container matching search criteria or None.
        """
        pass
    

    def find_containers( self, search = {} ):
        """
        Gets Containers matching search criteria.
        
        :param search: Dictionary of search criteria.
            [Default: {}]
        :returns: List of Containers matching search.
        """
        pass
    
    
    def find_asset( self, search = {} ):
        """
        Gets a single Asset matching search criteria.
        
        :param search: Dictionary of search criteria.
            [Default: {}]
        :returns: Asset matching search criteria or None.
        """
        pass
    
    
    def find_assets( self, search = {} ):
        """
        Gets Assets matching search criteria.
        
        :param search: Dictionary of search criteria.
            [Default: {}]
        :returns: List of Assets matching search.
        """
        pass
    
    
    def create_asset( self, asset ):
        """
        Creates a new Asset.
        
        :param asset: Asset to create.
        """
        pass


# # Work

# In[62]:


# root = os.path.join( os.getcwd(), '_tests/data/inclined-plane' )
# thot = LocalProject( root )


# In[63]:


# result = thot.find_container( { 'type': 'sample' } )

