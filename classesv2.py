# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:31:51 2021

@author: Alejandro Sanchez
"""

class Operations:
    
    def __init__(self, int1, int2):
        self.int1 = int1
        self.int2 = int2

    def printSum(self):
        x = self.int1 + self.int2
        print("The sum is: ", x)
    
    def printMax(self):
        if (self.int1 > self.int2):
            print("The max is: ", self.int1)
        else:
            print("The max is: ", self.int2)
    
    def printMult(self):
        y = self.int1 * self.int2
        print("The product is: ", y)
        

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

op = Operations(a, b)
op.printSum()
op.printMax()
op.printMult()