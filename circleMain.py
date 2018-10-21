#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:26:40 2018

@author: chakyu
"""
import sys
sys.path.append('/Users/chakyu/Documents/Personal/Interest/Engineering/Programming/Python/Practice/Python-practice/')

import circleFn
#---- Start Program ----

radius = input('Please enter a number for radius in cm: ')
radius = float(radius)

circleProps = circleFn.calcProperties(radius)

print('-'*60)
print('A circle of radius %0.2f cm has diameter of %0.2f cm' % (radius, circleProps[0]))
print('A circle of radius %0.2f cm has a circumference of %0.2f cm' % (radius, circleProps[1]))
print('A circle of radius %0.2f cm has a area of %0.2f cm squared' % (radius, circleProps[2]))
print('A circle of radius %0.2f cm has a volume of %0.2f cm cubed' % (radius, circleProps[3]))

#---- End Program ----