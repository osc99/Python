from functools import reduce

def main():
	a=[]
	n=int(input())

	a = list(int(i) for i in input().strip().split())[:n]
	print("Input List : ",a)

	a_filter = list(filter(lambda c:(for i in range(2, int(c**.5)+1),a))
	print("Filtered List : ",a_filter)

	a_map = list(map(lambda c:c*2,a_filter))
	print("List after map : ",a_map)
	
	a_reduce = reduce(lambda n1,n2:max(n1,n2),a_map)
	print("Output of reduce : ",a_reduce)
	
if __name__ == '__main__':
	main()


# 2 70 11 10 17 23 31 77