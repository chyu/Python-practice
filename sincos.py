#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:15:36 2018

@author: chakyu
"""

#---- Start Program ----

import math

angle = input('Please enter an angle (deg): ')
angle = float(angle)

anglerads = math.radians(angle)

sinang = math.sin(anglerads)
cosang = math.cos(anglerads)
tanang = math.tan(anglerads)

print('The angle entered is: ')
print('For an angle of %0.2f degrees, the: ' % angle)

print('sine is: \t\t %.3f' % sinang)
print('cosine is: \t\t %.3f' % cosang)
print('tangent is: \t\t %.3f' % tanang)


#---- End Program ----