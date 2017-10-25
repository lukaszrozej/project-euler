# https://projecteuler.net/problem=46

from itertools import count, filterfalse
from sympy import isprime
from math import sqrt
from pyprimesieve import primes

ps = primes(1000000)

def is_square(x):
	s = int(sqrt(x))
	return x == s*s

def find():
	for n in filterfalse(isprime, count(9, 2)):
		if any( is_square((n - p)//2) for p in ps if p < n ):
			continue
		return n

print(find())
