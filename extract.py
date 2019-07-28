# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 12:55:41 2019
EXTRACTING CONDITION BASED NON CONTIGUOUS SUBSETS
#extract()
@author: SIDDHARTH
"""
# =============================================================================
# numpy.extract(<FramingConditions>,<arrays>)
# eg : condition = np.mod(array,5)==0
# =============================================================================

import numpy as np
ary=np.arange(0,24).reshape(4,6)
print("\n\n")
print(ary)
print("\n\n")
condition1=np.mod(ary,5)==0
print(ary)

print("\n in the array if num%5==0 then array becomes \n\n",condition1)
print("\n\n")
condition2=np.mod(ary,2)==0
print(ary)
print("\n in the array if num%2==0 then array becomes \n\n",condition2)
