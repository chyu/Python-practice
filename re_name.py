#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:52:33 2018

@author: chakyu
"""

import re

# --- Start Program ---

someinput = input('Enter your meaningless sentence here: ')
myname = 'chak'

if re.search(myname, someinput, re.IGNORECASE):
    print('awwww... you\'re thinking of me :)')
else: 
    print('what do you mean you\'re not talking about me! ><')

# --- End Program ---