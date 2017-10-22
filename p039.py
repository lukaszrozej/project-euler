# https://projecteuler.net/problem=39

from math import sqrt, floor, ceil
from collections import defaultdict

solutions = defaultdict(set)
bound = 1000
m_max = int(sqrt(bound // 2))
for m in range(2, m_max):
	n_max = min(m, int(bound // 2 // m - m)+1)
	for n in range(1, n_max):
		a = m**2 - n**2
		b = 2*m*n
		c = m**2 + n**2
		p = a + b + c
		k = 1
		while p <= bound:
			solutions[p].add( frozenset( {k*a, k*b, k*c} ) )
			k += 1
			p += a + b + c

max_number = 0
max_triples = 0
for number, triples in solutions.items():
	length = len(triples)
	if length > max_triples:
		max_triples = length
		max_number = number

print(max_number)
print( str(solutions[max_number]). \
			replace('), ','\n'). \
			replace('{f', '{\nf'). \
			replace('frozenset(', '    '). \
			replace(')}', '\n}') \
		)