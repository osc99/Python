def main():
	n=int(input("Enter the no : "))     	
	num = 1
    for i in range(0, n):
        num = 1
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print()

if __name__=="__main__":
	main()