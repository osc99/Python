def add(a):
	s=0
	for i in range(len(a)):
		s=s+a[i]
	return s

def main():
	a=[]
	n=int(input())
	a = list(int(i) for i in input().strip().split())[:n]
	ret = add(a)
	print("Result : ",ret)

if __name__ == '__main__':
	main()