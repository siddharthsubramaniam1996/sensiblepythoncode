# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 19:47:18 2019

@author: SIDDHARTH
"""

import numpy as np
L=np.array([3,4,5])
N=np.array([3,4,5],np.int32)
print(L)
print(N)
print(L*N)
print(N*3)
print(L+L)
print(N+N)

O=np.array([2,4,6,8])
print(O)

P=np.array([[2],[4],[6]])
print(P)

Q=np.array([[1,2,3,4],[5,1,7,8]])
print(Q)

R=np.zeros([1,6],dtype=int,order='C')
print("\nMatrix R: \n", R)

R[0][3]=15
R[0][5]=25
print("Result",R)


S=np.arange(13,25).reshape(3,4)
print (S)

A=np.arange(10,100,10)
print("\n\tA IS: \n")
print(A)

B=np.arange(0,16).reshape(4,4)
print("\n\tB IS: \n")
print(B)

print("\n\tCut1 0:2,1:3 \n")
C1=B[0:2,1:3]
print(C1)

print("\n\tCut2 2:6:3 \n")
C2=A[2:6:3] #start stop jump
print(C2)

print("\n\tCut3 -1:-3 \n")
C3=A[-1:-3]
print(C3)

print("\n\tCut4 :-1 \n")
C4=B[:-1]
print(C4)

print("\n\tCut5 :-1 \n")
C5=B[:3, 2:]
print(C5)

print("\n\tCut6 :-1 \n")
C6=B[-3,6:2:-1]
print(C6)

print("\n\tConcat 1 \n")
c7=np.array([1,2,3])
c8=np.array([3,2,1])
z=np.concatenate([c7,c8])
print(z)

print("\n\tConcat 2 (axis =0) \n")
grid=np.array([[1,2,3],[4,5,6]])
G2=np.concatenate([grid,grid], axis=None)
print(G2)

print("\n\tConcat 3 (axis =1) \n")
grid=np.array([[1,2,3],[4,5,6]])
G3=np.concatenate([grid,grid], axis=1)
print(G3)

print("\n\tvstack \n")
x=np.array([1,2,3])
g=np.array([[9,8,7],[6,5,4]])
R=np.vstack([x,g])
print(R)

print("\n\t hstack \n")
g1=np.array([[9,8,7],[6,5,4]])
y=np.array([[99],[99]])
R1=np.hstack([g,y])
print(R1)

print("\n\t split \n")
x=[1,2,3,99,99,3,2,1]
x1, x2, x3=np.split(x, [3,5])
print("\nx1:",x1, "\nx2:",x2,"\nx3:",x3)
