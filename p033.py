# https://projecteuler.net/problem=33

from fractions import Fraction

def wrongly_cancelled(a, b):
	a = str(a)
	b = str(b)
	for d in '123456789':
		if d in a and d in b:
			return Fraction( a.replace(d, '', 1) + '/' +  b.replace(d, '', 1) )

product = Fraction(1,1)
for a in range(11, 100):
	for b in range(a+2, 100):
		f = Fraction(a, b)
		if a % 10 and b % 10 and f == wrongly_cancelled(a, b):
			product *= f

print(product)

