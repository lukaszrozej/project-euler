# https://projecteuler.net/problem=614

from functools import lru_cache
from math import sqrt, ceil

# number of ways to partition n into k distinct summands
@lru_cache(maxsize=None)
def p_d(n, k):
	# print('    '*l, n, k)
	if n == k:
		if n == 0 or n == 1:
			# print('    '*l, '    ok')
			return 1
		else:
			return 0
	if n <= 0 or n <= k or k <= 0:
		return 0
	if k == 1:
		return 1
	return 	p_d(n-k, k-1) + p_d(n-k, k) % 1000000007

# number of ways to partition n into distinct summands
def pp_d(n):
	return sum( p_d(n, k) for k in range(0, ceil(sqrt(1 + 8*n)) // 2 + 1) ) % 1000000007


# number of ways to partition n into k distinct odd summands
@lru_cache(maxsize=None)
def p_do(n, k):
	# print('    '*l, n, k)
	if n == k:
		if n == 0 or n == 1:
			# print('    '*l, '    ok')
			return 1
		else:
			return 0
	if n <= 0 or n <= k or k <= 0:
		return 0
	if k == 1:
		if n % 2 == 1:
			return 1
		else:
			return 0
	return 	p_do(n+1-2*k, k-1) + p_do(n-2*k, k) % 1000000007

# number of ways to partition n into distinct summands
def pp_do(n):
	return sum( p_do(n, k)	for k in range(0, ceil(sqrt(1 + 8*n)) // 2 + 1) ) % 1000000007


def ppp(n):
	return sum( pp_d(i) * pp_do(n - 4*i) % 1000000007 for i in range(0, n//4 + 1)) % 1000000007


print( sum( ppp(i) for i in range(1,10000001) ) % 1000000007 )
