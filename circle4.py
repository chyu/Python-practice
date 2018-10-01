#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 16:44:51 2018

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
print('A circle with a radius of %.3f cm has:' % radius)
print('A diameter of %15.3fcm' % diameter)
print('A circumference %13.3fcm squared' % area)
print('A volume of %17.3fcm cubed' % volume)

# --- End Program ---