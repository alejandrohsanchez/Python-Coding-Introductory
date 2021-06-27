# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 18:29:27 2021

@author: Alejandro Sanchez
"""

import fruitshoputil as util

total = 0

z = input('Would you like anything? (y/n) ')

if z == 'y':
    print('Welcome to the store!')
    
    total = util.promptFruit('bananas', util.banana, total)
    print('Your subtotal is --', total)
    
    total = util.promptFruit('oranges', util.orange, total)
    print('Your subtotal is --', total)
    
    total = util.promptFruit('apples', util.apple, total)
    print('Your subtotal is --', total)
    
    total = util.promptFruit('watermelons', util.watermelon, total)
    print('Your subtotal is --', total)
    
    total = util.promptFruit('durians', util.durian, total)
    print('Your subtotal is --', total)
    
    total = util.promptFruit('dragonfruits', util.dragonfruit, total)
    print('Your subtotal is --', total)
    
    total = util.promptFruit('grapes', util.grape, total)
    print('Your subtotal is --', total)
    
    print('Your total is', total, 'before taxes...')
    
    total = util.calcTax(total, util.taxRate)
    
    print('Your new total after taxes is', total)
    
elif z == 'n':
    print('Goodbye!')