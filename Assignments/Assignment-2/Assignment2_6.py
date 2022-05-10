def main():
	n=int(input("Enter the no : "))
	for i in range(n + 1, 0, -1):    
    	for j in range(0, i,- 1):  
    	    print("*", end=' ')  
   		 print(" ") 


if __name__=="__main__":
	main()