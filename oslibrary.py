# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:03:36 2019

@author: SIDDHARTH
"""

# =============================================================================
#
# import os
# os.start(/full/file/path).st_size==0
#
# OR
#
# import os
# os.getSize('/full/file/path') > 0
#
# =============================================================================

# FPATH MEANS FULL PATH. YOU HAVE TO PUT THE FULL FILEPATH IN PLACE OF FPATH


# =============================================================================
import os
ipath=input("enter complete filepath of the document here: ")
fpath=ipath.replace(os.sep, '/')
print("/n")
print(fpath)
print("/n")
def isEmpty(fpath):
    return os.path.isfile(fpath) and os.path.getSize(fpath) > 0
print (isEmpty(fpath))
# =============================================================================

# =============================================================================
# LINE BY LINE READING
# =============================================================================
# with open("filetest1.txt","r+") as fp:
#     for i in fp:
#         print(i)
# 
# =============================================================================
# OR
# =============================================================================
# NEEDS REVIEW AS IT IS KILLING THE TERMINAL ON RUN 
#        
# with open("filetest1.txt","r+") as fp:
#     while True:
#         cur_line=fp.readline()
#         if cur_line==' ':
#             break;
#         print(cur_line)
# =============================================================================


