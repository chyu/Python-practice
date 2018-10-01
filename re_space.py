#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:16:37 2018

@author: chakyu
"""

import re

# --- Start Program ---

someinput = input('Enter your meaningless sentence here: ')
firstname = 'chak'
lastname = 'yu'

if re.search(' *chak *yu *', someinput, re.IGNORECASE):
    print('awwww... you\'re thinking of me :)')
else: 
    print('what do you mean you\'re not talking about me! ><')

# --- End Program ---