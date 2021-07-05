# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 09:51:43 2021

@author: Alejandro Sanchez
"""

f = open("3_Names_and_PhoneNumbers.txt", "r")

x = f.readlines()
for i in range(10):
    if (x[i] == "END"):
        break
    else:
        print(x[i])

f.close()