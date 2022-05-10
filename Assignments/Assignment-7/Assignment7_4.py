def rec(n):
	if(n==0):
		return n
	else:
		return (n % 10 + rec(int(n / 10)))

def main():
	n = int(input("Enter Number : "))
	ret = rec(n)
	print(ret)

if __name__ == '__main__':
	main()