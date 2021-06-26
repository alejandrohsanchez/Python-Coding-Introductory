# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:52:28 2021

@author: Alejandro Sanchez
"""
import math

g = 9.81

v0 = int(input('Enter the initial launch velocity (m/s): '))

theta = int(input('Enter the initial launch angle (degrees): '))

theta = math.radians(theta)

R = (math.pow(v0, 2) * math.sin(2 * theta)) / g

vx0 = v0 * math.cos(theta)

vy0 = v0 * math.sin(theta)

t = R / vx0

t_half = t / 2

h = (vy0 * t_half) - (0.5 * g * math.pow(t_half, 2))

print('Calculating...')
print('Range: ', R)
print('Air time: ', t)
print('Maximum height: ', h)