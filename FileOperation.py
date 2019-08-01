# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 17:57:03 2019

@author: SIDDHARTH
"""


# =============================================================================
# NEEDS REVIEW
# cnt=0;
# with open("test.txt","a+") as f:
#   while True:
#     c = f.read(1)
#     if not c:
#       print ("End of file")
#       break
#     else :
#       cnt=cnt+1
#       if(cnt==3):
#           f.write("x")
#           
# print(c)
#     
# 
# =============================================================================

# Read in the file
a=[]
b=[]
c=[]
with open('test.txt', 'r+') as file :
    for i in file:
        for ch in i:
            #print(ch)
            a.append(ch)
            #cnt=cnt-1
print("THE ORIGINAL\n")
print(a)
print("\n")

for i in a:
    #print(i)
    if i=='\n': # or i=="\n\n" or i=="\n\n\n":
        a.remove(i)
        b=a
print("THE EDITED LIST: \n", a)

for i in b:
    #print(i)
    if i=="\n":
        b.remove(i)
        c=b
print("\nTHE SECOND EDITED LIST\n", b)

for i in c:
    #print(i)
    if i=="\n" or i=='\t':
        c.remove(i)
        
       
print("\nTHE FINALLY EDITED LIST\n", b)
  
d=len(c)
print("LENGTH OF LIST IS:", d)
print(c(d))
if c[d]=='\n' or c[d]=='\t':
    remove(c, d))

print(c)      
