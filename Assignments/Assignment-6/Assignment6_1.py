class BookStore:
	n=0
	def __init__(self,name,author):
		self.a=name
		self.b=author
		BookStore.n+=1

	def display(self):
		print(self.a,"by",self.b,". No of books : ",self.n)

def main():
	obj1=BookStore("Linux System Programming", "Robert Love")
	obj1.display()

	obj2=BookStore("C Programming", "Dennis Ritchie")
	obj2.display()

if __name__ == '__main__':
	main()