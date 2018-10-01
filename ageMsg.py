#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 16:59:45 2018

@author: chakyu
"""

#--- Start Program ---


name = input('Please enter your name: ')
age = input('Please enter your age: ')


if name == 'Chak':
    print('Hello Master %s' % name)

    if int(age) >= 45:
        print('My you must be so wise!')
    else:
        print('You''re just a spring chicken!')
        
else:
    if int(age) >= 45:
        print('Hello ', name)
        print('My you must be so wise!')
    else:
        print('Hello ', name)
        print('You''re just a spring chicken!')

#--- End Program ---

