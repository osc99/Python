def fact(n):
	s=1;
	while(n!=0):
		s=s*n
		n=n-1
	return s
def main():
	n=int(input("Enter the no : "))
	a = fact(n)
	print(a)
if __name__ == '__main__':
	main()