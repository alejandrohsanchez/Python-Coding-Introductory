# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 17:23:01 2021

@author: Alejandro Sanchez
"""
import matplotlib.pyplot as plt

fruitlist = ['banana', 'orange', 'apple', 'watermelon']

"""
print(fruitlist)
# for loop
for x in fruitlist:
    print(x)
    
    if (x == 'apple'):
        print('this is an apple')
        
for x in range(1,11):
    print(x)

"""

x = []
y = []
z = []

for i in range(-100,101):
    x.append(i)
    
for j in x:
    y.append(j * j)
    
for k in x:
    if k == 0:
        z.append(0)
    else:
        z.append(1/ k)
    
plt.show()
plt.plot(x,y)

plt.show()
plt.plot(x,z)