#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:49:40 2018

@author: chakyu
"""

# --- Start Program ---


radius = input('Please enter a number: ')

#check digit
while not radius.isdigit() == True:
    print('Sorry. Entered value contains types other than numbers.')
    radius = input('Please enter an integer for radius: ')
    print()

print('A circle of ', radius, 'cm has a diameter of ', int(radius)*2, 'cm')


# --- End Program ---