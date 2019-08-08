class worker:
	wname=input("Enter worker name :")
	hours_worked=int(input("Enter hours worked: "))
	pay_rate=int(input("enter pay rate: "))
	salary=hours_worked*pay_rate
	def display(self):
		print("The worker named", self.wname, "gets paid salary of:", self.salary)
		


work=worker()
work.display()



