#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 15:02:36 2018

@author: chakyu
"""

#---- Start Program ----

filename = input('Please enter the name of a csv file: ')
filename = filename + '.csv'

fileHandle = open(filename, 'r')

lc = 0
while True:    
    line = fileHandle.readline()
    if line == '':        
        fileHandle.close()
        break
    else:
        lc += 1

print('-'*50)
print('There are %i lines in the file provided' % lc)

#---- End Program ----