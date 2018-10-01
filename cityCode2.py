#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 12:00:16 2018

@author: chakyu
"""

#--- Start Program ---

aircode = input('Please enter an airport code: ')
citydict = {'SYD':'Sydney', 
            'BRI': 'Brisbane', 
            'MEL': 'Melbourne', 
            'HOB': 'Hobart', 
            'ADL': 'Adelaide', 
            'PER': 'Perth'}

city = citydict[aircode]
print(city)

#--- End Program ---