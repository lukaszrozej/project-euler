# https://projecteuler.net/problem=38

digits = set('123456789')

def pandigital_products():
	for n in range(1, 10000):
		s = ''
		k = 0
		while len(s) < 9:
			k += 1
			s += str(n*k)
		if len(s) == 9 and set(s) == digits and k > 1:
			yield int(s)


print( max(pandigital_products()) )
