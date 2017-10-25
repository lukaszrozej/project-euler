# https://projecteuler.net/problem=47

from pyprimesieve import factorize
from itertools import count

counter = 0
for n in count(1):
	if len(factorize(n)) >= 4:
		counter += 1
		if counter == 4:
			break
	else:
		counter = 0

print(n-3)
