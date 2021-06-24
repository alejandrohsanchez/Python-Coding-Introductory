# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 21:33:48 2021

@author: Alejandro Sanchez
"""

import matplotlib.pyplot as plt

x = []
y = []

for i in range(-10,11):
    x.append(i)

for i in x:
    y.append(i * i * i)

plt.plot(x,y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('y = x^3')