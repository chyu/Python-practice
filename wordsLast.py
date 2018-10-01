#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 09:07:37 2018

@author: chakyu
"""

#---- Start Program ----

sentence = input('Please enter a sentence of your choice: ')


splitsentence = sentence.split(' ')

#number of names in the sentence
lastword = splitsentence[-1]

#print the number of words
print('The last word in the sentence is \'%s\'.' % lastword)

#---- End Program ----