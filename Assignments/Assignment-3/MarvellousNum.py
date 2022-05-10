def ChkPrime(num):
	flag = False
	if num > 1:
		for i in range(2, num):
			if (num % i) == 0:
				flag = True
				break
	if flag:
		return False
	else:
		return True


def ListPrime(d):
	e=[]
	s=0
	for i in range(len(d)):
		f=d[i]
		if(ChkPrime(f)):
			e.append(f)
	for i in range(len(e)):
		s=s+e[i]

	return s