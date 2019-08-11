#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 19:13:22 2019

@author: SIDDHARTH
"""

class person:
    def __init__(self,name,id):
        self.id=id
        self.name=name
   
class Employee:
    def __init__(self,salary,designation):
        self.salary=salary
        self.designation=designation
class Leader:
    def __init__(self,name,id,salary,designation,points):
        self.points=points
        person.__init__(self,name,id)
        Employee.__init__(self,salary,designation)
        print(self.designation)
a=Leader("Ritesh",1,25000,"Developer","80")

