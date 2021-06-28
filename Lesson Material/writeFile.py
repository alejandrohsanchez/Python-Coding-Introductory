# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 10:33:22 2021

@author: Alejandro Sanchez
"""

# "a" means append. We will begin appending to the end of the file
f = open("WriteFileExample.txt", "a")

# Adding a "\n" to the write function, the written line appended
# will be on a new line
f.write("\nThis will be written on a new line!")
f.close()

# Open and read the file after the appending
f = open("WriteFileExample.txt", "r")
print(f.read())
f.close()