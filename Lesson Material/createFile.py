# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 10:43:19 2021

@author: Alejandro Sanchez
"""

# "x" is used to create a file. Returns an error if the file exists
# f = open("CreatedFile.txt", "x")
# f.close()
# Commented this section out because Python will error if 
# we attempt to create a file that already exists

# "w" is overwriting the "CreatedFile.txt" text file with
# the following two lines of code
f = open("CreatedFile.txt", "w")
f.write("This is the first line")
f.write("\nThis is the second line")
f.close()