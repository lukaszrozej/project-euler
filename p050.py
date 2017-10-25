# https://projecteuler.net/problem=50

from pyprimesieve import primes

ps = primes(1000000)
primes_count = len(ps)

max_p = 0
max_length = 0
for i in range(0, primes_count):
	s = ps[i]
	for j in range(i+1, primes_count):
		s += ps[j]
		if s > ps[-1]:
			break
		k = max(j+1, max_p)
		while k < primes_count:
			if s <= ps[k]:
				break
			k += 1
		if s == ps[k] and j - i + 1> max_length:
			max_length = j - i + 1
			max_p = k
max_p = ps[max_p]


print(max_length, max_p)