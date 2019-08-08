class book:
	book_id=input("Enter book ID :")
	book_name=input("Enter book name : "))
	book_cost=int(input("enter book cost : "))
	book_copies_sold=int(input("Enter no of copies sold :"))
	book_earnings=book_cost*book_copies
	def display(self):
		print("The book named", self.book_name, "has earned a revenue of", self.book_earnings)
		


books=book()
books.display()



