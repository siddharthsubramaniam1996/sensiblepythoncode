# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: SIDDHARTH
"""

class book:
    
    def __init__(self,book_id,book_name,book_cost,book_copies_sold):
            self.book_id=book_id #input("Enter book ID :")
            self.book_name=book_name #input("Enter book name : ")
            self.book_cost=book_cost #int(input("enter book cost : "))
            self.book_copies_sold=book_copies_sold #int(input("Enter no of copies sold :"))
            self.book_earnings=self.book_cost*self.book_copies_sold
    def display(self):
        print("The book named", self.book_name, "has earned a revenue of", self.book_earnings)

books=book(1,"Subramaniam",15,5)
books.display()


