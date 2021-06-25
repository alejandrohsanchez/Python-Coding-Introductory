# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Creating a class called "Dog"
class Dog:
    
    # This a property called x
    x = 5
    
    
    # Initiating the class "Dog"
    # This will always execute when you create an object that calls this class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # always include "self" even if you don't need a parameter in the function
    def introduce(self):
        print("Hello, my name is " + self.name)
        

# d1 is an object
# this object will use the properties inside the class "Dog"
# When you do this, the code will always execute the __init__ method
d1 = Dog("Fred", 15)

# name is a property
print(d1.name)

# age is a property
print(d1.age)
d1.introduce()

# Reassigns the value of the age property in the class "Dog"
d1.age = 20

print(d1.age)

# This calls the property x inside of "Dog"
print(d1.x)

