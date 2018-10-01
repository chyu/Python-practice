#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:14:51 2018

@author: chakyu
"""

import math

# --- Start Program ---

# define pi
pi = math.pi

#enter radius
radius = input('Please enter a number: ')
radius = float(radius)

#Perform calculations
diameter = radius*2
circumference = pi*2*radius
area = pi*radius**2
volume = (4/3)*pi*(radius**3)

#Print results
print('A circle of ', radius, 'cm has')
print('A diameter of ', diameter, 'cm')
print('A circumference ', area, 'cm squared')
print('A volume of ', volume, 'cm cubed')





# --- End Program ---