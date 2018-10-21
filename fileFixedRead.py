#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 15:39:16 2018

@author: chakyu
"""

#---- Start program ----

fileHandle = open('namesfixed.csv', 'r')

while True:
    line = fileHandle.readline()
    if  line == '':
        fileHandle.close()
        break
    else:
        name = line[0:10]
        name = name.strip() #removing empty characters
        
        number = line[10:]

        print('%s\'s number is %s' % (name, number))

#---- End program ----