# https://projecteuler.net/problem=32

# Suppose
# a * b = c and a < b < c
# then
# if a is 1-digit then b is 4-digit
# if a is 2.digit then b is 3-digit
# a can't have more then 2 digits 

# 1. With itertools:

from itertools import permutations

def pandigital_products():
	products = set()
	for p in permutations('123456789'):
		s = ''.join(p)
		a = int(s[0])
		b = int(s[1:5])
		c = int(s[5:])
		if a * b == c:
			products.add(c)
		a = int(s[0:2])
		b = int(s[2:5])
		c = int(s[5:])
		if a * b == c:
			products.add(c)
	return products

print(sum(pandigital_products()))

# 2. With my implementation of Heap's algorithm for generating permutations

def heap_permutations(i):
	permutation = [ item for item in i ]
	def generate(n):
		if n == 1:
			yield permutation.copy()
		else:
			for k in range(0, n-1):
				yield from generate(n-1)
				if n % 2 == 0:
					permutation[k], permutation[n-1] = permutation[n-1], permutation[k]
				else:
					permutation[0], permutation[n-1] = permutation[n-1], permutation[0]
			yield from generate(n-1)
	yield from generate(len(permutation))

def pandigital_products1():
	products = set()
	for p in heap_permutations('123456789'):
		s = ''.join(p)
		a = int(s[0])
		b = int(s[1:5])
		c = int(s[5:])
		if a * b == c:
			products.add(c)
		a = int(s[0:2])
		b = int(s[2:5])
		c = int(s[5:])
		if a * b == c:
			products.add(c)
	return products

print(sum(pandigital_products()))

# import time

# t = time.process_time()
# pandigital_products()
# elapsed_time = time.process_time() - t
# print('time: ', elapsed_time) # 0.969953974

# t = time.process_time()
# pandigital_products1()
# elapsed_time = time.process_time() - t
# print('time: ', elapsed_time) # 2.138461594
