#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Restaurant():
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(self.restaurant_name.title()+" is a "+self.cuisine_type+" restaurant")
        
    def open_restaurant(self):
        print(self.restaurant_name.title()+" is opening now")
    
    def set_number_served(self,num):
        self.number_served = num
        
    def increment_number_served(self,num):
        self.number_served += num    
        
class Flavor():
    def __init__(self):
        self.flavors = ["Vanilia","Choclate","Strewbrew"]
        
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)
        
class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavor = Flavor()     # Important
        
