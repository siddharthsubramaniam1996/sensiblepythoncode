# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 11:25:06 2019
concatination
@author: SIDDHARTH
"""
import numpy as np
l1=np.array([1,2,3])
l2=np.array([4,5,6])
l3=np.array([[9,8,7],[6,5,4],[1,2,3]])
l4=np.array([[2,4,2],[1,9,1]])
l5=np.array([[2,4],[9,1],[2,1]])
l6=np.array([[2],[9],[1]])
l7=np.array([[2,4,2,3],[2,1,9,1]])

jar1=np.concatenate((l3,l4),axis=0)
jar2=np.concatenate((l3,l5),axis=1)
jar3=np.concatenate((l3,l6),axis=1)
jar4=np.concatenate((l4,l3),axis=0)
jar5=np.concatenate((l4,l7),axis=1)

# .T is transpose
jar6=np.concatenate((l3,l4.T),axis=1)

jar7=np.concatenate((l3,l4),axis=0)

jar8=np.concatenate((l3,l4),axis=None)


print("\n\n",jar1)
print("\n\n",jar2)
print("\n\n",jar3)
print("\n\n",jar4)
print("\n\n",jar5)
print("\n\n jar6 is: \n",jar6)
print("\n\n transpose reversed of jar 6 \n",jar7)
print("\n\n",jar8)