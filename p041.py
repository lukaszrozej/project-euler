# https://projecteuler.net/problem=41

'''
1 + ... + n = n(n+1)/2
is divisible by 3 for all n except 1, 4, 7
1 is too small, so n can be only 4 or 7
Start from the alphabetically largest permutation
Stop the moment I find first prime
I skip permutations ending in an even number or 5
'''

from itertools import permutations, chain
from sympy import isprime

for p in chain(permutations('7654321'), permutations('4321')):
	if p[-1] in '137':
		n = int(''.join(p))
		if isprime(n):
			break

print(n)


