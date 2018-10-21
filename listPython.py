#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:37:42 2018

@author: chakyu
"""

#---- Start program ----

import os
import re

#--------------------------------------------------------------

def countComments(filename):
    fileHandle = open(filename, 'r')
    
    #line = fileHandle.readline()
    
    lc = 0
    
    for line in fileHandle:
        if re.search('#', line):
            if re.search('#!', line):
                lc += 0
            else:
                lc += 1

    return lc   

#--------------------------------------------------------------

#---- Main ----

filenames = os.listdir('.')

pcount = 0
pcountcom = 0
totalcom = 0
for filename in filenames:
    
    ext = filename[-3:]
    
    if ext == '.py':
        lineCount = countComments(filename)
        
        if lineCount != 0:
            print('There are %i commented lines in %s' % (lineCount,filename))
            pcountcom += 1
            totalcom = totalcom + lineCount
        else:
            print('There are no commented lines in %s' % (filename))
         
        pcount += 1

print('')
print('-'*50)
print('')
print('The number of python programs in this directory is %i' % pcount)
print('The number of python programs in this directory with comments is %i' % pcountcom)
print('There are a total of %i comments across all the python programs in directory: %s' % (totalcom,os.getcwd()))
print('The average number of comments per program in this directory is %0.2f' % (totalcom/pcount))



#---- End program ----