# https://projecteuler.net/problem=612

import numpy as np

# N = 3 -> 289665
# N = 4 -> 39235977
# N = 5 -> 4528635021
# N = 6 -> 481858831665

N = 18

combinations = np.zeros((10, 10), dtype=int)
combinations[:,0] = 1
for n in range(1,10):
	for k in range(1, n+1):
		combinations[n, k] = combinations[n-1, k] + combinations[n-1, k-1]

def comb(n,k):
	return int(combinations[n,k])

sum_over_k = 0
for k in range(1,10):
	sum_over_n = 0
	for n in range(1, N+1):
		sum_over_j = 0
		for j in range(0, k+1):
			if j % 2 == 0:
				sum_over_j += comb(k, j) * (k-j)**n
			else:
				sum_over_j += -comb(k, j) * (k-j)**n
		sum_over_n += sum_over_j
	sum_over_k += comb(9, k) * sum_over_n * (10**N - (10-k)**N)

for k in range(2,11):
	sum_over_n = 0
	for n in range(1, N+1):
		sum_over_j = 0
		for j in range(0, k):
			if j % 2 == 0:
				sum_over_j += comb(k-1, j) * (k-j)**(n-1) * (k-1)
			else:
				sum_over_j += -comb(k-1, j) * (k-j)**(n-1) * (k-1)
		sum_over_n += sum_over_j
	if k == 10:
		sub = 0
	elif k == 9:
		sub = N
	else:
		sub = (10-k) * ((10-k)**N - 1) // (10 - k - 1)
	sum_over_k += comb(9, k-1) * sum_over_n * (10**N - sub -1)

result = ((sum_over_k - 10**N + 1) // 2)
result %= 1000267129

print(result)