# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 17:42:44 2021

@author: Alejandro Sanchez
"""

# This is the list
# This program will search for the largest integer in the list
a = [4, 8, 21, 87, -23, 0, 43]
size = len(a)

max_num = a[0]

for i in range(size):
    if a[i] > max_num:
        max_num = a[i]
    
print(max_num)

