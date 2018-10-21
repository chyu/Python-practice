#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:19:10 2018

@author: chakyu
"""

#---- Start program ----

import os

cwd = os.getcwd()
#print('The current working director is: %s' % cwd)

#make directory
os.mkdir('Life')

#change directory
os.chdir('./Life')

filehandle = open('TheMeaningOfLife.txt', 'w')

filehandle.write('Well, it\'s nothing very special. \
                 Uh, try and be nice to people, avoid \
                 eating fat, read a good book every now \
                 and then, get some walking in, and try \
                 live together in peace and harmony \
                 with people of all creeds and nations.')

#finish editing file
filehandle.close()

#rename file
os.rename('TheMeaningOfLife.txt', 'TheMeaningOfLife.bak')

#remove file
os.remove('TheMeaningOfLife.bak')

#change to previous directory
os.chdir('..')
cwd = os.getcwd()
print('The current working directory is: %s' % cwd)

#remove 'Life' directory
os.rmdir('Life')

#---- End Program ----