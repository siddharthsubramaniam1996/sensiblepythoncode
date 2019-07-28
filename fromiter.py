# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 19:26:41 2019

@author: SIDDHARTH
"""
import numpy as np

a1 = np.array([1,2,3,4,5])

l1=['asddf','bdfxsg','crfghj']
print(l1)
print("a2 is")
a2 =np.array(l1)
print (a2)
print(type(a2[0]))

tup1=(2.5,3.5,4.7,8.5)
a3=np.array(tup1)
print (a3)

d1={1:'A',2:'B',3:'C',4:'D',5:'E',}
print('keys are')
x=d1.keys()
print(x)
print(d1)
print("value of a4")
a4=np.array(x)  
print(a4)

#fromiter syntax : numpy.fromiter(iterable, dtype, count=-1)
print('fromiter run')
a4=np.fromiter(d1,dtype=int, count=4)
print(a4)

astr="#ThisIsWrittenBySid"
a5=np.fromiter(astr,dtype="U2",count=19)
print(a5)


list1=['a','b','c','d','e']
print(list1)

tup1=(1,2,3,4,5)
print(tup1)
a6=np.fromiter(tup1,dtype="U3",count=4)
print ('value of a6 relating to tup1 is' ,a6)

a7=['1','2','3','4','5']
print('value of a7 is' ,a7)

