class demo:

	def __init__(self,n1,n2):
		self.a=n1
		self.b=n2

	def fun(self):
		print(self.a,"\n",self.b)

	def gun(self):
		print(self.a,"\n",self.b)

def main():
	Obj1 = demo(11,21)
	Obj2 = demo(51,101)

	Obj1.fun()
	Obj2.fun()
	Obj1.gun()
	Obj2.gun()

if __name__ == '__main__':
	main()