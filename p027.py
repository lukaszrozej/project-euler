# https://projecteuler.net/problem=27

# f(n) = n^2 + a*n + b
# b has to prime to get prime for n = 0
# b + a + 1 has to prime to get prime for n = 1
# so primes f(0) and f(1) determine the function

# 1.

from pyprimesieve import primes
from sympy.ntheory import isprime
from itertools import takewhile

primes_list = primes(1000000)

bound = 1000

max_len = 0
for f0 in takewhile(lambda x: x < bound, primes_list):
	for f1 in takewhile(lambda x: x < f0 + bound + 1, primes_list):
		a = f1 - f0 - 1
		b = f0
		n = 2
		while n*n + a*n + b in primes_list:
			n += 1
		if max_len < n:
			max_len = n
			max_a = a
			max_b = b


print('a = {}, b = {}, length = {}, a*b = {}'.format(max_a, max_b, max_len, max_a*max_b))


