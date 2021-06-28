# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 09:16:52 2021

@author: Alejandro Sanchez
"""

listA = [2, 6, 1, 8, 2, 11, 17, -4, 8, 1, 11]

singles = []

size = len(listA)

for i in range(size):
    counter = 0
    single = listA[i]
    
    for j in range(size):
        if (single == listA[j]):
            counter = counter + 1
    
    if (counter == 1):
        singles.append(single)

print("The singles are: ", singles)