# https://projecteuler.net/problem=52

from itertools import count

def powers_of(n):
	power = 1
	while True:
		yield power
		power *= n

def are_permutations(a, b):
	return sorted(str(a)) == sorted(str(b))

def find():
	for d in powers_of(10):
		for n in range(d, d*10//6+1):
			if all(	are_permutations(n, k*n) for k in range(2, 6) ):
				return n

print(find())