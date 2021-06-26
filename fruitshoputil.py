# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 18:27:38 2021

@author: Alejandro Sanchez
"""

# Utility functions
def subTotal(total, quantity, price):
    total = total + (quantity * price)
    return total

def promptFruit(name, price, total):
    print('Would you like', name, '(y/n)')
    t = input()
    
    if (t == 'y'):
        print('How many', name)
        u = int(input())
        total = subTotal(total, u, price)
        return total
    else:
        return 0

def calcTax(total,taxRate):
    temp = total * taxRate
    total = total + temp
    return total

# Prices of fruit
banana = 2
orange = 1
apple = 3
watermelon = 5
durian = 15
dragonfruit = 30
grape = 12

taxRate = 0.05
total = 0