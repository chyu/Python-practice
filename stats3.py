#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:55:27 2018

@author: chakyu
"""


#------DEFINE FUNCTION------
#------Function checks that the input is actually a digit------
def checkdigit(number, numtest, counter):
    while type(number) != float:                                                #basically keeps looping until it's happy that type is float
        if numtest.isdigit():                                                   #checks whether the number is actually a digit
            number = float(number)                                              #if it is, then turn number into type float
            break                                                               #if it's a float then break out of the loop
        else:                                                                   #if type is not a float then it means it's not a number                           
            number = input('Number %i: ' % counter)                             #therefore force user to input an actual number. keeps looping until a digit is entered
    return number                                                               #end function

#------START PROGRAM-------

number = print('Please enter ten numbers: ')                                    #enter a bunch of numbers
numberlist = []                                                                 #create an empty list that will be populated later on
maxn = 0
minn = 0
i = 1                                                                           #start counter
while i <= 10:                                                                  #loop 10 times per the stated requirement
    
    number = input('Number %i: ' % i)                                           #input the enter
    numtest = number                                                            #take the number and put it into another variable. this one will be modified in order to run through the check digit process
    
    if type(numtest.find('.')) == int and type(numtest.find('-')) == int:       #condition 1: the number entered is both negative and a decimal. since the entry is a string by default we need to search fand replace the decimal point and hypen
        numtest = numtest.replace('.','')                                       #replace decimal
        numtest = numtest.replace('-','')                                       #replace negative sign
        
        #----check digit----                    
        number = checkdigit(number, numtest, i)                                 #now we can check digit
        numberlist.append(number)                                               #once check digit is complete, we can append the number to the list 
        i += 1                                                                  #move the counter by one
        
        if number >= maxn:                                                      #maximum number test
            maxn = number
        elif number <= minn:                                                    #minimum number test
            minn = number
            
    elif type(numtest.find('.')) == int:                                        #condition 2: the number entered is a postive decimal
        numtest = numtest.replace('.','')                                       #replace decimal point
        
        #----check digit----                     
        number = checkdigit(number, numtest, i)                                 #check digit
        numberlist.append(number)                                               #check complete; append number
        i += 1                                                                  #move counter
        
        if number >= maxn:
            maxn = number
        elif number <= minn:
            minn = number
            
    elif type(numtest.find('-')) == int:                                        #condition 3: the number is a negative integer
        numtest = numtest.replace('-','')                                       #replace negative sign
        
        #----check digit----
        number = checkdigit(number, numtest, i)                                 #check digit
        numberlist.append(number)                                               #append number to list
        i += 1                                                                  #move counter
        
        if number >= maxn:
            maxn = number
        elif number <= minn:
            minn = number
            
#------CALCULATE STATISTICS------
 
print()                                                                         #prints an empty line. for aesthetic purposes only
print('Statistics')                                                             #prints heading
print('---------------------------------------------------------')              #prints separator for readability
print('The largest number entered is %.2f' % maxn)                              #prints the largest number
print('The smallest number entered is %.2f' % minn)                             #prints the smallest number


#------END PROGRAM-------