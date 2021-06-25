# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 00:42:54 2021

@author: Alejandro Sanchez
"""

import math
import matplotlib.pyplot as plt

x2 = [1,2,3,4,5,6,7,8,9,10]
y2 = [2,4,6,8,10,12,14,16,18,20]
size = len(x2)

plt.show()
plt.plot(x2,y2)
plt.title('Title')
plt.legend(['Plot 1'])
plt.xlabel('x axis')
plt.ylabel('y axis')

for i in range(size):
    x2[i] = x2[i] * 5
    y2[i] = math.sqrt(y2[i])

plt.show()
plt.plot(x2,y2)
plt.title('Title')
plt.legend(['Plot 1'])
plt.xlabel('x axis')
plt.ylabel('y axis')