s=1
def rec(n):
	global s
	if(s<=n):
		print(s,end=" ")
		s=s+1
		rec(n)


def main():
	n = int(input("Enter Number : "))
	rec(n)
if __name__ == '__main__':
	main()