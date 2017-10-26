# https://projecteuler.net/problem=53

import numpy as np

size = 101
treshold = 1000000
c = [0] * size
c[0] = 1

counter = 0
for n in range(1, size):
	for k in range(n, 0, -1):
		c[k] = c[k] + c[k-1]
		if c[k] > treshold:
			counter += 1

print(counter)