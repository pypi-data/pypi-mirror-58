
# coding: utf-8

# # Mongo Config
# Configuration MongoDB

# In[ ]:


from pymongo import MongoClient


# In[ ]:


connection_string = 'mongodb://localhost:27017/thot'

#TODO [2]: Share connection across imports?
client = MongoClient( connection_string )
db = client.thot


# In[ ]:


class MongoDB():
    pass

