#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 21:41:58 2018

@author: chakyu
"""

#---- Start Program ----

import math

#---- Start diameter function ----

def calcDiameter(radius):
    diameter = radius*2
    return diameter

#---- End diameter function ----

#----Start circumference function ----

def calcCircumference(radius):
    circum = math.pi*calcDiameter(radius)
    return circum

#---- End circumference function ----
    
#---- Start calculate area function ----

def calcArea(radius):
    area = math.pi*radius**2
    return area

#---- End calculate area function ----

#---- Start calculate volume function ----

def calcVolume(radius):
    volume = (4/3)*math.pi*radius**3
    return volume

#---- End calculate volume function ----
    
#---- Mainline ----

radius = input('Please enter a number for radius in cm: ')
radius = float(radius)

print('A circle of radius %0.2f cm has diameter of %0.2f cm' % (radius, calcDiameter(radius)))
print('A circle of radius %0.2f cm has a circumference of %0.2f cm' % (radius, calcCircumference(radius)))
print('A circle of radius %0.2f cm has a area of %0.2f cm squared' % (radius, calcArea(radius)))
print('A circle of radius %0.2f cm has a volume of %0.2f cm cubed' % (radius, calcVolume(radius)))

#---- End Program ----