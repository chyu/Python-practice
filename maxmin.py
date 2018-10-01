#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:26:59 2018

@author: chakyu
"""

#---- Start Program ----

numlist = []
for i in range(1,6):
    numbers = input('Please input 5 numbers. Number %i: ' % i)
    numbers = float(numbers)
    numlist.append(numbers)
    
maxn = max(numlist)
minn = min(numlist)

print()
print('------------------------------------------')
print('The smallest number entered is: %.3f' % minn)
print('The smallest number entered is: %.3f' % maxn)

#---- End Program ----