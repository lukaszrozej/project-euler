# https://projecteuler.net/problem=45

'''
Hn = n(2n-1) = 2n(2n-1) / 2 = T(2n-1)
So every hexagonal number is triangle
'''

from itertools import count
from math import sqrt
# from gmpy2 import isqrt, mpz

def is_pentagonal(p):
	n =  1 + int(sqrt(1 + 24*p)) // 6
	if p == (3*n*n - n) // 2:
		return True
	return False

for n in count(144):
	h = n * (2*n - 1)
	if is_pentagonal(h):
		break

print(h)