# A perfect number is a number for which
# the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be
# 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n
# and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis,
# it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import time

# 1. Simple solution

# function from problem 21:
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

t = time.process_time()


abundant_numbers = { n for n in range(12, 28124 - 12) if n < sum_proper_divisors_of(n) }

abundant_numbers_sums = { n + m for n in abundant_numbers for m in abundant_numbers if n + m < 28124}

non_abundant_numbers_sums = { n for n in range(1, 28124) if n not in abundant_numbers_sums }

answer = sum( non_abundant_numbers_sums )


elapsed_time = time.process_time() - t
print('time: ', elapsed_time) # 0.00145s

print( answer )

# 2. With some optimization:
#    - if n is abundant so are all its multiples
# 	 - when finding abundant_numbers_sums don't consider both n,m and m,n

t = time.process_time()


bound = 28124
abundant_numbers = set()
for n in range(12, bound):
	if n not in abundant_numbers and n < sum_proper_divisors_of(n):
		for k in range(n, bound, n):
			abundant_numbers.add(k)

abundant_numbers = list(abundant_numbers)

# add all numbers
answer = bound * (bound - 1) // 2

# substract abundant_numbers_sums
abundant_numbers_sums = set()
for i, n in enumerate(abundant_numbers):
	for m in abundant_numbers[i:]:
		s = n + m
		if s < bound and s not in abundant_numbers_sums:
			abundant_numbers_sums.add(s)
			answer -= s

elapsed_time = time.process_time() - t
print('time: ', elapsed_time) # 0.00145s


print( answer )
