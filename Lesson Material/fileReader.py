# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 10:00:26 2021

@author: Alejandro Sanchez
"""

# This is reading from a text file called "Helloworld.txt"
f = open("Helloworld.txt", "r")

# reads the entire file
print(f.read())


# Read lines of the file
#print(f.readline())
#print(f.readline())

# This will close the file when we are finished with it.
f.close()