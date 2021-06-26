# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 16:21:10 2021

@author: Alejandro Sanchez
"""


import math

class Projectile:
    
    def __init__(self, v, theta):
        self.v0 = v
        self.theta = math.radians(theta)
        self.g = 9.81
    
    def components(self):
        print("Calculating...")
        self.vx0 = self.v0 * math.cos(self.theta)
        self.vy0 = self.v0 * math.sin(self.theta)
        
    def printRange(self):
        self.Range = (math.pow(self.v0, 2) * math.sin(2 * self.theta)) / self.g
        print("Range: ", self.Range)
    
    def printAirtime(self):
        self.airtime = self.Range / self.vx0
        print("Air time: ", self.airtime)
    
    def printMaxheight(self):
        self.maxHeight = (self.vy0 * (self.airtime / 2)) - (0.5 * self.g * math.pow((self.airtime / 2), 2))
        print("Maximum height: ", self.maxHeight)