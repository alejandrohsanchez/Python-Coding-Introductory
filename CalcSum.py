# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:55:09 2021

@author: Alejandro Sanchez
"""

def calcSum(list1):
    size = len(list1)
    Sum = 0
    for i in range(size):
        Sum = Sum + list1[i]
    
    print(Sum)

list1 = [1, 3, 5, 7, 9, 11, 13, 15, 17]
calcSum(list1)