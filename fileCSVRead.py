#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 15:39:16 2018

@author: chakyu
"""

#---- Start program ----

fileHandle = open('names.csv', 'r')

while True:
    line = fileHandle.readline()
    if  line == '':
        fileHandle.close()
        break
    else:
        namenumbers = line.split(',')

        name = namenumbers[0]
        number = namenumbers[1].strip('\n')

        print('%s\'s number is %s' % (name, number))

#---- End program ----