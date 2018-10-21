#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 15:05:01 2018

@author: chakyu
"""

#Learning about Classes-----------------
class Location:
    #Methods
    def setPosition(self, newLat, newLong):
       self.lat = newLat
       self.long = newLong
       
       
    def getLat(self):
        return self.lat
    
    def getLong(self):
        return self.long
    
    
#Mainline ------------------------------

home = Location()
home.setPosition(-33.8, 151.2)

print(home.getLat())
print(home.getLong())
