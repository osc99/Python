def factor(n):
  fact = [1]
  s=0
  for i in range(2,n+1):
     if n%i==0:
         fact.append(i)
  for i in range(len(fact)):
  	s=s+fact[i]       							
  return s

def main():
	n=int(input("Enter the no"))
	f = factor(n)
	print("Sum of factors is : ",f)


if __name__=="__main__":
	main()