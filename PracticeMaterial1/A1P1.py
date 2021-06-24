# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 21:18:51 2021

@author: Alejandro Sanchez
"""

print('Please enter a number: ')
x = int(input())

if (x % 2 == 0):
    print('You entered an even number.')
elif (x % 2 == 1):
    print('You entered an odd number.')