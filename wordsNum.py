#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 09:00:51 2018

@author: chakyu
"""

#---- Start Program ----

sentence = input('Please enter a sentence of your choice: ')


splitsentence = sentence.split(' ')

#number of names in the sentence
numwords = len(splitsentence)

#print the number of words
print('There are %i words in the sentence.' % numwords)




#---- End Program ----