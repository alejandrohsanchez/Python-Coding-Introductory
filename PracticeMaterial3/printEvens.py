# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 21:13:58 2021

@author: Alejandro Sanchez
"""

import variables3 as v

def findEvens(listB):
    for i in range(len(listB)):
        if (listB[i]%2 == 0):
            if (listB[i] > 0):
                print(listB[i])

findEvens(v.listB)