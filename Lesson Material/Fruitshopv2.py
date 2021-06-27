# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 02:18:43 2021

@author: Alejandro Sanchez
"""

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

taxRate = 0.08
total = 0

z = input('Would you like anything? (y/n) ')

if z == 'y':
    print('Welcome to the store!')
    
    total = promptFruit('bananas', banana, total)
    print('Your subtotal is --', total)
    
    total = promptFruit('oranges', orange, total)
    print('Your subtotal is --', total)
    
    total = promptFruit('apples', apple, total)
    print('Your subtotal is --', total)
    
    total = promptFruit('watermelons', watermelon, total)
    print('Your subtotal is --', total)
    
    total = promptFruit('durians', durian, total)
    print('Your subtotal is --', total)
    
    total = promptFruit('dragonfruits', dragonfruit, total)
    print('Your subtotal is --', total)
    
    total = promptFruit('grapes', grape, total)
    print('Your subtotal is --', total)
    
    print('Your total is', total, 'before taxes...')
    
    total = calcTax(total, taxRate)
    
    print('Your new total after taxes is', total)
    
elif z == 'n':
    print('Goodbye!')