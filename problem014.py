# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import time

# 1. My solution with my own cache

cache = {1: 1}

def collatz_length(n):
	if n in cache:
		return cache[n]
	if n % 2 == 0:
		l = collatz_length(n // 2) + 1
	else:
		l = collatz_length(3 * n + 1) + 1
	cache[n] = l
	return l

def longest_collatz(bound):
	max_n = 0
	max = 0
	for n in range(1, bound):
		l = collatz_length(n)
		if max < l:
			max = l
			max_n = n
	return max_n, max

# t = time.process_time()
# longest_collatz(1000000)
# elapsed_time = time.process_time() - t
# print('time: ', elapsed_time) # 1.630797429s

print( longest_collatz(1000000) )

# 2. With lru_cache

from functools import lru_cache

@lru_cache(maxsize = None)
def collatz_length(n):
	if n == 1:
		return 1
	if n % 2 == 0:
		l = collatz_length(n // 2) + 1
	else:
		l = collatz_length(3 * n + 1) + 1
	return l

# t = time.process_time()
# longest_collatz(1000000)
# elapsed_time = time.process_time() - t
# print('time: ', elapsed_time) # 2.05428559s

print( longest_collatz(1000000) )
