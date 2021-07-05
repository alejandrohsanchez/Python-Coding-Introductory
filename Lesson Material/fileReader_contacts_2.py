# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 10:29:21 2021

@author: Alejandro Sanchez
"""

names_set_1 = open("Names_to_Use_1.txt", "r")
numbers_set_1 = open("Numbers_to_Use_1.txt", "r")

# Need 'splitlines()' because 'readlines()' keeps the 'newline' at the end of each line.
# 'splitlines()' gets rid of the new line at the end of each line.
# Useful for printing lines on the same line as each other.
names = names_set_1.read().splitlines()
numbers = numbers_set_1.read().splitlines()

for i in range(10):
    if (names[i] == "END"):
        break
    else:
        print(names[i], "- - - -",numbers[i])

