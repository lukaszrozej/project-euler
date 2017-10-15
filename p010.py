# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import time
from pyprimesieve import primes_sum

# 1. Using pyprimesieve

# t = time.process_time()
# primes_sum(2000000)
# elapsed_time = time.process_time() - t
# print('time: ', elapsed_time) # 0.00145s

print( primes_sum(2000000) )

# 2. Using a generator, just to learn how to gefine one

def is_prime(n):
	if n == 1:
		return False
	if n == 2 or n == 3:
		return True
	i = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

def primes_below(n):
	if n < 2:
		return
	yield 2
	for p in range(3, n, 2):
		if is_prime(p):
			yield p

# t = time.process_time()
# sum(primes_below(2000000))
# elapsed_time = time.process_time() - t
# print('time: ', elapsed_time) # 29.75s

print( sum(primes_below(2000000)) )