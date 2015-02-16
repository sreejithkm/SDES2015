def gcd(a,b):
	if (a<0 or b<0):
		raise ValueError ("inputs should be positive")
	if (type(a)!=int and type(a)!=long):
		raise TypeError ("inputs should be int or long")

	if (type(b)!=int and type(b)!=long):
		raise TypeError ("inputs should be int or long")
	while b!=0:
		a,b=b,a%b
	return a
	

