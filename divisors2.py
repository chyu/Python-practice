#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 22:56:03 2018

@author: chakyu
"""

#---- Start Program ----

import re
import math

number = input('Please enter a number: ')

#---- check integer ----
while True:                                                                     #loops continuously until break
    if number.isdigit():                                                        #tests whether the string is a digit
        if re.search('\..*',number):                                            #if the string is a series of digits, then tests whether there is a decimal (i.e. indicating that it is a floating point number)
            number = input('Please enter a positive integer: ')                 #if the above tests true, then we need to input another number, specifically an integer
        else:                                                                   #if the conditional is false then that's great! But we need to convert the string into type integer
            number = int(number)                                                #converts number into an integer
            break                                                               #break the loop because we've got an integer! 
    else:                                                                       #if not a digit, then need to re-enter a number, specifically a digit
        number = input('Please enter a positive integer: ')                     #if not a digit, then please enter a positive integer

print('The divisors for the number %i are: ' % number)

#---- perform division ----
divisorlist1 = []
totaldivisors = []
i = 1                                                                           #establish a counter, but start from 1 because can't divide by zero
while i <= number:
    if i > math.sqrt(number):
        j = 0                                                                   #initialise j to start from zero because the counter is for looping through the list 'divisorlist'
        divisorlist1.reverse()                                                  #reverse the divisor to keep the total divisor list ordered
        while j < len(divisorlist1):                                            #looping through the divisor list
            
            if divisorlist1[j] != math.sqrt(number):                            #we don't want the program to repeat divisors in the case the number provided is a square number
                
                symmetricdivisor = int(number/divisorlist1[j])                  #find the symmetric divisor
                totaldivisors.append(symmetricdivisor)                          #append the symmetric divisor to the total divisors list. This is a totally optional thing
            
                print(symmetricdivisor)                                         #print the symmetric divisor on the screen
                j += 1                                                          #add 1 to the counter
            else:                                                               #when the entered number is indeed a square number
                j += 1                                                          #the only thing we need to do in this case is move the divisorlist1 counter by 1
        
        break                                                                   #once looped through the entire divisor list then game over; break the loop 
    else:
        if number % i == 0:                                                     #if dividing the number by the counter results in no remainder
            divisorlist1.append(i)                                              #add it to the list with the first half of divisors
            totaldivisors.append(i)                                             #add it to the total list of divisors. This is totally optional
            print(i)                                                            #print the divisor on the screen
            i += 1                                                              #move the counter by 1
        else:
            i += 1                                                              #even if false still need to move the counter by 1

#print(totaldivisors)

# --- End Program ---
