# https://projecteuler.net/problem=35

from sympy import isprime

count = 0
for n in range(1000000):
	s = str(n)
	if all( isprime(int(s[i:] + s[:i])) for i in range(0, len(s)) ):
		count += 1

print(count)