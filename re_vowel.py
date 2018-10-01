#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 21:45:54 2018

@author: chakyu
"""
import re

#---- Start Program ----

vowellist = ['a', 'e', 'i', 'o', 'u']

sentence = input('Please enter something vacuous: ')
print('-------------------------------------------------------------------')

checkvowel = []
novowel = []
i = 0
while i < len(vowellist):
    if re.search('.*'+vowellist[i]+'.*', sentence, re.IGNORECASE):
        checkvowel.append(vowellist[i])
        i += 1
    else:
        novowel.append(vowellist[i])
        i += 1

if len(checkvowel) == len(vowellist):
    print(sentence)
else:
    j = 0
    while j < len(novowel):
        print('Input does not contain the vowel \'%s\'.' % novowel[j])
        j += 1

#---- End Program ----