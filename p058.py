# https://projecteuler.net/problem=58

from sympy import isprime
from itertools import count

primes_count = 0
diagonal_count = 1
for n in count(3, 2):
	primes_count += sum( isprime(k) for k in (n*n - n + 1, n*n - 2*n + 2, n*n - 3*n + 3) )
	diagonal_count += 4
	if primes_count * 10 < diagonal_count:
		break

print(n)