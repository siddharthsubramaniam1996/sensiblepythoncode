# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 12:55:41 2019
COMPRESS
#compress()
@author: SIDDHARTH
"""
# =============================================================================
# numpy.compress(<FramingConditions>,<arrayname>,[axis=None])
# eg : compress = np.mod(array,5)==0
# =============================================================================

import numpy as np
ary=np.arange(0,24).reshape(4,6)

print("\n\n")
print(ary)
print("\n\n")

# =============================================================================
rw=len(ary)
cl=len(ary.T)
# =============================================================================

print("\n\n")
condition1=np.mod(np.arange(rw),2)==0
print("THE ORIGINAL ARRAY IS \n",ary)
print("\n in the array if num%2==0 then array becomes \n\n",condition1)

print("\n\n")
condition2=np.mod(np.arange(cl),2)==0
print("THE ORIGINAL ARRAY IS \n",ary)
print("\n in the array if num%2==0 then array becomes \n\n",condition2)

a=np.compress(condition1,ary,axis=0)
b=np.compress(condition2,ary,axis=0)

print(a)

print(b)

