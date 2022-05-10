import arithmetic

def main():
	n1 = int(input("Enter the no 1 : "))
	n2 = int(input("Enter the no 2: "))
	a = arithmetic.add(n1,n2)
	b = arithmetic.sub(n1,n2)
	c = arithmetic.mul(n1,n2)
	d = arithmetic.div(n1,n2)
	print("Add : ",a)
	print("Sub : ",b)
	print("Mul : ",c)
	print("Div : ",d)

if __name__=="__main__":
	main()