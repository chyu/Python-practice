#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:08:10 2018

@author: chakyu
"""

#---- Start program ----

namefriend = input('Please enter the name of someone who\'s number you\'d like to find: ')

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

        if name == namefriend:
            print('%s\'s number is %s' % (name, number))


#---- End program ----