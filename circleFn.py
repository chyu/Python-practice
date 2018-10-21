#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:26:40 2018

@author: chakyu
"""

import math
    
#---- Start Program ----

def calcProperties(radius):
    
    properties = []
#---- Start diameter function ----
    diameter = radius*2
    properties.append(diameter)
#----Start circumference function ----
    circum = math.pi*diameter
    properties.append(circum)
#---- End circumference function ----
    
#---- Start calculate area function ----
    area = math.pi*radius**2
    properties.append(area)
#---- End calculate area function ----

#---- Start calculate volume function ----
    volume = (4/3)*math.pi*radius**3
    properties.append(volume)
#---- End calculate volume function ----

    return properties
    
#---- End Program ----