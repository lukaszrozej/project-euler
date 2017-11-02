# https://projecteuler.net/problem=61

from math import sqrt, floor, ceil

sets = [None] * 3

for s in range(3,9):
	sets.append(set())
	start = ceil( ( sqrt(8*(s-2)*1000 + (s-4)**2) + (s-4) ) / ( 2*(s-2) ) )
	stop = floor( ( sqrt(8*(s-2)*10000 + (s-4)**2) + (s-4) ) / ( 2*(s-2) ) )
	for n in range(start, stop):
		number = ( n*n * (s-2) + n*(s-4) ) // 2
		sets[s].add(number)
	print(s, ': ', len(sets[s]))
