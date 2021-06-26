# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 21:25:50 2021

@author: Alejandro Sanchez
"""
import math
import variables3 as v

D = []

for i in range(len(v.x1)):
    D.append(math.sqrt(math.pow((v.x2[i] - v.x1[i]),2) + math.pow((v.y2[i] - v.y1[i]),2)))
    
print(D)