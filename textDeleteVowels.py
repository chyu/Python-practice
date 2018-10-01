#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:06:29 2018

@author: chakyu
"""

#---- Start Program ----

sentence = input('Enter a sentence: ')
sentence = sentence.lower()

vowellist = ['a', 'e', 'i', 'o', 'u']

v = 0
while v < len(vowellist):
    sentence = sentence.replace(vowellist[v],'')
    v += 1
    
print(sentence)

#---- End Program ----