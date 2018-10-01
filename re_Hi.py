#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 19:11:06 2018

@author: chakyu
"""

import re

# --- Start Program ---

someinput = input('Enter your meaningless sentence here: ')
keyword = 'hi'

if re.match(keyword, someinput, re.IGNORECASE):
    print('awwww... you said %s :)' % keyword)
else: 
    print('so rude! ><')

# --- End Program ---
