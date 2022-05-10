def prime(n):

	f = False
	if n > 1:
	    for i in range(2, n):
	        if (n % i) == 0:
	            f = True
	            break
	if f:
	    print(n, "is not a prime number")
	else:
	    print(n, "is a prime number")


def main():
	n=int(input("Enter the no"))
	prime(n)


if __name__=="__main__":
	main()