mulX = lambda a,b: a*b

def main():
	n1,n2=input().split()
	n1=int(n1)
	n2=int(n2)
	ret = mulX(n1,n2)
	print("Result : ",ret)

if __name__ == '__main__':
	main()