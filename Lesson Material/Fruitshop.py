# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 16:23:54 2021

@author: Alejandro Sanchez
"""

# Prices of fruit
banana = 2
orange = 1
apple = 3
watermelon = 5
total = 0

"""
# if else
if banana < watermelon:
    # if the value of banana is less than watermelon
    print('banana is less than watermelon')
elif banana == watermelon:
    print('banana is the same as watermelon')
else:
    print('banana is greater than watermelon')

"""

z = input('Would you like anything? (y/n) ')

if z == 'y':
    print('Welcome to the store!')
    t = input('Would you like bananas? (y/n) ')
    if t == 'y':
        u = int(input('How many bananas? '))
        total = total + (u * banana)
    
    t = input('Would you like oranges? (y/n) ')
    if t == 'y':
        u = int(input('How many oranges? '))
        total = total + (u * orange)
        
    t = input('Would you like apples? (y/n) ')
    if t == 'y':
        u = int(input('How many apples? '))
        total = total + (u * apple)
        
    t = input('Would you like watermelon? (y/n) ')
    if t == 'y':
        u = int(input('How many watermelons? '))
        total = total + (u * watermelon)
        
    print('Your total is', total)
    
elif z == 'n':
    print('Goodbye!')