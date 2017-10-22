# https://projecteuler.net/problem=40

# nth digit of Champernowne's constant
def d(n):
	numbers_in_group = 9
	digits_per_number = 1
	smallest_in_group = 1
	digits_per_group = numbers_in_group * digits_per_number
	while n > digits_per_group:
		n -= digits_per_group
		numbers_in_group *= 10
		digits_per_number += 1
		smallest_in_group *= 10
		digits_per_group = numbers_in_group * digits_per_number
	q, r = divmod(n - 1, digits_per_number)
	return int( str(smallest_in_group + q)[r] )

for n in range(990, 1010):
	print(d(n))

print(d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000))

