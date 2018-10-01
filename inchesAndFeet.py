#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:24:40 2018

@author: chakyu
"""


#----- Start Program -----


print('Inches \t\t Feet/Inches \t\t Centimetres')

i = 0 # loop counter
while i <= 20:

    ft = i/12
    remi = i % 12
    
    cm = i*2.54
 
    print('%.1f \t\t %i / %.1f \t\t %.2f' % (i,ft,remi,cm))
    i += 1





#----- End Program -----