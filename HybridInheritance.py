#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 19:30:36 2019

@author: SIDDHARTH
"""
x=0   
len=0
br=0
pr=0

class accept_values:
    def accept_values_from_user(self):
        global len
        global br
        global pr
        len=int(input("Enter length: "))
        br=int(input("Enter breadth: "))
        pr=int(input("Enter selling price per unit: "))

class accept:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def printf(self):
        print(self.length,self.breadth)
    
class perimeter(accept):
    def __init__(self,length,breadth,perimeter):
        super().__init__(length,breadth)
        self.perimeter=2*(self.length+self.breadth)
       
    def printf(self):
        print("Perimeter :",self.perimeter)

class area(accept):
    def __init__(self,length,breadth,area):
        super().__init__(length, breadth)
        self.area=(self.length * self.breadth)
        
    def printa(self):
        print("Area : ",self.area)

class cost_calc(area):
    def __init__(self,length,breadth,area,pr):
        super().__init__(length,breadth,area)
        self.cost=self.area*pr
    def printc(self):
        print("Cost is :",self.cost)

y=accept_values()
y.accept_values_from_user()    


p=perimeter(len,br,x)
p.printf()

# =============================================================================
# a=area(len,br,x)
# a.printa()
# =============================================================================

z=cost_calc(len,br,area,pr)
z.printa()
z.printc()