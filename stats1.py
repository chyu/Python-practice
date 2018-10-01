#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 11:33:46 2018

@author: chakyu
"""

#------DEFINE FUNCTION------
#------Function checks that the input is actually a digit------
def checkdigit(number, numtest, counter):
    while type(number) != float:                        #basically keeps looping until it's happy that type is float
        if numtest.isdigit():                           #checks whether the number is actually a digit
            number = float(number)                      #if it is, then turn number into type float
            break                                       #if it's a float then break out of the loop
        else:                                           #if type is not a float then it means it's not a number                           
            number = input('Number %i: ' % counter)     #therefore force user to input an actual number. keeps looping until a digit is entered
    return number                                       #end function

#------START PROGRAM-------

number = print('Please enter ten numbers: ')            #enter a bunch of numbers
numberlist = []                                         #create an empty list that will be populated later on
i = 1                                                   #start counter
while i <= 10:                                          #loop 10 times per the stated requirement
    
    number = input('Number %i: ' % i)                   #input the enter
    numtest = number                                    #take the number and put it into another variable. this one will be modified in order to run through the check digit process
    
    if type(numtest.find('.')) == int and type(numtest.find('-')) == int:       #condition 1: the number entered is both negative and a decimal. since the entry is a string by default we need to search fand replace the decimal point and hypen
        numtest = numtest.replace('.','')               #replace decimal
        numtest = numtest.replace('-','')               #replace negative sign
        
        #----check digit----                    
        number = checkdigit(number, numtest, i)         #now we can check digit
        numberlist.append(number)                       #once check digit is complete, we can append the number to the list 
        i += 1                                          #move the counter by one
        
    elif type(numtest.find('.')) == int:                #condition 2: the number entered is a postive decimal
        numtest = numtest.replace('.','')               #replace decimal point
        
        #----check digit----                     
        number = checkdigit(number, numtest, i)         #check digit
        numberlist.append(number)                       #check complete; append number
        i += 1                                          #move counter
        
    elif type(numtest.find('-')) == int:                #condition 3: the number is a negative integer
        numtest = numtest.replace('-','')               #replace negative sign
        
        #----check digit----
        number = checkdigit(number, numtest, i)         #check digit
        numberlist.append(number)                       #append number to list
        i += 1                                          #move counter

#------CALCULATE STATISTICS------
        
if numberlist == []:                                    #check whether number list is empty. True means empty list so no numbers entered, therefore nothing to do
    print('No numbers have been entered. Please restart program')               #just an information header
else:                                                   #list is not empty; therefore numbers exist!
    listlength = len(numberlist)                        #this is for the loop
    j = 0                                               #initialise counter
    cumtotal = 0                                        #initialise cumulative total
    while j < listlength:                               #start loop. while less than the length of the list
        cumtotal = cumtotal + numberlist[j]             #calculate the running total as you add the numbers inside the list
        j += 1                                          #move the counter
         
    listaverage = cumtotal/listlength                   #calculate average
    print()                                             #prints an empty line. for aesthetic purposes only
    print('Statistics')                                 #prints heading
    print('---------------------------------------------------------')          #prints separator for readability
    print('The total is: %.3f' % cumtotal)              #prints the cumulative total
    print('The average of the entered numbers is: %.3f' % listaverage)          #prints the average of the list


#------END PROGRAM-------