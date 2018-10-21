#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:02:24 2018

@author: chakyu
"""

#---- Start program ----

import os

filenames = os.listdir('.')

count = 0
for filename in filenames:
    print(filename)
    count += 1
    
print(count)

#---- End program ----