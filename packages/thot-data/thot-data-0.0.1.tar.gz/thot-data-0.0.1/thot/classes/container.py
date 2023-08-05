
# coding: utf-8

# # Container

# In[2]:


from datetime import datetime

from .base_object import BaseObject
from .role import Role
from .note import Note
from .metadata import Metadata
from .asset import Asset


# In[ ]:


class Container( BaseObject ):
    """
    A Container.
    """
    
    def __init__( self, **kwargs ):
        """
        Creates a new Asset.
        
        :param **kwargs: Initial property values.
        """
        defaults = {
            'created':      datetime.now(),
            'type':         None,
            'name':         None,
            'description':  None,
            'parent':       None,
            'roles':        [],
            'tags':         [],
            'notes':        [],
            'children':     [],
            'assets':       [],
            'scripts':      [],
            'metadata':     {}
        }
        
        super().__init__( kwargs, defaults )
    
    
    
    def find_descendants( self, search = {}, level = None ):
        """
        Gets descendents.
        
        :param match: Dictionary filter or None for no filter. [Default: None]
        :param level:
        :returns: List of Containers.
        """
        pass
    
    
    def find_assets( self, search = {} ):
        """
        
        """
        pass
    
    
    def find_scritps( self, search = {} ):
        """
        
        """
        pass

