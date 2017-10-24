# https://projecteuler.net/problem=43

from itertools import permutations
primes = (2,3,5,7,11,13,17)

# s = '1406357289'
# for k in range(1, 8):
# 	print( int(s[k:k+3]) , primes[k-2] , int(s[k:k+3]) % primes[k-1] == 0  )


total = 0
for p in permutations('0123456789'):
	s = ''.join(p)
	if all(	int(s[k:k+3]) % primes[k-1] == 0 for k in range(1, 8) ):
		total += int(s)

print(total)