from functools import reduce

def main():
	a=[]
	n=int(input())

	a = list(int(i) for i in input().strip().split())[:n]
	print("Input List : ",a)

	a_filter = list(filter(lambda c:c%2==0,a))
	print("Filtered List : ",a_filter)

	a_map = list(map(lambda c:c*c,a_filter))
	print("List after map : ",a_map)
	
	a_reduce = reduce(lambda n1,n2:n1+n2,a_map)
	print("Output of reduce : ",a_reduce)
	
if __name__ == '__main__':
	main()


# 5 2 3 4 3 4 1 2 8 10