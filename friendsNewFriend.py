#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 09:46:19 2018

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

friend = input('Enter the name of a new friend: ')
position = input('What position should %s appear in? ' % friend)

friendlist.insert(int(position)-1, friend)  #position-1 only because it's a little bit more intuitive to the user since list indices start at zero

print('--------------------------------------')
print('Your new friends are now:')

i = 0
while i < len(friendlist):
    print(friendlist[i])
    i += 1

#---- End Program ----