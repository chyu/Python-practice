#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 15:42:46 2018

@author: chakyu
"""

import re

#---- Start Program ----

filename = input('Please enter a the name of a Python file: ')
filename = filename + '.py'

fileHandle = open(filename, 'r')

#line = fileHandle.readline()

lc = 0

for line in fileHandle:
    if re.search('#', line):
        if re.search('#!', line):
            lc += 0
        else:
            lc += 1

        
print('-'*50)
print('There are %i lines containing comments in this script' % lc)

#---- End Program ----