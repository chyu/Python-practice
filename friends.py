#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 09:29:49 2018

@author: chakyu
"""

#---- Start Program ----

friend = input('Enter the name of a friend: ')
friendlist = []
friendlist.append(friend)

while True:
    
    if friend == '':
        friendlist.pop()
        break
    else:
        friend = input('Enter the name of a friend: ')
        friendlist.append(friend)

#print list of friends
print('--------------------------------------')
print('You have %i friends' % len(friendlist))
print()
print('Your friends are: ')

i = 0
while i < len(friendlist):
    print(friendlist[i])
    i += 1


#---- End Program ----