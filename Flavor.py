#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Flavor():
    def __init__(self):
        self.flavors = ["Vanilia","Choclate","Strewbrew"]
        
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)

