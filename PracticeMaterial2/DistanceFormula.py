# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 00:42:30 2021

@author: Alejandro Sanchez
"""

import math

x1 = [1,1,1,1,1,1,1,1,1,1]
x2 = [1,2,3,4,5,6,7,8,9,10]
y1 = [1,1,1,1,1,1,1,1,1,1]
y2 = [2,4,6,8,10,12,14,16,18,20]

D = []
a = []

size = len(x1)

for i in range(size):
    D.append(math.sqrt(math.pow((x2[i] - x1[i]),2) + math.pow((y2[i] - y1[i]),2)))
    
print(D)

for i in range(size):
    a.append(math.sqrt())