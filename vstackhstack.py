# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 11:10:16 2019
vertical and horizontal vstack and hstack
@author: SIDDHARTH
"""
import numpy as np
l1=[1,2,3]
l2=[4,5,6]
l3=[[9,8,7],[6,5,4]]
l4=[[4],[5]]
sar1=np.vstack((l1,l2))
sar2=np.vstack((l1,l3))
sar3=np.hstack((l3,l4))

print("\n\n",sar1)
print("\n\n",sar2)
print("\n\n",sar3)
