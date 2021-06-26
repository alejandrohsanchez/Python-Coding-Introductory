# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 15:56:17 2021

@author: Alejandro Sanchez
"""

import projectileMotion as pm


v = int(input("Enter the initial launch velocity (m/s): "))
t = int(input("Enter the initial launch angle (degrees): "))

p = pm.Projectile(v, t)

p.components()
p.printRange()
p.printAirtime()
p.printMaxheight()