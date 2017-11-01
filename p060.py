# https://projecteuler.net/problem=60

from pyprimesieve import primes
from sympy import isprime
import numpy as np
from functools import lru_cache

@lru_cache(maxsize=2**16)
def forms_primes(a, b):
	return isprime(int(a + b)) and isprime(int(b + a))

# Find the lowest sum for a set of n primes below limit for which any two primes concatenate to produce another prime below.
def find(n, limit):
	prime_numbers = np.array(primes(limit))
	min_sum = prime_numbers[-n:].sum()
	found = np.repeat(str(prime_numbers[-1]), n)
	min_found = found.copy()

	# find assuming m primes have already been found,
	# start looking from k'th prime
	def fn(m, k, cur_sum):
		nonlocal min_sum, min_found
		for i in range(k, prime_numbers.size):
			p = prime_numbers[i]
			if (n-m) * p + cur_sum > min_sum:
				return
			s = str(p)
			if all( forms_primes(s, found[i]) for i in range(0, m) ):
				found[m] = s
				if m+1 == n:
					if min_sum > cur_sum + p:
						min_found = found.copy()
						min_sum = cur_sum + p
				else:
					fn(m+1, i+1, cur_sum+p)

	fn(0, 1, 0)

	return min_found, min_sum

print( find(5, 20000) )

