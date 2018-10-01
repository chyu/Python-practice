#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:52:49 2018

@author: chakyu
"""

#--- Start Program ---

aircode = input('Please enter an airport code: ')
aircode = aircode.upper()

citydict = {'SYD':'Sydney', 
            'BRI': 'Brisbane', 
            'MEL': 'Melbourne', 
            'HOB': 'Hobart', 
            'ADL': 'Adelaide', 
            'PER': 'Perth'}

if aircode in citydict:
    city = citydict[aircode]
    print(city)
else:
    print('Sorry, invalid airport code')
    aircode = input('Please enter a valid airport code: ')
    aircode = aircode.upper()

#--- End Program ---