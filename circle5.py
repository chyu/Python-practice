#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 21:32:46 2018

@author: chakyu
"""

#---- Start Program ----

#---- Start diameter function ----

def calcDiameter(radius):
    diameter = radius*2
    return diameter

#---- End diameter function ----
    
#---- Mainline ----

radius = input('Please enter a number: ')
radius = float(radius)

print('A circle of radius %0.2f cm has diameter of %0.2f cm' % (radius, calcDiameter(radius)))

#---- End Program ----