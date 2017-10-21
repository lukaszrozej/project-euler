# https://projecteuler.net/problem=37

from sympy import isprime

def is_left_truncatable_prime(s):
# assumes s is already prime
	return all( isprime(int(s[k:])) for k in range(1,len(s)) ) and len(s) > 1

def truncatable_primes():
	def find(s):
	# recursively find truncatable primes starting with digits in s
		if isprime(s):
			if is_left_truncatable_prime(s):
				yield int(s)
			for d in '1379':
				yield from find(s + d)

	for d in '2357':
		yield from find(d)

print( sum(truncatable_primes()) )