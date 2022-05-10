class BankAccount:
	roi = 10.5
	def __init__(self,name,amount):
		self.n = name
		self.amt = amount

	def deposite(self):
		a = int(input("Enter the amount you want to deposite : "))
		self.amt=self.amt+a

	def withdraw(self):
		a = int(input("Enter the amount you want to withdraw : "))
		self.amt=self.amt-a

	def calcInterest(self):
		self.amt = self.amt+(self.amt*self.roi/100)

	def display(self):
		print("Name : ",self.n)
		print("Amount : ",self.amt)

def main():

	name = input("Enter the Name of Acc Holder : ")
	amount = int(input("Enter Account Balance : "))
	obj1 = BankAccount(name,amount)
	obj1.display()
	obj1.deposite()
	obj1.display()
	obj1.withdraw()
	obj1.display()
	obj1.calcInterest()
	obj1.display()

	name = input("Enter the Name of Acc Holder : ")
	amount = int(input("Enter Account Balance : "))	
	obj2 = BankAccount(name,amount)
	obj2.display()
	obj2.deposite()
	obj2.display()
	obj2.withdraw()
	obj2.display()
	obj2.calcInterest()
	obj2.display()
	
if __name__ == '__main__':
	main()