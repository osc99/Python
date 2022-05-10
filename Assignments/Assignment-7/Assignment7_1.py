def rec(n):
	if(n>0):
		print("*",end=" ")
		n=n-1
		rec(n)


def main():
	n = int(input("Enter Number : "))
	rec(n)
if __name__ == '__main__':
	main()