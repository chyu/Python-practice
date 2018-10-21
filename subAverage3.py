#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 22:01:04 2018

@author: chakyu
"""

#---- Start Program ----

#---- Start calc average function ----

def calcAverage(num1, num2, num3):
    average = (num1+num2+num3)/3
    return average

#---- End calc average function ----

num1 = float(input('Please enter the first number: '))
num2 = float(input('Please enter the second number: '))
num3 = float(input('Please enter the third number: '))

print('The average of these numbers is %.3f ' % calcAverage(num1, num2, num2))


#---- End Program ----