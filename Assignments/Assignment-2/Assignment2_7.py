def main():
	n=int(input("Enter the no : "))
	for i in range(1,n+1):
		for j in range(1,n+1):
			print(j,end=" ")
		print()

if __name__=="__main__":
	main()