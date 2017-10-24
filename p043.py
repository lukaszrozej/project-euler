# https://projecteuler.net/problem=43

import time
from itertools import permutations
from re import sub
primes = (2,3,5,7,11,13,17)

# 1. Brute force

t = time.process_time()

total = 0
for p in permutations('0123456789'):
	s = ''.join(p)
	if all(	int(s[k:k+3]) % primes[k-1] == 0 for k in range(1, 8) ):
		total += int(s)

elapsed_time = time.process_time() - t
print('time: ', elapsed_time) # 13.335037617

print(total)

# 2. From divisibility rules by 5 and by 11:
# 	d6 = 5 and d8 = d7 + 6 % 11

t = time.process_time()

total = 0
for d7 in '01236789':
	d8 = str((int(d7)+6) % 11)
	for p in permutations( sub('['+d7+d8+']', '', '012346789') ):
		s = ''.join(p[:5]) + '5' + d7 + d8 + p[5] + p[6]
		if all(	int(s[k:k+3]) % primes[k-1] == 0 for k in range(1, 8) ):
			total += int(s)

elapsed_time = time.process_time() - t
print('time: ', elapsed_time) # 0.1907139529999995

print(total)
