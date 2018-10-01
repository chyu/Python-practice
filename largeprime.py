#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 21:45:13 2018

@author: chakyu
"""

# --- Start Program ---

primetest = int(1000004)

#perform factorisation (brute force method)

while True:
    
    i = 2   #must start from two (this will reset with every new increase in primetest)                                                                        
    while i < primetest:  #the counter between 2 and primetest - 1 (because definition of a prime)
        
        if primetest % i == 0:  #if there is no remainder, then primetest cannot be prime
            
            #break being in the current loop
            break                                                                
        else:   #if there is a remainder than i is not a factor. continue to the next i
            i += 1  #iterate to next i                                                                 

    if i >= primetest: #if the above while loop finishes without finding a factor than you've got a prime
        print(primetest)    #print the prime!
        break   #the game is over! break loop
    else:   #tests for the case where the nested loop broke early, so therefore i must be less than 
            #primetest. In this case we haven't found the prime yet so we need to increase primetest by 1
        primetest += 1  #move to the next potential prime number




# --- End Program ---