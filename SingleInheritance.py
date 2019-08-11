#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:51:30 2019

@author: om
"""
x=0
class class1 :
    def __init__(self):
        global x
        x+=1
        print("I am class1")
class class2(class1):
    def __init__(self):
        super().__init__()
        global x
        x+=2
        print("I am class2")
d=class2()
print(x)