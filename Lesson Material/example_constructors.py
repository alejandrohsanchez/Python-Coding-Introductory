# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 17:17:35 2021

@author: Alejandro Sanchez
"""

# This program calculates the volume of a cube using constructors

class volCube:
    def __init__(self):
        pass
    
    def set_length(self, length):
        self.length = length
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def set_volume(self):
        self.volume = self.length * self.width * self.height
        
    def printVol(self):
        print("The volume is:", self.volume)
        

length = 5
width = 3
height = 2

vol_1 = volCube()

vol_1.set_length(length)
vol_1.set_width(width)
vol_1.set_height(height)
vol_1.set_volume()

vol_1.printVol()