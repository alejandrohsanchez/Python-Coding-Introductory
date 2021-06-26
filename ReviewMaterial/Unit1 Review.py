# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 19:44:28 2021

@author: Alejandro Sanchez
"""

# REVIEW OF FIRST UNIT
import matplotlib.pyplot as plt
import math

# Setting a variable equal to a string
string1 = 'my string'

# Setting a variable equal to an integer
integer1 = 5

# Creating a new empty list called 'a'
a = []

# Creating a new list with 3 numbers in it
b = [1,2,3]

# Creating a new list with 5 ones in it
c = [1] * 5

# Creating a new list with 3 letters in it
d = ['a','b','c']

# Creating a new list called 'num' and adding the number 2 to it
num = []
num.append(2)

# Getting the size of a list using len() and saving the size into a variable called 'N'
someList = [1,2,3,4,5,6]
N = len(someList)

# Using a for loop to print "Hello" 5 times
for i in range(5):
    print('Hello')

# Using a for loop to add ones to an empty list called 'list1' 5 times
list1 = []
for i in range(5):
    list1.append(1)


# Using a for loop to print out all the values in a list called 'list2' of size 5 one-by-one
list2 = [1,2,3,4,5]
size1 = len(list2)
for i in range(size1):
    print(list2[i])

# Using a for loop to update all the values in a pre-existing list to be ones
existingList = [4,3,2,1,2,3,4]
size2 = len(existingList)
for i in range(size2):
    existingList[i] = 1

# Taking a variable that has a value of 2 and raising its value to the power of 2 with math.pow(x,y) (squaring a number)
a = 4
b = math.pow(a,2)
# now, b = 16

# Taking the square root of a number stored in a variable with math.sqrt()
a = 16
b = math.sqrt(a)
# now, b = 4
    
# Using a for loop to update all the values in a pre-existing list to be raised to the power of 2 (squaring them all)
existingList2 = [1,2,3,4,5]
size3 = len(existingList2)
for i in range(size3):
    existingList2[i] = math.pow(existingList2[i], 2)

# Using a for loop to update all the values in a pre-existing list to be square-rooted
existingList3 = [1,4,9,16,25]
size4 = len(existingList3)
for i in range(size4):
    existingList3[i] = math.sqrt(existingList3[i])

# Adding 1 to all the values in a pre-existing list
list3 = [1,2,3,4,5]
size = len(list3)
for i in range(size):
    list3[i] = (list3[i] + 1)

# Creating a line plot using plt.plot(x,y) given two sets of values (x values and y values)
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.show() # This creates the figure that our plot will be graphed on
plt.plot(x,y)

# Labeling a plot's axes
plt.xlabel('x label')
plt.ylabel('y label')

# Creating a plot legend
plt.legend(['This is a legend'])
