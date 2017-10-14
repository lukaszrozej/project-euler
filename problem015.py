# Starting in the top left corner of a 2×2 grid,
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# Theory:
# In an n by n grid each routw is a sequence of 2n moves
# with exactly n moves down and n moves right
# Choosing which moves are down determines the sequence
# So there are 2n choose n such sequences

import time

# 1. Using math factorial

from math import factorial

n = 20

print( factorial(2*n) // factorial(n) // factorial(n) )

# t = time.process_time()
# factorial(2*n) // factorial(n) // factorial(n)
# elapsed_time = time.process_time() - t
# print('time: ', elapsed_time) # 6.4069999999999405e-06

# 2. Writing my own n choose k

def comb(n, k):
	if k < 0 or k > n:
		return 0
	if n - k > k:
		k = n - k
	result = 1
	for i in range(k + 1, n + 1):
		result *= i
	for i in range(2, n - k + 1):
		result //= i
	return result

print( comb(2*n, n) )

# t = time.process_time()
# comb(2*n, n)
# elapsed_time = time.process_time() - t
# print('time: ', elapsed_time) # 1.3444000000001344e-05
		 