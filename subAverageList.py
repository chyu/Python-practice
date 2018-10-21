#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 22:05:54 2018

@author: chakyu
"""

#---- Start Program ----

#---- Start calc average function ----

def calcAverage(numlist):
    average = sum(numlist)/len(numlist)
    return average

#---- End calc average function ----

num = input('Please enter several numbers. Number 1 is: ')
numlist = []
i = 2
while True:
    if num == '':
        break
    else:
        num = float(num)
        numlist.append(num)
        num = input('Please enter number %i: ' % i)
        i += 1
print('-'*50)
print('The average of these numbers is %.3f ' % calcAverage(numlist))


#---- End Program ----