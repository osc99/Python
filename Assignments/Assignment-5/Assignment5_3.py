class arithmatic:
	def __init__(self):
		self.v1 = 0
		self.v2 = 0
		self.ans = 0

	def accept(self):
		self.v1 = int(input("Enter First no : "))
		self.v2 = int(input("Enter Second no : "))

	def addition(self):
		self.ans = self.v1 + self.v2
		print("Addition is : ",self.ans) 

	def subtraction(self):
		self.ans = self.v1 - self.v2
		print("Subtraction is : ",self.ans)

	def mult(self):
		self.ans = self.v1 * self.v2
		print("Multiplication is : ",self.ans) 

	def div(self):
		self.ans = self.v1 / self.v2
		print("Division is : ",self.ans)

def main():
	obj1 = arithmatic()
	obj2 = arithmatic()

	obj1.accept()
	obj1.addition()
	obj1.subtraction()
	obj1.mult()
	obj1.div()

	obj2.accept()
	obj2.addition()
	obj2.subtraction()
	obj2.mult()
	obj2.div()

if __name__=="__main__":
	main()