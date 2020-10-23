# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 23:56:40 2020

@author: egayu
"""


#CLASSES AND OBJECTS
print("CLASSES AND OBJECTS")
class MyClass:
    a = 10
    b = 20
    
    def add(self):
        sum = self.a + self.b
        print(sum)
        
obj = MyClass()
print(obj.a, obj.b)
obj.add()

class cons:
    
    def __init__(self, a, b):
        self.sum = a + b
    
    def printsum(self):
        print("Consructor sum: ", self.sum)
        
ob = cons(2,3)
ob.printsum()

# POLYMORPHISM - METHOD OVERLOADING

def area(r):
    return 3.14*r**2

def area(l,b):
    return l*b

#print(area(2))
print(area(2,3))

'''
Method overloading is not supported in Python, 
because if we see in the above example 
we have defined two functions 
with the same name ‘area’ 
but with a different number of parameters.

But in Python, 
the latest defined will get updated, 
hence the function area(r) will become useless.
'''
# POLYMORPHISM - METHOD OVERRIDING

class A:
    def say(self):
        print("POLYMORPHISM overriding In A")
class B(A):
    def say(self):
        print("POLYMORPHISM overriding In B")
        
obj = B()
obj.say()


# INHERITANCE
'''
1) Single
    2) Multilevel
        3)Multiple
    '''
print("\nINHERITANCE")

#1) SINGLE INHERITANCE

class A:
    a = 10
    b = 20
    def add(self):
        print("--> SINGLE")
        sum = self.a + self.b
        print("sum: ", sum)
        
class B(A):
    c = 30
    d = 40
    def sub(self):
        sub = self.c - self.d
        print("sub: ",sub)
        
inherit = B()
inherit.add()
inherit.sub()

#2) MULTILEVEL INHERITANCE
class A:
    a = 10
    b = 20
    def add(self):
        print("--> MULTILEVEL")
        sum = self.a + self.b
        print("sum: ", sum)

class B(A):
    def sub(self):
        sub = self.b - self.a
        print("sub: ",sub)
        
class C(B):
    def mul(self):
        mul = self.a * self.b
        print("mul: ", mul)
    
    
mulinherit = C()
mulinherit.add()
mulinherit.sub()

#2) MULTIPLE INHERITANCE
class A:
    a = 10
    b = 20
    def add(self):
        print("--> MULTIPLE")
        sum = self.a + self.b
        print("sum: ", sum)

class B:
    c = 30
    d = 40
    def sub(self):
        sub = self.c - self.d
        print("sub: ",sub)
        
class C(B, A):
    def mul(self):
        mul = self.a * self.c
        print("mul: ", mul)
    
    
mulinherit = C()
mulinherit.add()
mulinherit.sub()
mulinherit.mul()

#DATA HIDING
class datahiding:
    __num = "secretword"
    def reveal(self):
        print("The operation needs this ", self.__num)

obj = datahiding()
obj.reveal()
print(obj.__num)

'''
 The above statement gives an error
 because we are trying to access private
 variable outside the class
'''