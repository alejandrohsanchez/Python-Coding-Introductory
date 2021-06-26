# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 17:13:52 2021

@author: Alejandro Sanchez
"""
# Remember that when creating functions, the name of the function does not matter. We can name it whatever we want. Functions can
# either perform code or return a specific value (or both)

# ---- REVIEW OF FUNCTIONS THAT DO NOT RETURN VALUES ---- #

# This creataes a function called 'sampleFunct' that contains no parameters. This function prints 'Hello'
def sampleFunct():
    print('Hello')

# This function takes in an integer for its parameter and prints it out. Remember that 'x' is a variable we can make up
# This variable can also be named 'a' or 'num1'.
def printInteger(x):
    print(x)

# This function takes in two arguments and prints them out separately. Remember that 'x' and 'y' are some arbitrary variables that
# we made up
def printTwoInt(x,y):
    print(x)
    print(y)

# This function takes the sum of two arguments (both integers) and prints it out
def calcSum(x,y):
    Sum = x + y
    print(Sum)

# This function takes a list as an argument and prints out the list on one line
def printList(listA):
    print(listA)

# This function takes a list as an argument and prints out the values in the list one-by-one
def printListValues(listA):
    size = len(listA)
    for i in range(size):
        print(listA[i])

# This function prints out the first number in a list give a list as an argument
def printFirstNum(listA):
    print(listA[0])


# ---- REVIEW OF FUNCTIONS THAT RETURN VALUES ---- #

# This function does not take any arguments but returns the value 1
def returnOne():
    return 1

# This function takes in an integer as an argument and prints out two times its value. Remember that 'x' and 'returnVal' are arbitrary
# variable that we could have named anything else, such as 'val1' or 'Num5', etc.
def multTwo(x):
    returnVal = (2 * x)
    return (returnVal)

# This function imports a file and uses the variables from that file. This function calls the variable x defined in variables1.py by
# using variables1.x. It prints this value out
def importTest1():
    # import variables1
    # print(variables1.x)
    print('This function prints variable x from variables1.py')

# importing numpy to a program
import numpy as np

# Creating an array using np.array
x = np.array([1, 2, 3, 4, 5])