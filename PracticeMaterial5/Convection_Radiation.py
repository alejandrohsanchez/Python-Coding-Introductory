# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 05:27:59 2021

@author: Alejandro Sanchez
"""

import math

class Convection:
    
    def __init__(self):
        self.flux = 0
    
    def set_transfer_coef(self, h):
        self.transfer_coef = h
    
    def set_surface_temp(self, Ts):
        self.surface_temp = Ts
        
    def set_surrounding_temp(self, Tsur):
        self.surrounding_temp = Tsur
        
    def set_diameter(self, D):
        self.diameter = D

    def calc_heat_flux(self):
        self.flux = self.transfer_coef * (self.surface_temp - self.surrounding_temp) * (math.pi * self.diameter)
    
    def disp_heat_flux(self):
        if (self.flux):
            print(self.flux)
        else:
            print("Heat flux has not been calculated!")


class Radiation:
    
    def __init__(self):
        self.flux = 0
    
    def set_emissivity(self, epsilon):
        self.epsilon = epsilon
    
    def set_stefan_boltzmann(self, sigma):
        self.sigma = sigma
    
    def set_surface_temp(self, Ts):
        self.surface_temp = Ts
        
    def set_surrounding_temp(self, Tsur):
        self.surrounding_temp = Tsur
    
    def set_diameter(self, D):
        self.diameter = D

    def calc_heat_flux(self):
        self.flux = (self.epsilon * self.sigma * (math.pow(self.surface_temp, 4) - math.pow(self.surrounding_temp, 4))) * (math.pi * self.diameter)
    
    def disp_heat_flux(self):
        if (self.flux):
            print(self.flux)
        else:
            print("Heat flux has not been calculated!")

def calc_Convection(h, Ts, Tsur, D):
    conv = Convection()
    
    conv.set_transfer_coef(h)
    conv.set_surface_temp(Ts)
    conv.set_surrounding_temp(Tsur)
    conv.set_diameter(D)
    
    conv.calc_heat_flux()
    conv.disp_heat_flux()

def calc_Radiation(epsilon, sigma, Ts, Tsur, D):
    rad = Radiation()
    
    rad.set_emissivity(epsilon)
    rad.set_stefan_boltzmann(sigma)
    rad.set_surface_temp(Ts)
    rad.set_surrounding_temp(Tsur)
    rad.set_diameter(D)
    
    rad.calc_heat_flux()
    rad.disp_heat_flux()



h = 10
Ts = 353
Tsur = 293
D = 0.020
sigma = 5.67 * math.pow(10,-8)
epsilon = 1

calc_Convection(h, Ts, Tsur, D)
calc_Radiation(epsilon, sigma, Ts, Tsur, D)
