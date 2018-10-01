#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:33:11 2018

@author: chakyu
"""

# --- Start Program ---

name = input('Please enter your name: ')
age = input('Please enter your age: ')

while True:

    age = float(age)
    if 0 <= age <= 120:
        
        if int(age) >= 45:
            print('Hello ', name + '!')
            print('My you must be so wise!')
        else:
            print('Hello ', name + '!')
            print('You''re just a spring chicken!')
            
        break
    
    else:
        print('You have entered an invalid age')
        age = input('Please input a valid age (e.g. between 0 and 120): ')




# --- End Program ---