# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 11:10:16 2019
vertical and horizontal vsplit and hsplit
@author: SIDDHARTH
"""
#hsplit is horizontal split
#vsplit is vertical split

#numpy.hsplit(arrayname,numberofsubsets)
#numpy.vsplit(arrayname,numberofsubsets)
#split numpy array , axis = 0 horizontally and axis=1 is vertically
#syntax:- numpy.split(arrayname,numberofsubarrays | 1Darray,[axis=value])
import numpy as np
try:
    
    ar1d=[10,11,12,13,14,15,16,17,18,19]
    ar1dsplit=np.split(ar1d,[2,6,-2,-2]) #the splits are [0:2],[2:5]and[6:9]
    ary=np.arange(0,24).reshape(4,6)
    print(ary)
    
    a=np.hsplit(ary,3)
    b=np.vsplit(ary,2)
    
        
    print("\n\n", a)
    print("\n\n", b)
    print("\n\nsplitting a 1d array: \n", ar1dsplit)
    
except:
    print("HEY NAAG PRABHU ERROR AALA")