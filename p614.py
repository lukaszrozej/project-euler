# https://projecteuler.net/problem=614

from functools import lru_cache
from math import sqrt, ceil

max_k = [ ceil( (sqrt(1+6*n) - 1) * 2 )+3 for n in range(1, 1001)  ]

def p(n, k, l=0):
	# print('    '*l, n, k)
	if n == k and (n == 0 or n == 1):
		# print('    '*l, '  ok')
		return 1
	if n < 0 or n <= k or k <= 0:
		return 0
	if k == 1:
		if n % 4 == 2:
			return 0
		else:
			# print('    '*l, '  ok')
			return 1
	if (2*k - 5)**2 > 6*n + 1:
		return 0
	return  p(n - 4*k, k, l+1) + p(n - 4*k, k-1, l+1) + \
			p(n+1-4*k, k-1, l+1) + p(n+1-4*k, k-2, l+1) + \
			p(n+3-4*k, k-1, l+1) + p(n+3-4*k, k-2, l+1) + \
			p(n+4-4*k, k-2, l+1) + p(n+4-4*k, k-3, l+1)

def pp(n):
	return sum( p(n,k) for k in range(1, max_k[n-1]+1))

# print( pp(1) )
# print( pp(2) )
# print( pp(3) )
# print( pp(6) )
# print( pp(10) )
print( len(max_k) )

print( pp(1000) )
