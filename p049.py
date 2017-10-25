# https://projecteuler.net/problem=49

from pyprimesieve import primes
from itertools import combinations
from sympy import isprime

def are_permutations(a, b, c):
	a = sorted(str(a))
	b = sorted(str(b))
	c = sorted(str(c))
	return a == b and a == c

ps = primes(1000,9999)

c = 0
for a, b in combinations(ps, 2):
	c = b + b - a
	if  isprime(a) and isprime(b) and isprime(c) and are_permutations(a, b, c):
		print(a, b, c)
