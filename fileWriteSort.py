#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:30:35 2018

@author: chakyu
"""

#---- Creating files ----

fileHandle = open('names.csv', 'w')

print('Welcome to the phone number program')

i = 1
name = input('Please enter person %i\'s name: ' % i)

namelist = [] #need to create a list so that we can sort later on
namedict = {} #need to create a dictionary so that we can reference the numbers to the names after the sort
while True:

    if name == '':
        print()
        print('-'*50)
        print('No more names entered. Program will cease and file will be closed.')
        print('Thank You')
        break
    else:
        number = input('Please enter %s\'s number: ' % name)

        namelist.append(name)
        namedict[name] = number
        
        i += 1
        name = input('Please enter person %i\'s name: ' % i)

namelist.sort() #sort the names in alpha

lenlist = len(namelist) 
for j in range(lenlist):
    fileHandle.write(namelist[j] + ',' + namedict[namelist[j]] + '\n')

#close file
fileHandle.close()  

#---- End program ----
