#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 15:51:11 2022

@author: alejandrosanchez
"""

import math as m

# Round a float to its upper whole number
number1 = 2.3
newNumber1 = m.ceil(number1)
print(newNumber1)

number2 = 2.3
newNumber2 = m.floor(number2)
print(newNumber2)

number3 = 4 % 3
print(number3)

print(m.fmod(7,3))

# Get the sum of numbers in a list (including integers and floats)
listA = [1,2,3,4.3,5,5,7,3,21,3,4,5,2,3,22,53,3,4,23,24,1]
print(m.fsum(listA))

