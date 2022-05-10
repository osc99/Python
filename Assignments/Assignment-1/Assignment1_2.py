def ChkNum(n):
	if(n%2==0):
		print("Even Number")
	else:
		print("Odd Number")

def main():
	n = int(input("Please Enter the number : "))
	ChkNum(n)

if __name__=="__main__":
	main()
	