def add(n1,n2):
	a = n1+n2
	return a

def main():
	a = int(input("Enter first number"))
	b = int(input("Enter second number"))
	c = add(a,b)
	print("Addition : ",c)

if __name__=="__main__":
	main()