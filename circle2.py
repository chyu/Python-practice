#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 16:36:44 2018

@author: chakyu
"""

# --- Start Program ---

# define pi
pi = 3.14159

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
