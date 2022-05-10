class circle:
	def __init__(self):
		self.r=0.0
		self.a=0.0
		self.c=0.0

	def accept(self):
		self.r = float(input("Enter Radius of circle : "))

	def CalculateArea(self,pi=3.14):
		self.a = pi*(self.r**2)

	def CalculateCircumference(self,pi=3.14):
		self.c = 2*pi*self.r

	def display(self):
		print("Radius of circle is : ",self.r)
		print("Area of circle is : ",self.a)
		print("Circumference of circle is : ",self.c)

def main():
	obj1=circle()

	obj1.accept()
	obj1.CalculateArea()
	obj1.CalculateCircumference()
	obj1.display()

if __name__ == "__main__":
	main()