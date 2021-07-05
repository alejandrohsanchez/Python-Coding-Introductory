# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 17:37:52 2021

@author: Alejandro Sanchez
"""

# This class is meant to be imported

import math

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
        
class volCone:
    def __init__(self):
        pass
    
    def set_radius(self, radius):
        self.radius = radius
    
    def set_height(self, height):
        self.height = height
    
    def set_volume(self):
        self.volume = (math.pi * math.pow(self.radius, 2) * (self.height / 3))
        self.volume = round(self.volume, 2)
        
    def printVol(self):
        print("The volume is:", self.volume)