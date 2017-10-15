# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import time

# 1. By generating all permutations until the millionth

from itertools import islice, permutations

def lexicographic_permutations(n):
	permutation = list(range(0,n))
	while True:
		yield permutation
		i = n - 2
		while i >= 0 and permutation[i] > permutation[i+1]:
			i -= 1
		if i == -1:
			break
		j = n - 1
		while permutation[i] > permutation[j]:
			j -= 1
		permutation[i], permutation[j] = permutation[j], permutation[i]
		permutation[i+1:] = reversed(permutation[i+1:])

t = time.process_time()

millionth_permutation = next( islice(lexicographic_permutations(10), 999999, 1000000) )

elapsed_time = time.process_time() - t
print('time: ', elapsed_time) # 1.730069517

print( ''.join( map(str, millionth_permutation) ) )

# 2. Generating permutations with itertools

t = time.process_time()

millionth_permutation = next( islice( permutations(range(0, 10)), 999999, 10000000 ) )

elapsed_time = time.process_time() - t
print('time: ', elapsed_time) # 0.02583450900000006

print( ''.join( map(str, millionth_permutation) ) )

# 3. I can find the millionth permutation without going through the previous ones

import numpy as np

def lexicographic_permutation(size, index):
	factorial = 1
	factorials = np.zeros(size-1, dtype=int)
	for n in range(0,size-1):
		factorial *= n + 1
		factorials[size - (n+2)] = factorial

	permutation = list( range(0,size) )
	for n in range(0,size-1):
		q, r = divmod(index, factorials[n])
		permutation[n], permutation[n+1:n+q+1] = permutation[n+q], permutation[n:n+q]
		index = r
	
	return permutation
	
t = time.process_time()

millionth_permutation = lexicographic_permutation(10, 999999)

elapsed_time = time.process_time() - t
print('time: ', elapsed_time) # 4.486200000020091e-05

print( ''.join( map(str, millionth_permutation) ) )


