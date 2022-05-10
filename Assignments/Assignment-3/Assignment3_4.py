def freq(a,b):
	z=0;
	for i in range(len(a)):
		if(a[i]==b):
			z=z+1
	return z


def main():
	a=[]
	n=int(input("Number of elements : "))
	a = list(int(i) for i in input().strip().split())[:n]
	b = int(input("Element to search : "))
	ret = freq(a,b)
	print("Result : ",ret)


if __name__ == '__main__':
	main()