#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 14:45:34 2018

@author: chakyu
"""

#---- Creating files ----

fileHandle = open('namesfixed.csv', 'w')

print('Welcome to the phone number program')

name = input('Please enter person\'s name: ')

while True:

    if name == '':
        print()
        print('-'*50)
        print('No more names entered. Program will cease and file will be closed.')
        print('Thank You')
        fileHandle.close()  
        break
    else:
        number = input('Please enter %s\'s number: ' % name)
        fileHandle.write(name.ljust(10) + number.ljust(15) + '\n')

        name = input('Please enter person\'s name: ')

#---- End program ----
