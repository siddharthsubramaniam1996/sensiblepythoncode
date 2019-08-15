#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:00:04 2019

@author: om
"""
x=None
y=None
z=None
#field1,dtype1,field2,dtype2,field3,dtype3=None
my_first_db=input("enter database to be created : ")
import mysql.connector
db_connection = mysql.connector.connect(
        host= "localhost",
        user= "pythonuser",
        passwd= "Abcd1234!"
        )
# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()
# executing cursor with execute method and pass SQL query


class banavtudb:
    def dbcreation(self,x,z):
        x="create database "+my_first_db
        print(x)
        z="use "+my_first_db
        print(z)
        
        db_cursor.execute(x)
        db_cursor.execute(z)
        
        
    def tbcreation(self,y):
        print("Enter  field values only")
        
        tablename=input("enter the name of the table to be created: ")
        
        field1=input("enter field 1: ")
        dtype1=input("enter field1's datatype :")
        
        field2=input("enter field 2: ")
        dtype2=input("enter field2's datatype :")
        
        field3=input("enter field 3: ")
        dtype3=input("enter field3's datatype :")
        
        y="create table "+tablename+" ("+field1+" "+dtype1+","+field2+" "+dtype2+","+field3+" "+dtype3+")" 
        print("the query designed is: ",y)
        
        db_cursor.execute(y)


f=banavtudb()
f.dbcreation(x,z)
f.tbcreation(y)