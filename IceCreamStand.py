#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Restaurant import Restaurant
from Flavor import Flavor
class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavor = Flavor()     # Important


# In[ ]:




