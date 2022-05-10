def main():
	a=[]
	n=int(input())
	a = list(int(i) for i in input().strip().split())[:n]
	ret = max(a)
	print("Result : ",ret)

if __name__ == '__main__':
	main()