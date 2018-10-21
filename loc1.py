#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 15:12:07 2018

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

lat = input('Please enter the latitude of your position: ')
long = input('Please enter the longitude of your position: ')

home = Location()
home.setPosition(lat, long)

print(home.getLat())
print(home.getLong())
