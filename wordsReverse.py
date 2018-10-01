#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 09:09:44 2018

@author: chakyu
"""

#---- Start Program ----

sentence = input('Please enter a sentence: ')

#Split the sentence
words = sentence.split(' ')

#reverse the sentence
words.reverse()

#join words
space = ' '
revsent = space.join(words)

#print the reversed sentence
print(revsent)

#---- End Program ----