# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def sum_proper_divisors_of(n):
	result = 1
	d = 2
	while d*d <= n:
		q, r = divmod(n, d)
		if r == 0:
			result += d
			if q != d:
				result += q
		d += 1
	return result

def amicable_numbers_below(bound):
	result = set()
	for n in range(1, bound):
		if n not in result:
			m = sum_proper_divisors_of(n)
			if n != m and n == sum_proper_divisors_of(m):
				result.add(n)
				result.add(m)
	return result

print(  sum( amicable_numbers_below(10000) ) )