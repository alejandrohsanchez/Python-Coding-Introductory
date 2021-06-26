# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 21:08:52 2021

@author: Alejandro Sanchez
"""

import variables3 as v

def multiply(listA):
    total = 1
    for i in range(len(listA)):
        total = total * (listA[i])
    print(total)

multiply(v.listA)