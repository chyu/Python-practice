#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:00:48 2018

@author: chakyu
"""

#---- Start Program ----

sentence = input('Enter a sentence: ')
sentence = sentence.lower()
myname = 'Chak'
myname = myname.lower()

if myname in sentence:
    print('Hello my lord!')
else:
    print('So rude...')

#---- End Program ----