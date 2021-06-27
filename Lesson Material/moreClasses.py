# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 19:16:54 2021

@author: Alejandro Sanchez
"""

# This is the parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printName(self):
        print(self.firstname, self.lastname)

# This is a child class. It inherits properties from the "Person" class
class Student(Person):
    def __init__(self, fname, lname, year):
        # super will allow Student to inherit the properties in the class "Person"
        # Those properties include self.firstname and self.lastname
        super().__init__(fname, lname)
        self.graduationyear = year


x = Person("Alejandro", "Sanchez")
x.printName()

# Student uses "Person" class
p = Student("Ajay", "Singh", 2025)
p.printName()

x = Student("Mike", "Tyson", 2000)

x.printName()

