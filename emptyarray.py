# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 10:02:08 2019

@author: SIDDHARTH
"""

import numpy as np 
  
b = np.empty(2, dtype = int) 
print("Matrix b : \n", b) 
  
a = np.empty([2, 2], dtype = int) 
print("\nMatrix a : \n", a) 
  
c = np.empty([3, 5]) 
print("\nMatrix c : \n", c) 

print("New stuff")
d=np.empty([2,3],dtype=int,order='C')
print(d)


#ARRAY WITH ZEROS and float
e=np.zeros([5,4],dtype=float,order='C')
print("\nMatrix e: \n", e)

#ARRAY WITH ONES and int
f=np.ones([5,4],dtype=int,order='C')
print("\nMatrix f: \n", f)

# =============================================================================
# empty_like(array_name)
# zero_like(array_name)
# ones_like(array_name)
# =============================================================================

g=np.ones_like(d)
print("\n Matrix g which has 2 cols and 3 rows from d: \n", g)