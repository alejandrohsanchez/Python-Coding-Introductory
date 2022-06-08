# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 17:23:01 2021

@author: Alejandro Sanchez
"""
import matplotlib.pyplot as plt

"""
commenting old code
fruitlist = ['banana', 'orange', 'apple', 'watermelon']

print(fruitlist)
# for loop
for x in fruitlist:
    print(x)
    
    if (x == 'apple'):
        print('this is an apple')
        
for x in range(1,11):
    print(x)


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

"""

"""
# This will continue printing '1' until we tell it to stop.
# Intro to while loop:

while (True):
    print("1")
    ans = input("Continue? (y for yes, n for no) ")
    
    # If the user enters the letter 'n', the while loop will stop.
    if (ans == 'n'):
        break
"""

"""
# This will continue adding numbers.
sum = 0
while (True):
    number = int(input("Enter a number: "))
    sum = sum + number
    print("Your number is", sum)
    
    ans = input("Continue? (y for yes, n for no) ")
    if (ans == 'n'):
        print("Your final sum is:", sum)
        break
"""    

