#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 09:54:51 2018

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

position = input('Please enter the friend position to revoke: ')

notfriend = friendlist.pop(int(position)-1)  #position-1 only because it's a little bit more intuitive to the user since list indices start at zero

print('--------------------------------------')
print('%s is no longer your friend' % notfriend)
print()
print('Your friends are now:')

j = 0
while j < len(friendlist):
    print(friendlist[j])
    j += 1

#---- End Program ----