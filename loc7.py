#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 15:32:31 2018

@author: chakyu
"""

#Learning about Classes-----------------
class Location:
    #Methods
    
    def __init__(self):
        
        self.lat = 0.5
        self.long = 151.2
    
    def setPosition(self, newLat, newLong):
        
        if -90 < newLat < 90:
            self.lat = newLat
        else:
            self.lat = 0
            
        if -180 < newLong < 180:
            self.long = newLong 
        else:
            self.long = 0
       
    def getLat(self):
        return self.lat
    
    def getLong(self):
        return self.long
    
    def onEquator(self):
        if -1 < self.lat < 1:
            self.equator = True
        else:
            self.equator = False
        return self.equator
    
    def whichHemisphere(self):
        if -90 < self.lat < 0:
            self.hemisphere = 'South'
        elif 0 < self.lat < 90:
            self.hemisphere = 'North'
        elif self.lat == 0:
            self.hemisphere = 'Equator'
        return self.hemisphere
        
    def positionPrint(self):
        print(self.lat)
        print(self.long)
        print(self.onEquator())
        print(self.whichHemisphere())
   
#Mainline ------------------------------

home = Location()
home.positionPrint()
