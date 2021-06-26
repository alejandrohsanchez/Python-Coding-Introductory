# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 19:55:20 2021

@author: Alejandro Sanchez
"""

# PART 1 - These are the variables for Exercise 1
listA= [3, 1, 4, 2, 5, 3, 6, 4, 7, 5, 8, 6, 9, 7]

# PART 2 - This is the list used for Exercise 2
listB = [4, -11, 1, -4, 91, -47, 14, 9, 13, 54, 24, -65, 86, 243, 23, -221, 365, 624, -324, 154, 264, -4234, 3123, -6553, 7865, 7676, -87, 1298, -22178, 578, 45, 65, -3]

# PART 3
# importedFunction accepts an integer as a parameter called 'x'
def importedFunction(x):
    print(x)
    if (x%2 == 0):
        print('importedFunction says that this number is even')
    elif (x%2 == 1):
        print('importedFunction says that this number is odd')


# PART 4 - You will need to import these lists to perform the distance formula
x1 = [1,11,22,33,44,55,66,77,88,99,110]
y1 = [70,62,54,46,38,30,22,14,6,-2,-10]

x2 = [0,0,0,0,0,0,0,0,0,0,0]
y2 = [0,0,0,0,0,0,0,0,0,0,0]