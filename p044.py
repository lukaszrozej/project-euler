# https://projecteuler.net/problem=44

# 1. Ugly and slow :)
# p(n) - p(n-1) = 3n - 2
# p(k+1) - p(k) <= p(j)  =>  j >= (1 + sqrt(72*k + 25)) / 6

from math import sqrt, inf
from gmpy2 import isqrt, mpz

def is_pentagonal(p):
	n =  1 + int(sqrt(1 + 24*p)) // 6
	if p == (3*n*n - n) // 2:
		return True
	return False

# minimal = 1000000000
# k = 2
# while 3*k-2 < minimal:
# 	pk = (3*k*k - k) // 2
# 	minimal_j = 1
# 	if minimal < pk:
# 		minimal_j = int( (isqrt(mpz(1 + 24*(pk-minimal))) - 1) / 6 )
					
# 	for j in range(minimal_j,k):
# 		pj = (3*j*j - j) // 2
# 		if is_pentagonal(pk + pj) and is_pentagonal(pk - pj):
# 			minimal = pk - pj
# 			print(pk, pj, minimal)
# 	if k % 100000 == 0:
# 		print(k)
# 	k += 1
# 
# print(minimal)

# 2. Faster:
# 	pk + pj = ps
# 	pk - pj = pd
# so:
# 	2pk = ps + pd
# 	2pj = ps - pd
# Iterate over pd and ps, check if pk and pj are ok

from itertools import count

def is_double_pentagonal(p):
	return p % 2 == 0 and is_pentagonal(p // 2)

found = False
for s in count(1):
	for d in range(1,s):
		pd = (3*d*d - d) // 2
		ps = (3*s*s - s) // 2
		if is_double_pentagonal(ps + pd) and is_double_pentagonal(ps - pd):
			found = True
			break
	if found:
		break

print(pd)



