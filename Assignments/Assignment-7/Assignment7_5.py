def rec(n):
	if(n==1):
		return n
	else:
		return n*rec(n-1)

def main():
	n = int(input("Enter Number : "))
	ret = rec(n)
	print(ret)
if __name__ == '__main__':
	main()