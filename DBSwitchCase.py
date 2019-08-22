#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:06:22 2019

@author: SIDDHARTH
"""
# Displaing options
print("Option 1: Show databases \n")
print("Option 2 : Create a new database \n")
print("Option 3 : Create a table in a selected database \n")
print("Option 4: Insert values into a database")

# Choose an option
opt=int(input("\n enter option here : "))
usr=input("\n enter database user : ")
password=input("\n enter user's database password : ")
hname=input("\n Enter the host here : ")

# Connect the database
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user=usr,
        passwd=password
)


# Implement Python Switch Case Statement using Class

class PythonSwitch:

    def switch(self, option):
        default = "Incorrect Option"
        return getattr(self, 'case_' + str(option), lambda: default)()

    def case_1(self):
        print("\n You have chosen to show the databases accesible to the user \n")
        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        for x in mycursor:
            print(x)
 
    def case_2(self):
       print("\n You have chosen to create a new database accesible to the user \n")
       mycursor = mydb.cursor()
       db=input("enter name of database to be created : ")
       dbcreate="CREATE DATABASE "+db
       mycursor.execute(dbcreate)
                 
    def case_3(self):
        print("\n You have chosen to create a new table in a specific database accesible to the user \n")
        mycursor = mydb.cursor()
        
        db=input("enter name of database to be selected : ")
        dbselect="USE "+db
        mycursor.execute(dbselect)
               
        print("Enter  field values only")
        
        tablename=input("enter the name of the table to be created: ")
        
        field1=input("enter field 1: ")
        dtype1=input("enter field1's datatype :")
        
        field2=input("enter field 2: ")
        dtype2=input("enter field2's datatype :")
        
        field3=input("enter field 3: ")
        dtype3=input("enter field3's datatype :")
        
        y="create table "+tablename+" ("+field1+" "+dtype1+","+field2+" "+dtype2+","+field3+" "+dtype3+")" 
        print("the query designed is: \n",y)
        
        mycursor.execute(y)


    def case_4(self):
        print("\n You have chosen to insert values into a specific table in a specific database accesible to the user \n")
        mycursor = mydb.cursor()
        
        db=input("enter name of database to be selected : ")
        dbselect="USE "+db
        mycursor.execute(dbselect)
               
        print("Enter values only")
        
        tablename=input("enter the name of the table to be created: ")
        
        field1=input("enter field 1: ")
                
        field2=input("enter field 2: ")
                
        field3=input("enter field 3: ")
        
        
        y="insert into "+tablename+" values ('"+field1+"', '"+field2+"', '"+field3+"')" 
        # insert into siddharthtesting values("sid","arun","subramaniam")
        print("the query designed is: \n",y)
        
        mycursor.execute(y)

 
# Function calling for the switch case
s = PythonSwitch()
print(s.switch(opt))
