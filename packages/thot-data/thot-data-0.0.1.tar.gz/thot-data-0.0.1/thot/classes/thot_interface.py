
# coding: utf-8

# # Thot Interface

# In[3]:


from abc import ABC, abstractmethod


# In[4]:


class ThotInterface( ABC ):
    
    def __init__( self, root ):
        """
        :param root: Root Container.
        """
        self._root = root
        self._db = None
    
    
    @property
    def root( self ):
        return self._root
    
    
    @abstractmethod
    def find_container( self, search = {} ):
        """
        Gets a single Container matching search criteria.
        
        :param search: Dictionary of search criteria.
            [Default: {}]
        :returns: Container matching search criteria or None.
        """
        return self._db.containers.find_one( search )
    
    
    @abstractmethod
    def find_containers( self, search = {} ):
        """
        Gets Containers matching search criteria.
        
        :param search: Dictionary of search criteria.
            [Default: {}]
        :returns: List of Containers matching search.
        """
        return self._db.containers.find( search )
    
    
    @abstractmethod
    def find_asset( self, search = {} ):
        """
        Gets a single Asset matching search criteria.
        
        :param search: Dictionary of search criteria.
            [Default: {}]
        :returns: Asset matching search criteria or None.
        """
        return self._db.assets.find_one( search )
    
    
    @abstractmethod
    def find_assets( self, search = {} ):
        """
        Gets Assets matching search criteria.
        
        :param search: Dictionary of search criteria.
            [Default: {}]
        :returns: List of Assets matching search.
        """
        return self._db.assets.find( search )
    
    
    @abstractmethod
    def add_asset( self, asset ):
        """
        Adds a new Asset.
        
        :param asset: Asset to create.
        """
        pass

