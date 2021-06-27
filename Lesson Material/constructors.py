# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:56:56 2021

@author: Alejandro Sanchez
"""

# Object-Oriented Programming (OOP)

class Introductions:
    
    def __init__(self, str1):
        self.Name = str1
        
    # Parameterized Constructor
    def printAge(self, age):
        self.age = age
        print("I am", self.age, "years old")
    
    # Default Constructor
    # This method does not take any arguments
    def introduce(self):
        print("Hello, my name is", self.Name)
        

# Creating object of the class "Introductions"
ajay = Introductions("John")

# Call the instance method using the object "intro"
ajay.introduce()

# Invoking Parameterized Constructor
ajay.printAge(44)

alex = Introductions("Doug")
alex.introduce()
alex.printAge(35)