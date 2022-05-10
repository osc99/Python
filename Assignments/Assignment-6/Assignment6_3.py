class Numbers:
	def __init__(self,num):
		self.n=num

	def chkPrime(self):
		n=self.n

		if n<=1:
			return False
		if n<=3:
			return True

		if n%2==0 or n%3==0:
			return False

		i=5
		while i*i<=n:
			if n%i==0 or n%(i+2)==0:
				return False
			i=i+6
		return True

	def chkPerfect(self):
		n=self.n
		s = 0
		for i in range(1,n):
			if n%i==0:
				s=s+i
		if s==n:
			return True
		else:
			return False

	def sumFactors(self):
		n=self.n
		s=0
		for i in range(1,n):
			if n%i==0:
				s=s+i
		return s
        
	def factor(self):
		n=self.n
		a=[]

		for i in range(1,n+1):
			if n%i==0:
				a.append(i)
		return a

def main():
	a=[]
	n = int(input("Enter Number"))
	obj1 = Numbers(n)
	print("Is Num is Prime : ",obj1.chkPrime())
	print("Is Num is Perfect : ",obj1.chkPerfect())
	a = obj1.factor()
	print("List of Factors : ",a)
	print("Sum of factors : ",obj1.sumFactors())


if __name__ == '__main__':
	main()