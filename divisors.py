#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:53:28 2018

@author: chakyu
"""

# --- Start Program ---

import re


number = input('Please enter a number: ')

#check integer
while True:                                                                     #loops continuously until break
    if number.isdigit():                                                        #tests whether the string is a digit
        if re.search('\..*',number):                                            #if the string is a series of digits, then tests whether there is a decimal (i.e. indicating that it is a floating point number)
            number = input('Please enter a positive integer: ')                 #if the above tests true, then we need to input another number, specifically an integer
        else:                                                                   #if the conditional is false then that's great! But we need to convert the string into type integer
            number = int(number)                                                #converts number into an integer
            #break the loop because we've got an integer!                                                                    
            break
    else:                                                                       #if not a digit, then need to re-enter a number, specifically a digit
        number = input('Please enter a positive integer: ')                     #if not a digit, then please enter a positive integer

#perform division

i = 1                                                                           #establish a counter, but start from 1 because can't divide by zero
while i <= number:
    if number % i == 0:                                                         #if dividing the number by the counter results in no remainder
        print(i)                                                                #if true, then i is a divisor
        i += 1                                                                  #move the counter by 1
    else:
        i += 1                                                                  #even if false still need to move the counter by 1





# --- End Program ---